# -*- coding:utf-8 -*-
'''
@Time    : 2022/3/24 20:18 
@Author  : Pcw
@File    : manage.py
 '''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
import redis
"""
1、初始化
2、抽取配置文件在config类
3、数据库
4、
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


    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    ...
    # flask_session的配置信息
    SESSION_TYPE = "redis" # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True # 让 cookie 中的 session_id 被加密签名处理
    SESSION_PERMANENT = False  # 如果设置为True，则关闭浏览器session就失效。
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT) # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 86400 # session 的有效期，单位是秒



app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
CSRFProtect(app)
Session(app)


@app.route("/")
def index():
    return "test"


if __name__ == '__main__':
    app.run(host="192.168.3.109")
