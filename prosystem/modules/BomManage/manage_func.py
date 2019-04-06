from prosystem import db
from  . import other_func
from sqlalchemy import or_,and_
from prosystem.models import User,BomMain,BomSon
from prosystem.utils.response_code import RET
from flask import g, render_template, request, session
from flask import redirect, url_for, jsonify, current_app, abort

def getbommain(request):

    main_id = request.args.get('main_id', "")
    main_name = request.args.get('main_name', "")
    my_sel = request.args.get('my_sel', "")
    my_qstr = request.args.get('my_qstr', "")

    # 转换参数的数据类型
    boms_list = get_main_list(my_sel,my_qstr)
    boms_dict_list = other_func.get_boms_list(boms_list)
    if boms_list =="" or len(boms_dict_list) == 0:
        data = {
            'main': {
                'boms_dict_list': {},
            },
            'son': {
                'main_id': None,
                'main_name': None,
                'boms_dict_list': {},
            }
        }
    else:
        if main_id == "":
            main_id = boms_dict_list[0]["main_id"]
            main_name = boms_dict_list[0]["main_name"]

        try:
            son_list = BomSon.query.filter(BomSon.main_id == main_id).all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg='查询新闻数据失败')
        boms_dict_list2 = []
        for boms in son_list:
            boms_dict_list2.append(boms.to_dict())

        data = {
            'main': {
                'boms_dict_list': boms_list,
            },
            'son': {
                'main_id': main_id,
                'main_name': main_name,
                'boms_dict_list': boms_dict_list2,
            }
        }

    # 返回数据
    return render_template('one/onebasemanage.html', data=data)


def get_main_list(my_sel,my_qstr):
    if my_sel == "" :
        try:
            boms_list = BomMain.query.filter(and_(or_(BomMain.cate == '产成品', BomMain.cate == '自制半成品'), BomMain.is_bom == 'Y')).order_by(BomMain.id.asc())
        except Exception as e:
            current_app.logger.error(e)
            return ""
        return boms_list
    if int(my_sel) == 1:
        try:
            query_str = int(my_qstr)
        except Exception as e:
            current_app.logger.error(e)
            return ""
        try:
            boms_list = BomMain.query.filter(and_(and_(or_(BomMain.cate == '产成品', BomMain.cate == '自制半成品'), BomMain.is_bom == 'Y')),BomMain.main_id == query_str).order_by(BomMain.id.asc())
        except Exception as e:
            current_app.logger.error(e)
            return ""
        return boms_list
    if int(my_sel) == 2:
        try:
            boms_list = BomMain.query.filter(and_(and_(or_(BomMain.cate == '产成品', BomMain.cate == '自制半成品'), BomMain.is_bom == 'Y')),BomMain.main_name == my_qstr).order_by(BomMain.id.asc())
        except Exception as e:
            current_app.logger.error(e)
            return ""
        return boms_list

def delete_bom_rel(main_id):
    try:
        BomMain.query.filter_by(main_id=int(main_id)).update({"is_bom":"N"})
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(e)
    try:
        bom_demo = BomSon.query.filter(BomSon.main_id==int(main_id)).all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！！！")
    for demo in bom_demo :
        try:
            db.session.delete(demo)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            # 数据保存错误
            return jsonify(errno=RET.DATAERR, errmsg="数据保存错误")
    return jsonify(errno=RET.OK, errmsg="数据保存成功！！！")


