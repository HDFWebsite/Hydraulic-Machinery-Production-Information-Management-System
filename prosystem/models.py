# from flask_sqlalchemy import model
from datetime import datetime
from prosystem import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    """用户"""
    __tablename__ = "tb_user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 用户编号
    nick_name = db.Column(db.String(32), unique=True, nullable=False)  # 用户昵称
    password_hash = db.Column(db.String(128), nullable=False)  # 加密的密码
    mobile = db.Column(db.String(11), unique=True, nullable=False)  # 手机号
    is_admin = db.Column(db.Boolean, default=True)

    @property
    def password(self):
        raise AttributeError("当前属性不可读")

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        resp_dict = {
            "id": self.id,
            "nick_name": self.nick_name,
        }
        return resp_dict


class BomMain(db.Model):
    """BOM物料表"""
    __tablename__ = "tb_bommain"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    main_id = db.Column(db.Integer, unique=True)  # 主件品号
    main_name = db.Column(db.String(32), nullable=False)  # 主件品名
    unit = db.Column(db.String(8), nullable=False)  # 单位
    spec = db.Column(db.String(20), nullable=False)  # 货品规格
    cate = db.Column(db.String(16), nullable=False)  # 货品类别
    price = db.Column(db.Float, nullable=True)  # 单价
    date = db.Column(db.DateTime, default=datetime.now)  # 录入日期
    company = db.Column(db.String(20), nullable=True)  # 公司名称
    notes = db.Column(db.String(255))  # 是否有BOM结构

    def to_dict(self):
        resp_dict = {
            "id": self.id, # 编号
            "main_id": self.main_id,# 主件品号
            "main_name": self.main_name,# 主件品名
            "unit": self.unit if self.unit else "kg",# 单位
            "cate": self.cate if self.cate else "待定",# 货品类别
            "company": self.company if self.company else "未知", # 公司名称
            "spec": self.spec if self.spec else "BGS",# 货品规格
            "date":self.date,
            "price":self.price
        }
        return resp_dict

class BomSon(db.Model):
    """BOM关系表"""
    __tablename__ = "tb_bomson"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    main_id = db.Column(db.Integer)  # 主件品号
    main_name = db.Column(db.String(32), nullable=False)  # 主件品名
    son_id = db.Column(db.Integer)  # 子件品号
    son_name = db.Column(db.String(32), nullable=False)  # 子件品名
    num = db.Column(db.Integer, nullable=False)  # 子件组成量
    unit = db.Column(db.String(16), nullable=False)  # 子件单位

    def to_dict(self):
        resp_dict = {
            "id": self.id, # 编号
            "main_id": self.main_id,# 主件品号
            "main_name": self.main_name,# 主件品名 "
            "son_id": self.son_id,# 主件品号
            "son_name": self.son_name,# 主件品名
            "num": self.num if self.cate else 1,  # 货品类别
            "unit": self.unit if self.unit else "kg",# 单位
        }
        return resp_dict


class ProductionPlan(db.Model):
    """生产计划表"""
    __tablename__ = "tb_productionplan"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    plan_id = db.Column(db.Integer)  # 主件品号
    plan_name = db.Column(db.String(32), nullable=False)  # 主件品名
    unit = db.Column(db.String(16), nullable=False)  # 单位
    num = db.Column(db.Integer, nullable=False)  # 数量
    date = db.Column(db.DateTime, default=datetime.now)  # 录入日期
    is_need = db.Column(db.Boolean, default=False)  # 是否进行需求计算

    def to_dict(self):
        resp_dict = {
            "id": self.id, # 编号
            "main_id": self.plan_id,# 主件品号
            "main_name": self.plan_name,# 主件品名 "
            "unit": self.unit if self.unit else "kg",# 主件品号
            "num": self.num,# 主件品名
            "date": self.date,  # 货品类别
            "is_need": self.is_need ,# 单位
        }
        return resp_dict

class MaterialRequire(db.Model):
    """物料需求表"""
    __tablename__ = "tb_materialrequire"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    require_id = db.Column(db.Integer)  # 主件品号
    require_name = db.Column(db.String(32), nullable=False)  # 主件品名
    company = db.Column(db.String(16), nullable=True)  # 公司名称
    unit = db.Column(db.String(16), nullable=False)  # 单位
    num = db.Column(db.Integer, nullable=False)  # 数量
    build_time = db.Column(db.DateTime, default=datetime.now)  # 生成日期
    is_order = db.Column(db.Boolean, default=False)  # 是否下单
    order_time = db.Column(db.DateTime, default=datetime.now)  # 下单日期
    is_get = db.Column(db.Boolean, default=False)  # 是否到货
    get_time = db.Column(db.DateTime, default=datetime.now)  # 到货日期


class FinishedProduct(db.Model):
    """已生产产成品"""
    __tablename__ = "tb_finishedproduct"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    finished_id = db.Column(db.Integer)  # 产成品品号
    finished_name = db.Column(db.String(32), nullable=False)  # 产成品品名
    date = db.Column(db.DateTime, default=datetime.now)  # 录入日期
    num = db.Column(db.Integer, nullable=False)  # 数量
    unit = db.Column(db.String(16), nullable=False)  # 单位
    cal_date = db.Column(db.DateTime, default=datetime.now)  # BOM计算日期
    sign = db.Column(db.String(255))  # 计算标志
    raw_cost = db.Column(db.Float, nullable=True)  # 汇总原材料费用
    aux_cost = db.Column(db.Float, nullable=True)  # 汇总辅助材料费
    sem_cost = db.Column(db.Float, nullable=True)  # 汇总半成品费用
    unit_cost = db.Column(db.Float, nullable=True)  # 单位成本
    total_cost = db.Column(db.Float, nullable=True)  # 总费用


class MaterialCost(db.Model):
    """由产成品算出的各种原材料、辅助材料信息"""
    __tablename__ = "tb_materialcost"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    finished_id = db.Column(db.Integer)  # 产成品品号
    finished_name = db.Column(db.String(32), nullable=False)  # 产成品品名
    num = db.Column(db.Integer, nullable=False)  # 数量
    unit = db.Column(db.String(16), nullable=False)  # 单位
    son_id = db.Column(db.Integer)  # 子件编号
    son_name = db.Column(db.String(32), nullable=False)  # 子件品名
    son_num = db.Column(db.Integer, nullable=False)  # 子件数量
    son_unit = db.Column(db.String(16), nullable=False)  # 子件单位
    unit_price = db.Column(db.Float, nullable=False)  # 单价
    total_price = db.Column(db.Float, nullable=True)  # 总价


class SemifinishedProduct(db.Model):
    """由产成品算出的已生产半成品"""
    __tablename__ = "tb_semifinishedproduct"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    finished_id = db.Column(db.Integer)  # 产成品品号
    finished_name = db.Column(db.String(32), nullable=False)  # 产成品品名
    son_id = db.Column(db.Integer)  # 子件半成品编号
    son_name = db.Column(db.String(32), nullable=False)  # 子件半成品品名
    son_num = db.Column(db.Integer, nullable=False)  # 子件半成品数量
    date = db.Column(db.DateTime, default=datetime.now)  # 录入日期
    unit = db.Column(db.String(16), nullable=False)  # 单位
    cal_date = db.Column(db.DateTime, default=datetime.now)  # BOM计算日期
    raw_cost = db.Column(db.Float, nullable=True)  # 汇总原材料费用
    aux_cost = db.Column(db.Float, nullable=True)  # 汇总辅助材料费
    unit_cost = db.Column(db.Float, nullable=True)  # 单位加工费用
    total_cost = db.Column(db.Float, nullable=True)  # 总费用


class SemifinishedCost(db.Model):
    """由已生产半成品算出的各种原材料、辅助材料信息"""
    __tablename__ = "tb_semifinishedcost"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    semi_id = db.Column(db.Integer)  # 半成品品号
    semi_name = db.Column(db.String(32), nullable=False)  # 半成品品名
    num = db.Column(db.Integer, nullable=False)  # 数量
    unit = db.Column(db.String(16), nullable=False)  # 单位
    son_id = db.Column(db.Integer)  # 子件编号
    son_name = db.Column(db.String(32), nullable=False)  # 子件品名
    son_num = db.Column(db.Integer, nullable=False)  # 子件数量
    son_unit = db.Column(db.String(16), nullable=False)  # 子件单位
    unit_price = db.Column(db.Float, nullable=False)  # 单价
    total_price = db.Column(db.Float, nullable=False)  # 总价
