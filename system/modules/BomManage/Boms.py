from flask import render_template
from . import boms_blue
# 首页模板数据加载
@boms_blue.route('/')
# @login_required
def index():

    data = {
        'user_info':'黄德飞'
    }
    return render_template('index.html',data=data)


@boms_blue.route('/onebaseinfo')
# @login_required
def onebaseinfo():

    data = {
        'user_info':'黄德飞'
    }
    return render_template('onebaseinfo.html',data=data)

@boms_blue.route('/onebaseinput')
# @login_required
def onebaseinput():
    data = {
        'user_info':'黄德飞'
    }
    return render_template('onebaseinput.html',data=data)

@boms_blue.route('/onebasemanage')
# @login_required
def onebasemanage():
    data = {
        'user_info':'黄德飞'
    }
    return render_template('onebasemanage.html',data=data)