# -*- coding:utf-8 -*-
'''
@Time    : 2022/3/27 0:14 
@Author  : Pcw
@File    : __init__.py.py
 '''

from flask import Blueprint

index_blu = Blueprint('index', __name__)

from .view import *


if __name__ == '__main__':
    pass
