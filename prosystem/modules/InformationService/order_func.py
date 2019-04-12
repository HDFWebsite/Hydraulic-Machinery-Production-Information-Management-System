from prosystem import db
from .import other_func
from datetime import datetime
from prosystem.models import ProductionPlan,MaterialRequire,BomSon
from flask import g, render_template, request, session
from prosystem.utils.response_code import RET
from flask import redirect, url_for, jsonify, current_app, abort

def getorderdata(request):
    pro_one = datetime.now().strftime("%Y-%m-01 00:00:00")
   # 获取数据
    try:
        boms_list = MaterialRequire.query.filter(MaterialRequire.plan_time>pro_one).order_by(MaterialRequire.id.asc())
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    boms_dict_list = other_func.get_boms_list(boms_list)
    data = {
        "year": datetime.now().strftime("%Y"),
        "month": datetime.now().strftime("%m"),
        'boms_dict_list': boms_dict_list,
    }
    # 返回数据
    return render_template('there/therepurchaseorderget.html', data=data)

def addorderdata(request):
    id = request.json.get('id')
    try:
        MaterialRequire.query.filter_by(id=int(id)).update({"is_order":True,"order_time":datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
    return jsonify(errno=RET.OK, errmsg="数据保存成功！！！")


def getarrivedata(request):
    pro_one = datetime.now().strftime("%Y-%m-01 00:00:00")
   # 获取数据
    try:
        boms_list = MaterialRequire.query.filter(MaterialRequire.plan_time>pro_one,MaterialRequire.is_order==True).order_by(MaterialRequire.id.asc())
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    boms_dict_list = other_func.get_boms_list(boms_list)
    data = {
        "year": datetime.now().strftime("%Y"),
        "month": datetime.now().strftime("%m"),
        'boms_dict_list': boms_dict_list,
    }
    # 返回数据
    return render_template('there/thereproarrivalmanage.html', data=data)

def addarrivedata(request):
    id = request.json.get('id')
    try:
        MaterialRequire.query.filter_by(id=int(id)).update({"is_get":True,"get_time":datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
    return jsonify(errno=RET.OK, errmsg="数据保存成功！！！")