from prosystem import db
from sqlalchemy import or_,and_
from prosystem.models import User,BomMain,BomSon
from prosystem.utils.response_code import RET
from flask import g, render_template, request, session
from flask import redirect, url_for, jsonify, current_app, abort

def compare_size(page,total_page):
    if int(page) >= int(total_page) and total_page != 0:
        page = total_page
    return page

def get_page(paginate):
    boms_list = paginate.items
    total_page = paginate.pages
    current_page = paginate.page
    return boms_list,total_page,current_page

def get_paginate(main_sel,query_str,page,strtype):
    if query_str == "" :
        try:
            paginate = BomMain.query.filter(and_(or_(and_(BomMain.price>0,BomMain.cate == '自制半成品'),BomMain.cate ==strtype,),BomMain.is_bom=="N")).order_by(
                BomMain.id.asc()).paginate(page, 20, False)
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg='查询新闻数据失败')
        return paginate

    else:
        if int(main_sel) == 1:
            try:
                query_str = int(query_str)
            except Exception as e:
                current_app.logger.error(e)
                return ""
            try:
                paginate = BomMain.query.filter(and_(or_(and_(BomMain.price>0,BomMain.cate == '自制半成品'),BomMain.cate ==strtype,),BomMain.is_bom=="N",BomMain.main_id ==query_str)).order_by(
                    BomMain.id.asc()).paginate(page, 20, False)
            except Exception as e:
                current_app.logger.error(e)
                return jsonify(errno=RET.DBERR, errmsg='查询新闻数据失败')
            return paginate
        else:
            if int(main_sel) == 2:
                try:
                    query_str = str(query_str)
                except Exception as e:
                    current_app.logger.error(e)
                    return jsonify(errno=RET.PARAMERR, errmsg='参数格式错误')
                try:
                    paginate = BomMain.query.filter(and_(or_(and_(BomMain.price>0,BomMain.cate == '自制半成品'),BomMain.cate ==strtype,),BomMain.is_bom=="N",BomMain.main_name ==query_str)).order_by(
                        BomMain.id.asc()).paginate(page, 20, False)
                except Exception as e:
                    current_app.logger.error(e)
                    return jsonify(errno=RET.DBERR, errmsg='查询新闻数据失败')
                return paginate

def get_paginate2(main_sel,query_str,page):
    if query_str == "" :
        try:
            paginate = BomMain.query.filter(BomMain.cate != '产成品',BomMain.price>0).order_by(
                BomMain.id.asc()).paginate(page, 20, False)
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(errno=RET.DBERR, errmsg='查询新闻数据失败')
        return paginate

    else:
        if int(main_sel) == 1:
            try:
                query_str = int(query_str)
            except Exception as e:
                current_app.logger.error(e)
                return ""
            try:
                paginate = BomMain.query.filter(BomMain.cate != '产成品',BomMain.price>0,BomMain.main_id ==query_str).order_by(
                    BomMain.id.asc()).paginate(page, 20, False)
            except Exception as e:
                current_app.logger.error(e)
                return jsonify(errno=RET.DBERR, errmsg='查询新闻数据失败')
            return paginate
        else:
            if int(main_sel) == 2:
                try:
                    query_str = str(query_str)
                except Exception as e:
                    current_app.logger.error(e)
                    return jsonify(errno=RET.PARAMERR, errmsg='参数格式错误')
                try:
                    paginate = BomMain.query.filter(BomMain.cate != '产成品',BomMain.price>0,BomMain.main_name ==query_str).order_by(
                        BomMain.id.asc()).paginate(page, 20, False)
                except Exception as e:
                    current_app.logger.error(e)
                    return jsonify(errno=RET.DBERR, errmsg='查询新闻数据失败')
                return paginate

def get_boms_list(boms_list):
    boms_dict_list = []
    for boms in boms_list:
        boms_dict_list.append(boms.to_dict())
    return boms_dict_list