from flask import render_template
from . import consumes_blue
# 首页模板数据加载
@consumes_blue.route('/twomaterialinput1')
# @login_required
def twomaterialinput1():
    data = {
        'user_info':'黄德飞'
    }
    return render_template('twomaterialinput1.html',data=data)


@consumes_blue.route('/twomaterialinput2')
# @login_required
def twomaterialinput2():

    data = {
        'user_info':'黄德飞'
    }
    return render_template('twomaterialinput2.html',data=data)

@consumes_blue.route('/twomaterialinput3')
# @login_required
def twomaterialinput3():
    data = {
        'user_info':'黄德飞'
    }
    return render_template('twomaterialinput3.html',data=data)
