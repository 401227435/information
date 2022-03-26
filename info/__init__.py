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

from information.config import config


db = None

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    db = SQLAlchemy(app)
    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    CSRFProtect(app)
    Session(app)

    return app


if __name__ == '__main__':
    pass
