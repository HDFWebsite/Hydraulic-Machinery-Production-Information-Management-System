from prosystem import db
from . import other_func
from prosystem.models import User,BomMain,BomSon
from prosystem.utils.response_code import RET
from flask import g, render_template, request, session
from flask import redirect, url_for, jsonify, current_app, abort

def getbommain(request):
    page = request.args.get('page', 1)
    per_page = request.args.get('per_page', 20)
    total_page = request.args.get('total_page', 0)
    query_str = request.args.get('query_str', "")

    page = other_func.compare_size(page,total_page)
    # 转换参数的数据类型
    page, per_page, query_str= int(page), int(per_page),str(query_str)

    if query_str == "" :
        try:
            paginate = BomMain.query.order_by(BomMain.id.asc()).paginate(page, per_page, False)
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg='查询新闻数据失败')
        try:
            count = BomMain.query.filter_by().count()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg='查询新闻数据失败')
    else:
        try:
            count = BomMain.query.filter_by(main_name=query_str).count()
        except Exception as e:
            current_app.logger.error(e)
            return render_template('other/errorHtml.html')
        try:
            paginate = BomMain.query.filter_by(main_name=query_str).order_by(BomMain.id.asc()).paginate(page, per_page, False)
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg='查询新闻数据失败')
    # 获取分页后的数据
    boms_list,total_page,current_page=other_func.get_page(paginate)

    # 定义容器，存储查询到的新闻数据
    boms_dict_list = other_func.get_boms_list(boms_list)
    data = {
        'boms_dict_list': boms_dict_list,
        'total_page': total_page,
        'current_page': current_page,
        'per_page':per_page,
        'count':count,
        'query_str':query_str
    }
    return render_template('one/onebaseinfo.html',data=data)

def addbommain(request):
    food_num = request.json.get('food_num')
    food_name = request.json.get('food_name')
    food_spec = request.json.get('food_spec')
    food_cate = request.json.get('food_cate')
    food_unit = request.json.get('food_unit')
    food_company = request.json.get('food_company')
    bom_demo = BomMain()
    bom_demo.main_id = int(food_num)
    bom_demo.main_name = food_name
    bom_demo.spec = food_spec
    bom_demo.cate = food_cate
    bom_demo.unit = food_unit
    bom_demo.company = food_company
    try:
        db.session.add(bom_demo)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        # 数据保存错误
        return jsonify(errno=RET.DATAERR, errmsg="数据保存错误")
    return jsonify(errno=RET.OK, errmsg="数据保存成功！！！")

def delbommain(request):
    main_id = request.args.get("main_id")
    try:
        bom_demo = BomMain.query.filter_by(main_id=main_id).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！！！")
    try:
        db.session.delete(bom_demo)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
        # 数据保存错误
        return jsonify(errno=RET.DATAERR, errmsg="数据保存错误")
    return jsonify(errno=RET.OK, errmsg="数据保存成功！！！")