# 自定义过滤器
from flask import session, current_app, g
from flask import redirect, url_for
from prosystem.models import User

# 让被装饰的函数的属性不发生变化
import functools


# 登录验证装饰器
# 装饰器:函数嵌套，闭包，作用：在不改变原有代码的情况下，添加新的功能。
def login_required(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        # 尝试从redis缓存中获取用户id
        user_id = session.get('user_id')
        user = None
        # 判断获取结果
        if user_id:
            # 根据user_id，查询mysql获取用户信息
            try:
                user = User.query.get(user_id)
            except Exception as e:
                current_app.logger.error(e)
        # 把查询结果传给被装饰的视图函数,在请求过程中用来临时存储数据
        if not user:
            return redirect(url_for('other_blue.login'))
        return f(*args, **kwargs)

    # wrapper.__name__ = f.__name__
    return wrapper
