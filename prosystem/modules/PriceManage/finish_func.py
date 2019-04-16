from prosystem import db
from .import other_func
from datetime import datetime
from prosystem.models import FinishedProduct,BomMain,BomSon
from flask import g, render_template, request, session
from prosystem.utils.response_code import RET
from flask import redirect, url_for, jsonify, current_app, abort

def getfinishdata(request):

    main_sel = request.args.get('m_sel', "")
    main_query_str = request.args.get('m_qstr', "")
    son_sel = request.args.get('s_sel', "")
    son_query_str = request.args.get('s_qstr', "")

    boms_dict_list1 =other_func.getplanlist(main_sel,main_query_str)
    if boms_dict_list1 =="":
        boms_dict_list1 = other_func.getplanlist(2, "货品编号是INT类型")
    # 获取分页后的数据
    boms_list2 = other_func.get_planpaginate(son_sel,son_query_str)
    if boms_list2 =="":
        boms_list2 = other_func.get_planpaginate(2, "货品编号是INT类型")
    boms_dict_list2 = other_func.get_boms_list(boms_list2)

    data = {
        "year": datetime.now().strftime("%Y"),
        "month": datetime.now().strftime("%m"),
        'main': {
            'boms_dict_list': boms_dict_list1,
            'm_sel': main_sel,
            'query_str':main_query_str,
        },
        'son': {
            'boms_dict_list': boms_dict_list2,
            's_sel': son_sel,
            'query_str': son_query_str,
        }
    }
    # 返回数据
    return render_template('four/fourfinishproinput.html', data=data)


def addfinishbom(request):

    plan_id = request.json.get('main_id', "")
    plan_name = request.json.get('main_name', "")
    unit = request.json.get('main_unit', "")
    num = request.json.get('num', '10')
    print(plan_id)
    # 转换参数的数据类型
    plan_id,num = int(plan_id),int(num)
    plan_demo = FinishedProduct()
    plan_demo.finished_id = plan_id
    plan_demo.finished_name = plan_name
    plan_demo.unit = unit
    plan_demo.num = num
    try:
        db.session.add(plan_demo)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        # 数据保存错误
        return jsonify(errno=RET.DATAERR, errmsg="数据保存错误")
    return jsonify(errno=RET.OK, errmsg="数据保存成功！！！")

def delfinishbom(request):
    id = request.json.get('id')
    # 转换参数的数据类型
    id= int(id)
    plan_demo = FinishedProduct.query.filter(FinishedProduct.id==id).first()
    try:
        db.session.delete(plan_demo)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        # 数据保存错误
        return jsonify(errno=RET.DATAERR, errmsg="数据保存错误")
    return jsonify(errno=RET.OK, errmsg="数据保存成功！！！")