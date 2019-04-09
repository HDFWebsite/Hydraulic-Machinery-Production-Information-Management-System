from . import other_blue
from prosystem import db
from prosystem.models import User
from prosystem.utils.response_code import RET
from prosystem.utils.commons import login_required
from flask import g, render_template, request, session
from flask import redirect, url_for, jsonify, current_app, abort


def clear_session():
    """清除浏览器缓存"""
    session.pop('user_id', None)
    session.pop('nick_name', None)


# 登录
@other_blue.route('/login', methods=["GET", "POST"])
def login():
    """登录接口"""
    if request.method == "GET":
        # 已登录直接显示主页
        user_id = session.get('user_id', None)
        if user_id:
            return redirect(url_for('other_blue.index'))
        return render_template('other/login.html')
        # 取到登录的参数
    username = request.form.get("username")
    password = request.form.get("password")
    if not all([username, password]):
        return render_template('other/login.html', errmsg="参数不足")
    try:
        user = User.query.filter(User.nick_name == username).first()
    except Exception as e:
        current_app.logger.error(e)
        return render_template('other/login.html', errmsg="数据查询失败")

    if not user:
        return render_template('other/login.html', errmsg="用户不存在")

    if not user.check_password(password):
        return render_template('other/login.html', errmsg="密码错误")
    session["user_id"] = user.id
    session["nick_name"] = user.nick_name
    return redirect(url_for('other_blue.index'))


# 首页模板数据加载
@other_blue.route('/')
@login_required
def null():
    return redirect(url_for('other_blue.index'))


# 首页模板数据加载
@other_blue.route('/index')
@login_required
def index():
    """后台管理首页"""
    user_id = session.get('user_id', None)
    nick_name = session.get('nick_name', None)
    resp_dict = {
        "user": {
            "id": user_id,
            'nick_name': nick_name
        }
    }
    return render_template('other/index.html', resp_dict=resp_dict)


@other_blue.route('/main')
@login_required
def main():
    return render_template('other/main.html')


@other_blue.route('/favicon.ico')
@login_required
def favicon():
    """实现/favicon.ico路径下的图标加载
      使用current_app调用flask内置的函数，发送静态文件给浏览器，实现logo图标的加载
    """
    return current_app.send_static_file('/static/images/favicon.ico')


# 退出登录
@other_blue.route('/logout')
@login_required
def logout():
    """退出登录,本质是清除用户在服务器缓存的用户信息"""
    clear_session()
    return jsonify(errno=RET.OK, errmsg='OK')


# 注销
@other_blue.route('/logoff')
def logoff():
    """注销账号"""
    try:
        user = User.query.get(session.get('user_id'))
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg='注销账号失败')
    # 清除缓存
    clear_session()
    return redirect(url_for('other_blue.login'))
