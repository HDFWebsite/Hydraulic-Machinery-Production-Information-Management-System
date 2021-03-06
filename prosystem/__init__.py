import logging
from flask import Flask, g,render_template
from flask_login import current_user
# 导入Config类，导入config_dict字典
from config import Config, config_dict
# 导入flask_session扩展包，用来指定session信息存储的位置
from flask_session import Session
# 导入flask_sqlalchemy扩展，实现数据库的连接
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler

# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)  # 调试debug级
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
# 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器
logging.getLogger().addHandler(file_log_handler)
# 实例化redis对象
from redis import StrictRedis

redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT, decode_responses=True)

# 先实例化sqlalchemy对象
db = SQLAlchemy()

# 导入flask_wtf扩展提供的csrf保护功能
from flask_wtf import CSRFProtect, csrf


# 定义工厂函数，让函数根据参数的不同，生产不同环境下的app，即开发模式下的app，或生产模式下的app
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])
    # 让sqlalchemy对象通过函数调用，实现和程序实例app进行关联
    db.init_app(app)
    Session(app)
    # 后端服务器开启csrf保护,不仅会验证请求方法POST/PUT/DELETE/PATCH/，
    # 还会验证请求头中是否设置了X-CSRFToken
    CSRFProtect(app)

    @app.before_request
    def before_request():
        g.user = current_user

    @app.after_request
    def after_request(response):
        # 生成csrf_token
        csrf_token = csrf.generate_csrf()
        # 把csrf_token设置到客户端浏览器的cookie中
        response.set_cookie('csrf_token', csrf_token)
        return response

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('other/errorHtml.html'), 404

    # # 导入蓝图对象，注册蓝图对象
    from prosystem.modules.OtherBlue import other_blue
    app.register_blueprint(other_blue)
    from prosystem.modules.BomManage import boms_blue
    app.register_blueprint(boms_blue)
    from prosystem.modules.ConsumeManage import consumes_blue
    app.register_blueprint(consumes_blue)
    from prosystem.modules.InformationService import infos_blue
    app.register_blueprint(infos_blue)
    from prosystem.modules.PriceManage import price_blue
    app.register_blueprint(price_blue)
    from prosystem.modules.PurchaseManage import purchases_blue
    app.register_blueprint(purchases_blue)
    from prosystem.modules.CostManage import cost_blue
    app.register_blueprint(cost_blue)

    return app
