# -*- coding:utf-8 -*-
'''
@Time    : 2022/3/24 20:18 
@Author  : Pcw
@File    : manage.py
 '''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
"""
1、初始化
2、抽取配置文件在config类
3、
"""

app = Flask(__name__)


class Config(object):
    DEBUG = True
    # mysql 配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@192.168.3.23:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis 配置信息
    REDIS_HOST = "192.168.3.23"
    REDIS_PORT = 6379


app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)


@app.route("/")
def index():
    return "test"


if __name__ == '__main__':
    app.run(host="192.168.3.109")
