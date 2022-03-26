# -*- coding:utf-8 -*-
'''
@Time    : 2022/3/27 0:17 
@Author  : Pcw
@File    : view.py
 '''
from . import index_blu
import logging

@index_blu.route("/")
def index():
    # 存取session
    # session["name"] = 'test_session'
    # 获取session  登录redis可以keys * 可以看到session的key
    # print(session["name"])
    logging.debug("This is a debug log.")
    logging.info("This is a info log.")
    logging.warning("This is a warning log.")
    logging.error("This is a error log.")
    logging.critical("This is a critical log.")
    return "index_blu"


if __name__ == '__main__':
    pass
