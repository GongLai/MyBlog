# -*- coding: utf-8 -*-
# 配置文件


class Config(object):
    # CSRF被激活时，用于令牌加密，表单验证
    SECRET_KEY = 'yunjx*&svo6f%%#e20s5v6%vsedc2#7'
    # 格式为mysql+pymysql://数据库用户名:密码@数据库地址:端口号/数据库的名字?数据库格式
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Hjq131415600@localhost:3306/CS_flaskblog?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
