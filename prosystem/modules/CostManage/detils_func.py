from prosystem import db
from datetime import datetime
from prosystem.models import FinishedProduct,MaterialCost
from prosystem.models import BomSon,SemifinishedProduct,SemifinishedCost
from flask import g, render_template, request, session
from prosystem.utils.response_code import RET
from flask import redirect, url_for, jsonify, current_app, abort

def get_boms_list1(boms_list,year,month):
    boms_dict_list = []
    raw_cost,aux_cost,all_cost,total_cost =0,0,0,0
    for boms in boms_list:
        raw_cost += boms.raw_cost
        aux_cost += boms.aux_cost
        all_cost += boms.all_cost
        total_cost += boms.total_cost
        boms_dict_list.append(boms.to_dict())
    data = {
        "year1": datetime.now().strftime("%Y"),
        "year2": int(datetime.now().strftime("%Y"))-1,
        "year3": int(datetime.now().strftime("%Y"))-2,
        "year4": int(datetime.now().strftime("%Y"))-3,
        "query_year": int(year),
        "query_month": str(month),
        'boms_dict_list': boms_dict_list,
        'raw_cost': raw_cost,
        'aux_cost': aux_cost,
        'unit_cost': all_cost,
        'total_cost': total_cost,
    }
    return data


def get_boms_list2(boms_list,year,month):
    boms_dict_list = []
    raw_cost, aux_cost, sem_cost, total_cost = 0, 0, 0, 0
    for boms in boms_list:
        raw_cost += boms.raw_cost
        aux_cost += boms.aux_cost
        sem_cost += boms.sem_cost
        total_cost += boms.total_cost
        boms_dict_list.append(boms.to_dict())
    data = {
        "year1": datetime.now().strftime("%Y"),
        "year2": int(datetime.now().strftime("%Y"))-1,
        "year3": int(datetime.now().strftime("%Y"))-2,
        "year4": int(datetime.now().strftime("%Y"))-3,
        "query_year": int(year),
        "query_month": str(month),
        'boms_dict_list': boms_dict_list,
        'raw_cost': raw_cost,
        'aux_cost': aux_cost,
        'sem_cost': sem_cost,
        'total_cost': total_cost,
    }
    return data

def getDetailSemCost(request):
    year = request.args.get('year', datetime.now().strftime("%Y"))
    month = request.args.get('month', datetime.now().strftime("%m"))
    start = datetime.now().strftime(year+"-"+month+"-01 00:00:00")
    end = datetime.now().strftime(year+"-"+str(int(month)+1)+"-01 00:00:00")
    try:
        sboms_list = SemifinishedProduct.query.filter(SemifinishedProduct.date > start,
        SemifinishedProduct.date <end).order_by(SemifinishedProduct.id.asc())
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    data = get_boms_list1(sboms_list,year,month)

    return render_template('six/sixthere.html', data=data)


def getDetailFinishCost(request):
    year = request.args.get('year', datetime.now().strftime("%Y"))
    month = request.args.get('month', datetime.now().strftime("%m"))
    start = datetime.now().strftime(year + "-" + month + "-01 00:00:00")
    end = datetime.now().strftime(year + "-" + str(int(month) + 1) + "-01 00:00:00")
    try:
        sboms_list = FinishedProduct.query.filter(FinishedProduct.date > start,
                   FinishedProduct.date < end).order_by(FinishedProduct.id.asc())
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据查询失败！")
    data = get_boms_list2(sboms_list,year,month)
    return render_template('six/sixfive.html', data=data)