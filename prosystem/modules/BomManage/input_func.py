from prosystem import db
from  . import other_func
from datetime import datetime
from prosystem.models import User,BomMain,BomSon
from prosystem.utils.response_code import RET
from flask import g, render_template, request, session
from flask import redirect, url_for, jsonify, current_app, abort

def getbommain(request):
    main_page = request.args.get('m_page', '1')
    main_total_page = request.args.get('m_tpage', 0)
    son_page = request.args.get('s_page', '1')
    son_total_page = request.args.get('s_tpage', 0)


    main_page = other_func.compare_size(main_page, main_total_page)
    son_page = other_func.compare_size(son_page, son_total_page)

    # 转换参数的数据类型
    main_page, son_page,= int(main_page), int(son_page)
    paginate1 =other_func.get_paginate("","",main_page,'产成品')
    paginate2 = other_func.get_paginate2("","",son_page)

    # 获取分页后的数据
    boms_list1, total_page1, current_page1 = other_func.get_page(paginate1)
    boms_list2, total_page2, current_page2 = other_func.get_page(paginate2)

    # 定义容器，存储查询到的新闻数据
    boms_dict_list1  = other_func.get_boms_list(boms_list1)
    boms_dict_list2  = other_func.get_boms_list(boms_list2)

    data = {
        'main': {
            'boms_dict_list': boms_dict_list1,
            'total_page': total_page1,
            'current_page': current_page1,
        },
        'son': {
            'boms_dict_list': boms_dict_list2,
            'total_page': total_page2,
            'current_page': current_page2,
        }
    }
    # 返回数据
    return render_template('one/onebaseinput.html', data=data)

def getbommainquery(request):

    main_page = request.json.get('m_page', '1')
    query_key = request.json.get('query_key', "")
    query_sel = request.json.get('query_sel', "")
    query_text = request.json.get('query_text', "")
    if query_key == "":
        return jsonify(errno=RET.DBERR, errmsg='query_key不能为空!')
    # 转换参数的数据类型
    main_page = int(main_page)
    if query_key == "产成品":
        paginate1 =other_func.get_paginate(query_sel,query_text,main_page,query_key)
    else:
        paginate1 = other_func.get_paginate2(query_sel, query_text, main_page)
    # 获取分页后的数据
    boms_list, total_page, current_page = other_func.get_page(paginate1)
    # 定义容器，存储查询到的新闻数据
    boms_dict_list  = other_func.get_boms_list(boms_list)

    data = {
            'boms_dict': boms_dict_list,
            "total_page":total_page,
            "current_page":current_page
        }
    # 返回数据
    return jsonify(errno=RET.OK, data=data)


def addbommain(request):

    main_id = request.json.get('main_id')
    main_name = request.json.get('main_name')
    son_id = request.json.get('son_id')
    son_num = request.json.get('son_num')
    try:
        BomMain.query.filter_by(main_id=int(main_id)).update({"is_bom":"Y","date":datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
    try:
        maindemo = BomMain.query.filter_by(main_id=int(son_id)).first()
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    son_bom = BomSon()
    son_bom.main_id = int(main_id)
    son_bom.main_name = main_name
    son_bom.son_id = int(son_id)
    son_bom.son_name = maindemo.main_name
    son_bom.son_cate = maindemo.cate
    son_bom.num = int(son_num)
    son_bom.unit = maindemo.unit
    son_bom.price = maindemo.price
    son_bom.son_company = maindemo.company
    try:
        db.session.add(son_bom)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        # 数据保存错误
        return jsonify(errno=RET.DATAERR, errmsg="数据保存错误")
    return jsonify(errno=RET.OK, errmsg="数据保存成功！！！")
