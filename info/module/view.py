# -*- coding:utf-8 -*-
'''
@Time    : 2022/3/27 0:17 
@Author  : Pcw
@File    : view.py
 '''
from . import index_blu


@index_blu.route("/")
def index():
    # 存取session
    # session["name"] = 'test_session'
    # 获取session  登录redis可以keys * 可以看到session的key
    # print(session["name"])
    return "index_blu"


if __name__ == '__main__':
    pass
