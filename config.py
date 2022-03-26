# -*- coding:utf-8 -*-
'''
@Time    : 2022/3/26 23:31 
@Author  : Pcw
@File    : config.py
 '''
from redis import StrictRedis


class Config(object):
    DEBUG = False
    # mysql 配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@192.168.3.23:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis 配置信息
    REDIS_HOST = "192.168.3.23"
    REDIS_PORT = 6379

    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    ...
    # flask_session的配置信息
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_PERMANENT = False  # 如果设置为True，则关闭浏览器session就失效。
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)  # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 86400  # session 的有效期，单位是秒


# dev
class Developement(Config):
    DEBUG = True


# prod
class Production(Config):
    DEBUG = False


config = {
    "dev": Developement,
    "Production": Production,
    "uat": None
}

if __name__ == '__main__':
    pass
