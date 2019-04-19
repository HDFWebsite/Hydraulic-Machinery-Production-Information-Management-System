from . import cost_blue,cost_func
from . import sem_func,finish_func,detils_func
from flask import render_template,request
from prosystem.utils.commons import login_required
# 首页模板数据加载
@cost_blue.route('/sixone')
@login_required
def sixone():
    data = cost_func.getFinishCost(request)
    return data


@cost_blue.route('/sixtwo')
@login_required
def sixtwo():
    data = sem_func.getSemData(request)
    return data

@cost_blue.route('/sixthere')
@login_required
def sixthere():

    data = detils_func.getDetailSemCost(request)
    return data

@cost_blue.route('/sixfour')
@login_required
def sixfour():
    data = finish_func.getFinishCost(request)
    return data

@cost_blue.route('/sixfive')
@login_required
def sixfive():
    data = detils_func.getDetailFinishCost(request)
    return data