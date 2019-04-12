from . import infos_blue,plan_func,cal_func,order_func
from sqlalchemy import or_
from prosystem.models import User,BomMain,ProductionPlan,BomSon
from prosystem.utils.commons import login_required
from prosystem.utils.response_code import RET
from flask import g, render_template, request, session
from flask import redirect, url_for, jsonify, current_app, abort
# 首页模板数据加载
@infos_blue.route('/thereproplaninput')
@login_required
def thereproplaninput():
    data = plan_func.getplandata(request)
    return data

@infos_blue.route('/thereproplaninputadd',methods=["POST"])
@login_required
def thereproplaninputadd():
    data =plan_func.addbomplan(request)
    return data

@infos_blue.route('/thereproplaninputdel',methods=["POST"])
@login_required
def thereproplaninputdel():
    data =plan_func.delbomplan(request)
    return data

@infos_blue.route('/theremareqcalculation')
@login_required
def theremareqcalculation():
    data = cal_func.getcaldata(request)
    return data

@infos_blue.route('/theremareqcalculationadd', methods=["POST"])
@login_required
def theremareqcalculationadd():
    data = cal_func.addbomcal(request)
    return data

@infos_blue.route('/therepurchaseorderget')
@login_required
def therepurchaseorderget():
    data = order_func.getorderdata(request)
    return data

@infos_blue.route('/therepurchaseordergetadd', methods=["POST"])
@login_required
def therepurchaseordergetadd():
    data = order_func.addorderdata(request)
    return data

@infos_blue.route('/thereproarrivalmanage')
@login_required
def thereproarrivalmanage():
    data = order_func.getarrivedata(request)
    return data

@infos_blue.route('/thereproarrivalmanageadd', methods=["POST"])
@login_required
def thereproarrivalmanageadd():
    data = order_func.addarrivedata(request)
    return data