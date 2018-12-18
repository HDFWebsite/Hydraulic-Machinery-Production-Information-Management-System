from flask import render_template
from . import price_blue
# 首页模板数据加载
@price_blue.route('/fourfinishproinput')
# @login_required
def fourfinishproinput():

    data = {
        'user_info':'黄德飞'
    }
    return render_template('fourfinishproinput.html',data=data)


@price_blue.route('/fourrawmccalculation')
# @login_required
def fourrawmccalculation():

    data = {
        'user_info':'黄德飞'
    }
    return render_template('fourrawmccalculation.html',data=data)

@price_blue.route('/fourrawmcstatistics')
# @login_required
def fourrawmcstatistics():
    data = {
        'user_info':'黄德飞'
    }
    return render_template('fourrawmcstatistics.html',data=data)

@price_blue.route('/foursemimccalculation')
# @login_required
def foursemimccalculation():
    data = {
        'user_info':'黄德飞'
    }
    return render_template('foursemimccalculation.html',data=data)

@price_blue.route('/foursemimcstatistics')
# @login_required
def foursemimcstatistics():
    data = {
        'user_info':'黄德飞'
    }
    return render_template('foursemimcstatistics.html',data=data)