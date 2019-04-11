from . import consumes_blue,input_func
from prosystem.utils.commons import login_required
from flask import g, render_template, request, session
# 首页模板数据加载
@consumes_blue.route('/twomaterialinput1')
@login_required
def twomaterialinput1():
    data =input_func.getbommain1(request)
    return data

@consumes_blue.route('/twomaterialinput1add',methods=["POST"])
@login_required
def twomaterialinput1add():
    data =input_func.addbomprice(request)
    return data

@consumes_blue.route('/twomaterialinput1del',methods=["POST"])
@login_required
def twomaterialinput1del():
    data =input_func.delbomprice(request)
    return data

@consumes_blue.route('/twomaterialinput2')
@login_required
def twomaterialinput2():
    data = input_func.getbommain2(request)
    return data

@consumes_blue.route('/twomaterialinput2add',methods=["POST"])
@login_required
def twomaterialinput2add():
    data =input_func.addbomprice(request)
    return data

@consumes_blue.route('/twomaterialinput2del',methods=["POST"])
@login_required
def twomaterialinput2del():
    data =input_func.delbomprice(request)
    return data

@consumes_blue.route('/twomaterialinput3')
@login_required
def twomaterialinput3():
    data = input_func.getbommain3(request)
    return data

@consumes_blue.route('/twomaterialinput3add',methods=["POST"])
@login_required
def twomaterialinput3add():
    data =input_func.addbomprice(request)
    return data

@consumes_blue.route('/twomaterialinput3del',methods=["POST"])
@login_required
def twomaterialinput3del():
    data =input_func.delbomprice(request)
    return data