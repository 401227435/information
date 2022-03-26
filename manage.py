# -*- coding:utf-8 -*-
'''
@Time    : 2022/3/24 20:18 
@Author  : Pcw
@File    : manage.py
 '''

from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from redis import StrictRedis
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
"""
1、初始化
2、抽取配置文件在config类
3、数据库
4、redis
5、添加csrf
6、添加session存储在redis中
7、添加命令行管理manage
8、数据库迁移
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
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT) # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 86400 # session 的有效期，单位是秒



app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
CSRFProtect(app)
Session(app)
manager=Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)



@app.route("/")
def index():
    # 存取session
    session["name"]='test_session'
    # 获取session  登录redis可以keys * 可以看到session的key
    print(session["name"])
    return "test"


if __name__ == '__main__':
    manager.run()
