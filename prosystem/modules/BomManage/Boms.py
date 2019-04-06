from . import boms_blue,info_func,input_func,manage_func,other_func
from sqlalchemy import or_,and_
from prosystem.models import User,BomMain,BomSon
from prosystem.utils.commons import login_required
from prosystem.utils.response_code import RET
from flask import g, render_template, request, session
from flask import redirect, url_for, jsonify, current_app, abort

@boms_blue.route('/onebaseinfo')
@login_required
def onebaseinfo():

    data = info_func.getbommain(request)
    # 返回数据
    return data

@boms_blue.route('/onebaseinfoadd', methods=["POST"])
@login_required
def onebaseinfoadd():

    data = info_func.addbommain(request)
    # 返回数据
    return data

@boms_blue.route('/onebaseinfodel')
@login_required
def onebaseinfodel():

    data = info_func.delbommain(request)
    # 返回数据
    return data

@boms_blue.route('/onebaseinput')
@login_required
def onebaseinput():
    data = input_func.getbommain(request)
    # 返回数据
    return data

@boms_blue.route('/onebaseinputquery', methods=["POST"])
@login_required
def onebaseinputquery():
    data = input_func.getbommainquery(request)
    print(data.data)
    # 返回数据
    return data

@boms_blue.route('/onebaseinputadd', methods=["POST"])
@login_required
def onebaseinputadd():

    data = input_func.addbommain(request)
    # 返回数据
    return data
@boms_blue.route('/onebasemanage')
@login_required
def onebasemanage():
    data = manage_func.getbommain(request)
    return data

@boms_blue.route('/onebasemanagedel')
@login_required
def onebasemanagedel():
    main_id = request.args.get('main_id', "")
    data = manage_func.delete_bom_rel(main_id)
    return data