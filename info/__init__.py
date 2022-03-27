# -*- coding:utf-8 -*-
'''
@Time    : 2022/3/26 23:40 
@Author  : Pcw
@File    : __init__.py.py
 '''
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis

from config import config
from info.module import index_blu
import logging
from logging.handlers import RotatingFileHandler

# 初始化sqlalchemy
db = SQLAlchemy()


def create_log():
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


def create_app(config_name):
    create_log()
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    db.init_app(app)
    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    CSRFProtect(app)
    Session(app)

    # 添加蓝图后的路由
    app.register_blueprint(index_blu)

    return app


if __name__ == '__main__':
    pass
