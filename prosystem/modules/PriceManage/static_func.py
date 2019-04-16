from prosystem import db
from .import other_func
from datetime import datetime
from prosystem.models import FinishedProduct,MaterialCost
from prosystem.models import BomSon,SemifinishedProduct,SemifinishedCost
from flask import g, render_template, request, session
from prosystem.utils.response_code import RET
from flask import redirect, url_for, jsonify, current_app, abort

def getRawStatic(request):
    pro_one = datetime.now().strftime("%Y-%m-01 00:00:00")
    # 获取数据
    try:
        boms_list1 = MaterialCost.query.filter(MaterialCost.date > pro_one,MaterialCost.son_cate=="原材料").order_by(MaterialCost.id.asc())
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    boms_dict_list1 = other_func.get_boms_list(boms_list1)

    try:
        boms_list2 = MaterialCost.query.filter(MaterialCost.date > pro_one,MaterialCost.son_cate=="辅助材料").order_by(
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
    return render_template('four/fourrawmcstatistics.html', data=data)

def getRSmaterdata(request):
    pro_one = datetime.now().strftime("%Y-%m-01 00:00:00")
    # 获取数据
    try:
        boms_list1 = SemifinishedProduct.query.filter(SemifinishedProduct.date > pro_one).order_by(SemifinishedProduct.id.asc())
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    boms_dict_list1 = other_func.get_boms_list(boms_list1)

    try:
        boms_list2 = SemifinishedCost.query.filter(SemifinishedCost.date > pro_one).order_by(
            SemifinishedCost.id.asc())
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
    return render_template('four/foursemimccalculation.html', data=data)

def addRSmaterdata(request):
    # 获取数据
    pro_one = datetime.now().strftime("%Y-%m-01 00:00:00")
    try:
        boms_list1 = SemifinishedProduct.query.filter(SemifinishedProduct.is_cal == False, SemifinishedProduct.date > pro_one).all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    for boms in boms_list1:
        try:
            boms_son_list1 = BomSon.query.filter(BomSon.main_id == boms.son_id).all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
        for sons in boms_son_list1:
            material = SemifinishedCost()
            material.spid = boms.id
            material.semi_id = boms.son_id
            material.semi_name = boms.son_name
            material.unit = boms.son_unit
            material.num = boms.son_num
            material.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            material.son_id = sons.son_id
            material.son_name = sons.son_name
            material.son_num = boms.son_num * sons.num
            material.son_unit = sons.unit
            material.son_cate = sons.son_cate
            material.unit_price = sons.price
            material.total_price = float(boms.num) * float(sons.num)*sons.price
            try:
                db.session.add(material)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                current_app.logger.error(e)
                return jsonify(errno=RET.DATAERR, errmsg="数据保存错误")
        try:
            SemifinishedProduct.query.filter_by(finished_id=boms.finished_id).update({"is_cal": True})
            db.session.commit()
        except Exception as e:
            print("err")
            db.session.rollback()
            current_app.logger.error(e)
    return jsonify(errno=RET.OK, errmsg="数据保存成功！！！")

def getSSmaterdata(request):
    pro_one = datetime.now().strftime("%Y-%m-01 00:00:00")
    try:
        boms_list = SemifinishedProduct.query.filter(SemifinishedProduct.date > pro_one,SemifinishedProduct.total_cost==None).order_by(
            SemifinishedProduct.id.asc())
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    for boms in boms_list:
        try:
            boms_sons_list1 = SemifinishedCost.query.filter(SemifinishedCost.spid ==boms.id,
                SemifinishedCost.son_cate=="原材料").order_by(SemifinishedCost.id.asc())
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
        raw_cost = 0.0
        for sons1 in boms_sons_list1:
            raw_cost += sons1.total_price
        try:
            boms_sons_list2 = SemifinishedCost.query.filter(SemifinishedCost.spid ==boms.id,
                SemifinishedCost.son_cate=="辅助材料").order_by(SemifinishedCost.id.asc())
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
        aux_cost =0.0
        for sons2 in boms_sons_list2:
            aux_cost += sons2.total_price
        boms.raw_cost = raw_cost
        boms.aux_cost = aux_cost
        boms.total_cost = raw_cost + aux_cost+ int(boms.son_num) *boms.unit_cost
        boms.pro_cost = boms.total_cost/int(boms.num)
        db.session.commit()
    try:
        boms_list = FinishedProduct.query.filter(FinishedProduct.date > pro_one,
            FinishedProduct.total_cost == None).order_by(FinishedProduct.id.asc())
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    for boms2 in boms_list:
        # 原材料
        try:
            boms_sons_list1 = MaterialCost.query.filter(MaterialCost.fpid == boms2.id,
              MaterialCost.son_cate == "原材料").order_by(MaterialCost.id.asc())
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
        raw_cost = 0.0
        for sons3 in boms_sons_list1:
            raw_cost += sons3.total_price
        # 辅助材料
        try:
            boms_sons_list2 = MaterialCost.query.filter(MaterialCost.fpid == boms2.id,
                MaterialCost.son_cate == "辅助材料").order_by(MaterialCost.id.asc())
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
        aux_cost = 0.0
        for sons4 in boms_sons_list2:
            aux_cost += sons4.total_price
        # 半成品
        try:
            boms_sons_list3 = SemifinishedProduct.query.filter(SemifinishedProduct.fpid == boms2.id).order_by(SemifinishedProduct.id.asc())
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
        sem_cost = 0.0
        sraw_cost = 0.0
        saux_cost = 0.0
        for sons5 in boms_sons_list3:
            sraw_cost += sons5.raw_cost
            saux_cost += sons5.aux_cost
            sem_cost += sons5.all_cost
        boms2.raw_cost = raw_cost+sraw_cost
        boms2.aux_cost = aux_cost+saux_cost
        boms2.sem_cost = sem_cost
        boms2.total_cost = raw_cost + aux_cost + sem_cost+sraw_cost+saux_cost
        boms2.pro_cost = boms2.total_cost / int(boms2.num)
        db.session.commit()
    try:
        sboms_list = SemifinishedProduct.query.filter(SemifinishedProduct.date > pro_one).order_by(
            SemifinishedProduct.id.asc())
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    boms_dict_list = other_func.get_boms_list(sboms_list)
    data = {
        "year": datetime.now().strftime("%Y"),
        "month": datetime.now().strftime("%m"),
        'main': {
            'boms_dict_list': boms_dict_list,
        }
    }
    # 返回数据
    return render_template('four/foursemimcstatistics.html', data=data)

def getFinishcost(request):
    pro_one = datetime.now().strftime("%Y-%m-01 00:00:00")
    try:
        sboms_list = FinishedProduct.query.filter(FinishedProduct.date > pro_one).order_by(
            FinishedProduct.id.asc())
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    boms_dict_list = other_func.get_boms_list(sboms_list)
    data = {
        "year": datetime.now().strftime("%Y"),
        "month": datetime.now().strftime("%m"),
        'main': {
            'boms_dict_list': boms_dict_list,
        }
    }
    return render_template('four/fourfinishcostcal.html', data=data)