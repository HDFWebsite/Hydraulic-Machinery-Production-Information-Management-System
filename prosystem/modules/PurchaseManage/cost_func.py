from prosystem import db
from . import other_func
from datetime import datetime
from sqlalchemy import and_,or_
from prosystem.models import MaterialCost,AllCostInfo
from prosystem.models import MaterialRequire,SemifinishedCost
from prosystem.utils.response_code import RET
from flask import g, render_template, request, session
from flask import redirect, url_for, jsonify, current_app, abort

def getFinishCost(request):
    year = request.args.get('year', datetime.now().strftime("%Y"))
    try:
        plans_list = MaterialCost.query.filter(MaterialCost.is_add ==False
           ).order_by(MaterialCost.id.asc()).all()
    except Exception as e:
        db.session.commit()
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    for plans in plans_list:
        current_year = plans.date.strftime("%Y")
        current_month = plans.date.strftime("month"+"%m")#month04

        boms_sons_list = AllCostInfo.query.filter(AllCostInfo.main_id == plans.son_id,
            AllCostInfo.year == current_year,AllCostInfo.type=="消耗量")
        if boms_sons_list.count() == 0:
            plan = AllCostInfo(
                main_id=plans.son_id,main_name=plans.son_name,unit = plans.son_unit,
                cate = plans.son_cate, year = current_year,type = "消耗量"
            )
            plan = other_func.getAllneedModel1(current_month,plan,plans)
            db.session.add(plan)
        else:
            plan = boms_sons_list.first()
            plan = other_func.getAllneedModel2(current_month, plan, plans)
            db.session.commit()
        try:
            MaterialCost.query.filter_by(id=plans.id).update({"is_add":True})
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(errno=RET.DATAERR, errmsg="数据库操作失败！")

    try:
        plans_list = SemifinishedCost.query.filter(SemifinishedCost.is_add ==False
           ).order_by(SemifinishedCost.id.asc()).all()
    except Exception as e:
        db.session.commit()
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    for plans in plans_list:
        current_year = plans.date.strftime("%Y")
        current_month = plans.date.strftime("month"+"%m")#month04

        boms_sons_list = AllCostInfo.query.filter(AllCostInfo.main_id == plans.son_id,
          AllCostInfo.year == current_year,AllCostInfo.type=="消耗量")
        if boms_sons_list.count() == 0:
            plan = AllCostInfo(
                main_id=plans.son_id,main_name=plans.son_name,unit = plans.son_unit,
                cate = plans.son_cate, year = current_year,type = "消耗量"
            )
            plan = other_func.getAllneedModel1(current_month,plan,plans)
            db.session.add(plan)
        else:
            plan = boms_sons_list.first()
            plan = other_func.getAllneedModel2(current_month, plan, plans)
            db.session.commit()
        try:
            SemifinishedCost.query.filter_by(id=plans.id).update({"is_add":True})
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(errno=RET.DATAERR, errmsg="数据库操作失败！")

    try:
        boms_list = AllCostInfo.query.filter(and_(or_(AllCostInfo.cate =="原材料",AllCostInfo.cate =="辅助材料"),
            AllCostInfo.type=="消耗量" , AllCostInfo.year == year)).order_by(AllCostInfo.cate.asc())
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    data = other_func.get_boms_list(boms_list,year)
    return render_template('five/fivethere.html',data=data)