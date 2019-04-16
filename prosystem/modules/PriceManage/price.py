from . import price_blue,finish_func,mater_func,static_func
from prosystem.utils.commons import login_required
from flask import g, render_template, request, session
# 首页模板数据加载
@price_blue.route('/fourfinishproinput')
@login_required
def fourfinishproinput():
    data = finish_func.getfinishdata(request)
    return data

@price_blue.route('/fourfinishproinputadd',methods=["POST"])
@login_required
def fourfinishproinputadd():

    data = finish_func.addfinishbom(request)
    print(data)
    return data

@price_blue.route('/fourfinishproinputdel',methods=["POST"])
@login_required
def fourfinishproinputdel():

    data = finish_func.delfinishbom(request)
    return data

@price_blue.route('/fourrawmccalculation')
@login_required
def fourrawmccalculation():
    data = mater_func.getRmaterdata(request)
    return data

@price_blue.route('/fourrawmccalculationadd',methods=["POST"])
@login_required
def fourrawmccalculationadd():
    data = mater_func.addRmaterdata(request)
    return data

@price_blue.route('/foursemmatercalculation')
@login_required
def foursemmatercalculation():
    data = mater_func.getSmaterdata(request)
    return data

@price_blue.route('/fourrawmcstatistics')
@login_required
def fourrawmcstatistics():
    data = static_func.getRawStatic(request)
    return data

@price_blue.route('/foursemimccalculation')
@login_required
def foursemimccalculation():

    data = static_func.getRSmaterdata(request)
    return data

@price_blue.route('/foursemimccalculationadd',methods=["POST"])
@login_required
def foursemimccalculationadd():

    data = static_func.addRSmaterdata(request)
    return data

@price_blue.route('/foursemimcstatistics')
@login_required
def foursemimcstatistics():
    data = static_func.getSSmaterdata(request)
    return data

@price_blue.route('/fourfinishcostcal')
@login_required
def fourfinishtotalcostcal():
    data = static_func.getFinishcost(request)
    return data