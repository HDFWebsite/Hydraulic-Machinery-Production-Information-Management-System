from flask import render_template
from . import purchases_blue
# 首页模板数据加载
@purchases_blue.route('/fiveone')
# @login_required
def fiveone():

    data = {
        'user_info':'黄德飞'
    }
    return render_template('fiveone.html',data=data)


@purchases_blue.route('/fivetwo')
# @login_required
def fivetwo():
    data = {
        'user_info':'黄德飞'
    }
    return render_template('fivetwo.html',data=data)

@purchases_blue.route('/fivethere')
# @login_required
def fivethere():
    data = {
        'user_info':'黄德飞'
    }
    return render_template('fivethere.html',data=data)

@purchases_blue.route('/fivefour')
# @login_required
def fivefour():
    data = {
        'user_info':'黄德飞'
    }
    return render_template('fivefour.html',data=data)

@purchases_blue.route('/fivefive')
# @login_required
def fivefive():
    data = {
        'user_info':'黄德飞'
    }
    return render_template('fivefive.html',data=data)