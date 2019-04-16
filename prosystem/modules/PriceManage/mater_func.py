from prosystem import db
from .import other_func
from datetime import datetime
from prosystem.models import FinishedProduct,MaterialCost
from prosystem.models import BomSon,SemifinishedProduct
from flask import g, render_template, request, session
from prosystem.utils.response_code import RET
from flask import redirect, url_for, jsonify, current_app, abort

def getRmaterdata(request):
    pro_one = datetime.now().strftime("%Y-%m-01 00:00:00")
    # 获取数据
    try:
        boms_list1 = FinishedProduct.query.filter(FinishedProduct.date > pro_one).order_by(FinishedProduct.id.asc())
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    boms_dict_list1 = other_func.get_boms_list(boms_list1)

    try:
        boms_list2 = MaterialCost.query.filter(MaterialCost.date > pro_one).order_by(
            MaterialCost.id.asc())
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
    return render_template('four/fourrawmccalculation.html', data=data)


def addRmaterdata(request):
    # 获取数据
    pro_one = datetime.now().strftime("%Y-%m-01 00:00:00")
    try:
        boms_list1 = FinishedProduct.query.filter(FinishedProduct.is_cal == False, FinishedProduct.date > pro_one).all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    for boms in boms_list1:
        try:
            boms_son_list1 = BomSon.query.filter(BomSon.main_id == boms.finished_id,BomSon.son_cate!="自制半成品").all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
        for sons in boms_son_list1:
            material = MaterialCost()
            material.fpid = boms.id
            material.finished_id = boms.finished_id
            material.finished_name = boms.finished_name
            material.unit = boms.unit
            material.num = boms.num
            material.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            material.son_id = sons.son_id
            material.son_name = sons.son_name
            material.son_num = boms.num * sons.num
            material.son_unit = sons.unit
            material.son_cate = sons.son_cate
            material.unit_price = sons.price
            material.total_price = boms.num * sons.num * sons.price
            try:
                db.session.add(material)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                current_app.logger.error(e)
                return jsonify(errno=RET.DATAERR, errmsg="数据保存错误")
        try:
            boms_son_list1 = BomSon.query.filter(BomSon.main_id == boms.finished_id, BomSon.son_cate == "自制半成品").all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
        for sons in boms_son_list1:
            finish = SemifinishedProduct()
            finish.fpid = boms.id
            finish.finished_id = boms.finished_id
            finish.finished_name = boms.finished_name
            finish.unit = boms.unit
            finish.num = boms.num
            finish.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            finish.son_id = sons.son_id
            finish.son_name = sons.son_name
            finish.son_num = boms.num * sons.num
            finish.son_unit = sons.unit
            finish.unit_cost = sons.price
            finish.all_cost = sons.price * boms.num * sons.num
            try:
                db.session.add(finish)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                current_app.logger.error(e)
                return jsonify(errno=RET.DATAERR, errmsg="数据保存错误")
        try:
            FinishedProduct.query.filter_by(finished_id=boms.finished_id).update({"is_cal": True,"cal_date":datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
    return jsonify(errno=RET.OK, errmsg="数据保存成功！！！")

def getSmaterdata(request):
    pro_one = datetime.now().strftime("%Y-%m-01 00:00:00")
    # 获取数据
    try:
        boms_list1 = FinishedProduct.query.filter(FinishedProduct.date > pro_one).order_by(FinishedProduct.id.asc())
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    boms_dict_list1 = other_func.get_boms_list(boms_list1)

    try:
        boms_list2 = SemifinishedProduct.query.filter(SemifinishedProduct.date > pro_one).order_by(
            SemifinishedProduct.id.asc())
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
    return render_template('four/foursemmatercalculation.html', data=data)