from prosystem import db
from .import other_func
from datetime import datetime
from prosystem.models import ProductionPlan,MaterialRequire
from prosystem.models import AllNeedInfo,BomSon
from flask import g, render_template, request, session
from prosystem.utils.response_code import RET
from flask import redirect, url_for, jsonify, current_app, abort

def getcaldata(request):
    pro_one = datetime.now().strftime("%Y-%m-01 00:00:00")
   # 获取数据
    try:
        boms_list1 = ProductionPlan.query.filter(ProductionPlan.date>pro_one).order_by(ProductionPlan.id.asc())
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    boms_dict_list1 = other_func.get_boms_list(boms_list1)

    try:
        boms_list2 = MaterialRequire.query.filter(MaterialRequire.plan_time>pro_one).order_by(MaterialRequire.id.asc())
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    boms_dict_list2 = other_func.get_boms_list(boms_list2)
    data = {
        "year": datetime.now().strftime("%Y"),
        "month": datetime.now().strftime("%m"),
        'main': {
            'boms_dict_list': boms_dict_list1,
        },
        'son': {
            'boms_dict_list': boms_dict_list2,
        }
    }
    # 返回数据
    return render_template('there/theremareqcalculation.html', data=data)


def addbomcal(request):
    # 获取数据
    pro_one = datetime.now().strftime("%Y-%m-01 00:00:00")
    try:
        boms_list1 = ProductionPlan.query.filter(ProductionPlan.is_need==False,ProductionPlan.date>pro_one).all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    for boms in boms_list1:
        try:
            boms_son_list1 = BomSon.query.filter(BomSon.main_id ==boms.plan_id).all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
        for sons in boms_son_list1:
            if sons.son_cate != "自制半成品":
                require = MaterialRequire()
                require.plan_id = boms.plan_id
                require.plan_name = boms.plan_name
                require.plan_time = boms.date
                require.plan_unit = boms.unit
                require.plan_num = boms.num
                require.require_id = sons.son_id
                require.require_name = sons.son_name
                require.unit = sons.unit
                require.num = boms.num*sons.num
                require.cate = sons.son_cate
                require.company = sons.son_company
                require.is_order = False
                require.is_get = False
                require.build_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                try:
                    db.session.add(require)
                    db.session.commit()
                except Exception as e:
                    db.session.rollback()
                    current_app.logger.error(e)
                    return jsonify(errno=RET.DATAERR, errmsg="数据保存错误")
            else:
                try:
                    boms_son_list2 = BomSon.query.filter(BomSon.main_id == sons.son_id).all()
                except Exception as e:
                    current_app.logger.error(e)
                    return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
                for sons1 in boms_son_list2:
                    require = MaterialRequire()
                    require.plan_id = boms.plan_id
                    require.plan_name = boms.plan_name
                    require.plan_time = boms.date
                    require.plan_unit = boms.unit
                    require.plan_num = boms.num
                    require.require_id = sons1.son_id
                    require.require_name = sons1.son_name
                    require.unit = sons1.unit
                    require.num = boms.num * sons.num *sons1.num
                    require.cate =sons1.son_cate
                    require.company = sons1.son_company
                    require.is_order = False
                    require.is_get = False
                    require.build_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    try:
                        db.session.add(require)
                        db.session.commit()
                    except Exception as e:
                        db.session.rollback()
                        current_app.logger.error(e)
                        return jsonify(errno=RET.DATAERR, errmsg="数据保存错误")
        try:
            ProductionPlan.query.filter_by(plan_id=boms.plan_id).update({"is_need": True})
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
    return jsonify(errno=RET.OK, errmsg="数据保存成功！！！")