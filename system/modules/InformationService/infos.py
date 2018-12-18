from flask import render_template
from . import infos_blue
# 首页模板数据加载
@infos_blue.route('/thereproplaninput')
# @login_required
def thereproplaninput():

    data = {
        'user_info':'黄德飞'
    }
    return render_template('thereproplaninput.html',data=data)


@infos_blue.route('/theremareqcalculation')
# @login_required
def theremareqcalculation():

    data = {
        'user_info':'黄德飞'
    }
    return render_template('theremareqcalculation.html',data=data)

@infos_blue.route('/therepurchaseorderget')
# @login_required
def therepurchaseorderget():
    data = {
        'user_info':'黄德飞'
    }
    return render_template('therepurchaseorderget.html',data=data)

@infos_blue.route('/thereproarrivalmanage')
# @login_required
def thereproarrivalmanage():
    data = {
        'user_info':'黄德飞'
    }
    return render_template('thereproarrivalmanage.html',data=data)