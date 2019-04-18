from prosystem import db
from . import other_func
from datetime import datetime
from prosystem.models import AllCostInfo,BomMain
from prosystem.models import FinishedProduct
from prosystem.utils.response_code import RET
from flask import g, render_template, request, session
from flask import redirect, url_for, jsonify, current_app, abort

def getFinishCost(request):
    year = request.args.get('year', datetime.now().strftime("%Y"))
    try:
        plans_list = FinishedProduct.query.filter(FinishedProduct.is_add ==False,
        ).order_by(FinishedProduct.id.asc()).all()
    except Exception as e:
        db.session.commit()
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    for plans in plans_list:
        current_year = plans.date.strftime("%Y")
        current_month = plans.date.strftime("month"+"%m")#month04

        boms_sons_list = AllCostInfo.query.filter(AllCostInfo.main_id == plans.finished_id,
                    AllCostInfo.year == current_year,AllCostInfo.type=="消耗量")
        if boms_sons_list.count() == 0:
            plan = AllCostInfo(
                main_id=plans.finished_id,main_name=plans.finished_name,unit = plans.unit,
                cate = "产成品", year = current_year,type = "消耗量"
            )
            plan = other_func.getAllneedModel1(current_month,plan,plans)
            db.session.add(plan)
        else:
            plan = boms_sons_list.first()
            plan = other_func.getAllneedModel2(current_month, plan, plans)
            db.session.commit()
        try:
            FinishedProduct.query.filter_by(id=plans.id).update({"is_add":True})
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(errno=RET.DATAERR, errmsg="数据库操作失败！")
    try:
        boms_list = AllCostInfo.query.filter(AllCostInfo.cate=="产成品",
                AllCostInfo.type=="消耗量" , AllCostInfo.year == year).order_by(AllCostInfo.cate.asc())
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    data = other_func.get_boms_list(boms_list,year)
    return render_template('five/fivesix.html',data=data)