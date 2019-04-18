from . import purchases_blue,plan_func,need_func
from . import get_func,cost_func,sem_func,finish_func
from flask import g, render_template, request
from prosystem.utils.commons import login_required
# 首页模板数据加载
@purchases_blue.route('/fiveone')
@login_required
def fiveone():
    data = plan_func.getProdPlan(request)
    return data

@purchases_blue.route('/fivetwo')
@login_required
def fivetwo():
    data = need_func.getNeedPlan(request)
    return data

@purchases_blue.route('/fivethere')
@login_required
def fivethere():

    data = get_func.getPurchasePlan(request)
    return data

@purchases_blue.route('/fivefour')
@login_required
def fivefour():
    data = cost_func.getFinishCost(request)
    return data

@purchases_blue.route('/fivefive')
@login_required
def fivefive():
    data = sem_func.getSemData(request)
    return data

@purchases_blue.route('/fivesix')
@login_required
def fivesix():
    data = finish_func.getFinishCost(request)
    return data