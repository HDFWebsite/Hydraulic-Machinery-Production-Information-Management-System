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