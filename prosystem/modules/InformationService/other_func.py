from prosystem import db
from sqlalchemy import or_,and_
from prosystem.models import ProductionPlan,BomMain,BomSon
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

def getplanlist(main_sel,query_str):
    if query_str == "" :
        try:
            boms_list1 = BomMain.query.filter(BomMain.cate == '产成品', BomMain.is_bom == "Y").order_by(
                BomMain.id.asc()).all()
        except Exception as e:
            current_app.logger.error(e)
            return ""
        # 定义容器，存储查询到的新闻数据
        boms_dict_list1 = []
        for boms in boms_list1:
            try:
                sons_list1 = BomSon.query.filter(BomSon.main_id == boms.to_dict()["main_id"],
                                                 BomSon.son_cate == '自制半成品').order_by(BomSon.id.asc())
            except Exception as e:
                current_app.logger.error(e)
                return ""
            if sons_list1.count() >= 1:
                for sons1 in sons_list1:
                    try:
                        sons_list2 = BomMain.query.filter(BomMain.main_id == sons1.to_dict()["son_id"]).order_by(
                            BomMain.id.asc())
                    except Exception as e:
                        current_app.logger.error(e)
                        return ""

                    if sons_list2[0].to_dict()["is_bom"] == "Y":
                        boms_dict_list1.append(boms.to_dict())
            else:
                boms_dict_list1.append(boms.to_dict())
        return boms_dict_list1

    else:
        if int(main_sel) == 1:
            try:
                query_str = int(query_str)
            except Exception as e:
                current_app.logger.error(e)
                return ""
            try:
                boms_list1 = BomMain.query.filter(BomMain.main_id==query_str, BomMain.cate == '产成品', BomMain.is_bom == "Y").order_by(
                    BomMain.id.asc()).all()
            except Exception as e:
                current_app.logger.error(e)
                return ""
            # 定义容器，存储查询到的新闻数据
            boms_dict_list1 = []
            for boms in boms_list1:
                try:
                    sons_list1 = BomSon.query.filter(BomSon.main_id == boms.to_dict()["main_id"],
                                                     BomSon.son_cate == '自制半成品').order_by(BomSon.id.asc())
                except Exception as e:
                    current_app.logger.error(e)
                    return ""
                if sons_list1.count() >= 1:
                    for sons1 in sons_list1:
                        try:
                            sons_list2 = BomMain.query.filter(BomMain.main_id == sons1.to_dict()["son_id"]).order_by(
                                BomMain.id.asc())
                        except Exception as e:
                            current_app.logger.error(e)
                            return ""

                        if sons_list2[0].to_dict()["is_bom"] == "Y":
                            boms_dict_list1.append(boms.to_dict())
                else:
                    boms_dict_list1.append(boms.to_dict())
            return boms_dict_list1

        else:
            if int(main_sel) == 2:
                try:
                    query_str = str(query_str)
                except Exception as e:
                    current_app.logger.error(e)
                    return ""
                try:
                    boms_list1 = BomMain.query.filter(BomMain.main_name==query_str, BomMain.cate == '产成品', BomMain.is_bom == "Y").order_by(
                        BomMain.id.asc()).all()
                except Exception as e:
                    current_app.logger.error(e)
                    return ""
                # 定义容器，存储查询到的新闻数据
                boms_dict_list1 = []
                for boms in boms_list1:
                    try:
                        sons_list1 = BomSon.query.filter(BomSon.main_id == boms.to_dict()["main_id"],
                                                         BomSon.son_cate == '自制半成品').order_by(BomSon.id.asc())
                    except Exception as e:
                        current_app.logger.error(e)
                        return ""
                    if sons_list1.count() >= 1:
                        for sons1 in sons_list1:
                            try:
                                sons_list2 = BomMain.query.filter(BomMain.main_id == sons1.to_dict()["son_id"]).order_by(
                                    BomMain.id.asc())
                            except Exception as e:
                                current_app.logger.error(e)
                                return ""

                            if sons_list2[0].to_dict()["is_bom"] == "Y":
                                boms_dict_list1.append(boms.to_dict())
                    else:
                        boms_dict_list1.append(boms.to_dict())
                return boms_dict_list1


def get_planpaginate(main_sel,query_str):
    if query_str == "" :
        try:
            boms_list = ProductionPlan.query.filter(ProductionPlan.is_need==False).order_by(ProductionPlan.id.asc())
        except Exception as e:
            current_app.logger.error(e)
            return ""
        return boms_list
    if int(main_sel) == 1:
        try:
            query_str = int(query_str)
        except Exception as e:
            current_app.logger.error(e)
            return ""
        try:
            boms_list = ProductionPlan.query.filter(ProductionPlan.is_need==False,ProductionPlan.plan_id==query_str).order_by(ProductionPlan.id.asc())
        except Exception as e:
            current_app.logger.error(e)
            return ""
        return boms_list

    if int(main_sel) == 2:
        try:
            query_str = str(query_str)
        except Exception as e:
            current_app.logger.error(e)
            return ""
        try:
            boms_list = ProductionPlan.query.filter(ProductionPlan.is_need==False,ProductionPlan.plan_name==query_str).order_by(ProductionPlan.id.asc())
        except Exception as e:
            current_app.logger.error(e)
            return ""
        return boms_list


def get_boms_list(boms_list):
    boms_dict_list = []
    for boms in boms_list:
        boms_dict_list.append(boms.to_dict())
    return boms_dict_list