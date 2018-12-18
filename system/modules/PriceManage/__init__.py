from flask import Blueprint


# 创建新闻模块的蓝图对象

price_blue = Blueprint('price_blue',__name__)

# 把使用蓝图对象的文件，导入到创建蓝图对象的下面
from . import price
