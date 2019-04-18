from prosystem import db
from . import other_func
from datetime import datetime
from prosystem.models import AllNeedInfo,BomMain
from prosystem.models import MaterialRequire,ProductionPlan
from prosystem.utils.response_code import RET
from flask import g, render_template, request, session
from flask import redirect, url_for, jsonify, current_app, abort

def getPurchasePlan(request):
    year = request.args.get('year', datetime.now().strftime("%Y"))
    try:
        plans_list = MaterialRequire.query.filter(MaterialRequire.is_addg ==False,
        MaterialRequire.is_order ==True).order_by(MaterialRequire.id.asc()).all()
    except Exception as e:
        db.session.commit()
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    for plans in plans_list:
        current_year = plans.order_time.strftime("%Y")
        current_month = plans.order_time.strftime("month"+"%m")#month04

        boms_sons_list = AllNeedInfo.query.filter(AllNeedInfo.main_id == plans.require_id,
               AllNeedInfo.year == current_year,AllNeedInfo.type=="采购")
        if boms_sons_list.count() == 0:
            plan = AllNeedInfo(
                main_id=plans.require_id,main_name=plans.require_name,unit = plans.unit,
                cate = plans.cate, year = current_year,type = "采购"
            )
            plan = other_func.getAllneedModel1(current_month,plan,plans)
            db.session.add(plan)
        else:
            plan = boms_sons_list.first()
            plan = other_func.getAllneedModel2(current_month, plan, plans)
            db.session.commit()
        try:
            MaterialRequire.query.filter_by(id=plans.id).update({"is_addg":True})
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(errno=RET.DATAERR, errmsg="数据库操作失败！")
    try:
        boms_list = AllNeedInfo.query.filter(AllNeedInfo.cate!="产成品",
            AllNeedInfo.type=="采购" , AllNeedInfo.year == year).order_by(AllNeedInfo.cate.asc())
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    data = other_func.get_boms_list(boms_list,year)

    return render_template('five/fivethere.html',data=data)
