# -*- coding:utf-8 -*-
'''
@Time    : 2022/3/24 20:18 
@Author  : Pcw
@File    : manage.py
 '''

from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from redis import StrictRedis
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from config import Config
from info import app,db

"""
1、初始化
2、抽取配置文件在config类
3、数据库
4、redis
5、添加csrf
6、添加session存储在redis中
7、添加命令行管理manage
8、数据库迁移
9、拆分Config
10、加载内容
11、把路由变成蓝图
"""


manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0', port=8080))
Migrate(app, db)
manager.add_command('db', MigrateCommand)


@app.route("/")
def index():
    # 存取session
    session["name"] = 'test_session'
    # 获取session  登录redis可以keys * 可以看到session的key
    print(session["name"])
    return "test"


if __name__ == '__main__':
    manager.run()
