from flask import render_template
from . import purchases_blue
# 首页模板数据加载
@purchases_blue.route('/fivesix')
# @login_required
def fivesix():

    data = {
        'user_info':'黄德飞'
    }
    return render_template('fivesix.html',data=data)


@purchases_blue.route('/fiveseven')
# @login_required
def fiveseven():

    data = {
        'user_info':'黄德飞'
    }
    return render_template('fiveseven.html',data=data)

@purchases_blue.route('/fiveeight')
# @login_required
def fiveeight():
    data = {
        'user_info':'黄德飞'
    }
    return render_template('fiveeight.html',data=data)

@purchases_blue.route('/fivenine')
# @login_required
def fivenine():
    data = {
        'user_info':'黄德飞'
    }
    return render_template('fivenine.html',data=data)

@purchases_blue.route('/fiveten')
# @login_required
def fiveten():
    data = {
        'user_info':'黄德飞'
    }
    return render_template('fiveten.html',data=data)