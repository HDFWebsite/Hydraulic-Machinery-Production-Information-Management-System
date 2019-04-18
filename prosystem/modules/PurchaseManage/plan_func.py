from prosystem import db
from datetime import datetime
from . import other_func
from prosystem.models import AllNeedInfo,BomMain
from prosystem.models import BomMain,ProductionPlan
from prosystem.utils.response_code import RET
from flask import g, render_template, request, session
from flask import redirect, url_for, jsonify, current_app, abort

def getProdPlan(request):
    year = request.args.get('year', datetime.now().strftime("%Y"))
    try:
        plans_list = ProductionPlan.query.filter(ProductionPlan.is_add ==False).order_by(ProductionPlan.id.asc()).all()
    except Exception as e:
        db.session.commit()
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    for plans in plans_list:
        current_year = plans.date.strftime("%Y")
        current_month = plans.date.strftime("month"+"%m")#month04

        boms_sons_list = AllNeedInfo.query.filter(AllNeedInfo.main_id == plans.plan_id,
               AllNeedInfo.year == current_year)
        if boms_sons_list.count() == 0:
            plan = AllNeedInfo(
                main_id=plans.plan_id,main_name=plans.plan_name,unit = plans.unit,
                cate = "产成品", year = current_year,type = "产成品"
            )
            plan = other_func.getAllneedModel1(current_month,plan,plans)
            db.session.add(plan)
        else:
            plan = boms_sons_list.first()
            plan = other_func.getAllneedModel2(current_month, plan, plans)
            db.session.commit()
        try:
            ProductionPlan.query.filter_by(id=plans.id).update({"is_add":True})
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(errno=RET.DATAERR, errmsg="数据库操作失败！")
    try:
        boms_list = AllNeedInfo.query.filter(AllNeedInfo.cate=="产成品",
        AllNeedInfo.year == year).order_by(AllNeedInfo.id.asc())
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    data = other_func.get_boms_list(boms_list,year)

    return render_template('five/fiveone.html',data=data)