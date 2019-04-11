from prosystem import db
from  . import other_func
from datetime import datetime
from prosystem.models import User,BomMain,BomSon
from flask import g, render_template, request, session
from prosystem.utils.response_code import RET
from flask import redirect, url_for, jsonify, current_app, abort

def getbommain1(request):
    main_page = request.args.get('m_page', '1')
    main_total_page = request.args.get('m_tpage', 0)
    main_sel = request.args.get('m_sel', "")
    main_query_str = request.args.get('m_qstr', "")
    son_page = request.args.get('s_page', '1')
    son_total_page = request.args.get('s_tpage', 0)
    son_sel = request.args.get('s_sel', "")
    son_query_str = request.args.get('s_qstr', "")

    main_page = other_func.compare_size(main_page, main_total_page)
    son_page = other_func.compare_size(son_page, son_total_page)

    # 转换参数的数据类型
    main_page, son_page,= int(main_page), int(son_page)
    paginate1 =other_func.get_paginate1(main_sel,main_query_str,main_page,'原材料')
    if paginate1 == "":
        paginate1 = other_func.get_paginate1(2, "货品编号是INT类型", main_page, '原材料')
    paginate2 = other_func.get_paginate2(son_sel,son_query_str,son_page,'原材料')
    if paginate2 == "":
        paginate2 = other_func.get_paginate2(2, "货品编号是INT类型", son_page, '原材料')

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
            'per_page': 20,
            'm_sel': main_sel,
            'query_str':main_query_str,
        },
        'son': {
            'boms_dict_list': boms_dict_list2,
            'total_page': total_page2,
            'current_page': current_page2,
            'per_page': 15,
            's_sel': son_sel,
            'query_str': son_query_str,
        }
    }
    # 返回数据
    return render_template('two/twomaterialinput1.html', data=data)


def getbommain2(request):
    main_page = request.args.get('m_page', '1')
    main_total_page = request.args.get('m_tpage', 0)
    main_sel = request.args.get('m_sel', "")
    main_query_str = request.args.get('m_qstr', "")
    son_page = request.args.get('s_page', '1')
    son_total_page = request.args.get('s_tpage', 0)
    son_sel = request.args.get('s_sel', "")
    son_query_str = request.args.get('s_qstr', "")

    main_page = other_func.compare_size(main_page, main_total_page)
    son_page = other_func.compare_size(son_page, son_total_page)

    # 转换参数的数据类型
    main_page, son_page,= int(main_page), int(son_page)
    paginate1 =other_func.get_paginate1(main_sel,main_query_str,main_page,'辅助材料')
    if paginate1 == "":
        paginate1 = other_func.get_paginate1(2, "货品编号是INT类型", main_page, '辅助材料')
    paginate2 = other_func.get_paginate2(son_sel,son_query_str,son_page,'辅助材料')
    if paginate2 == "":
        paginate2 = other_func.get_paginate2(2, "货品编号是INT类型", son_page, '辅助材料')

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
            'per_page': 20,
            'm_sel': main_sel,
            'query_str':main_query_str,
        },
        'son': {
            'boms_dict_list': boms_dict_list2,
            'total_page': total_page2,
            'current_page': current_page2,
            'per_page': 15,
            's_sel': son_sel,
            'query_str': son_query_str,
        }
    }
    # 返回数据
    return render_template('two/twomaterialinput2.html', data=data)

def getbommain3(request):
    main_page = request.args.get('m_page', '1')
    main_total_page = request.args.get('m_tpage', 0)
    main_sel = request.args.get('m_sel', "")
    main_query_str = request.args.get('m_qstr', "")
    son_page = request.args.get('s_page', '1')
    son_total_page = request.args.get('s_tpage', 0)
    son_sel = request.args.get('s_sel', "")
    son_query_str = request.args.get('s_qstr', "")

    main_page = other_func.compare_size(main_page, main_total_page)
    son_page = other_func.compare_size(son_page, son_total_page)

    # 转换参数的数据类型
    main_page, son_page,= int(main_page), int(son_page)
    paginate1 =other_func.get_paginate1(main_sel,main_query_str,main_page,'自制半成品')
    if paginate1 == "":
        paginate1 = other_func.get_paginate1(2, "货品编号是INT类型", main_page, '自制半成品')
    paginate2 = other_func.get_paginate2(son_sel,son_query_str,son_page,'自制半成品')
    if paginate2 == "":
        paginate2 = other_func.get_paginate2(2, "货品编号是INT类型", son_page, '自制半成品')

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
            'per_page': 20,
            'm_sel': main_sel,
            'query_str':main_query_str,
        },
        'son': {
            'boms_dict_list': boms_dict_list2,
            'total_page': total_page2,
            'current_page': current_page2,
            'per_page': 15,
            's_sel': son_sel,
            'query_str': son_query_str,
        }
    }
    # 返回数据
    return render_template('two/twomaterialinput3.html', data=data)

def addbomprice(request):
    main_id = request.json.get('main_id', "")
    price = request.json.get('price', '')
    # 转换参数的数据类型
    try:
        bomdemo = BomMain.query.filter_by(main_id=int(main_id)).first()
        bomdemo.price = price
        bomdemo.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='保存数据失败！')
    else:
        return jsonify(errno=RET.OK, errmsg='保存数据成功！')

def delbomprice(request):
    main_id = request.json.get('main_id', "")
    # 转换参数的数据类型
    try:
        bomdemo = BomMain.query.filter_by(main_id=int(main_id)).first()
        bomdemo.price = 0.0
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print('保存数据失败！')
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='保存数据失败！')
    else:
        print('保存数据成功！')
        return jsonify(errno=RET.OK, errmsg='保存数据成功！')