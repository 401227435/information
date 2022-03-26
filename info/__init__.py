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

app = Flask(__name__)

app.config.from_object(config['dev'])
db = SQLAlchemy(app)
redis_store = StrictRedis(host=config['dev'].REDIS_HOST, port=config['dev'].REDIS_PORT)
CSRFProtect(app)
Session(app)

if __name__ == '__main__':
    pass
