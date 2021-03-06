# -*- coding:utf-8 -*-
'''
@Time    : 2022/3/24 20:18 
@Author  : Pcw
@File    : manage.py
 '''

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from info import create_app, db,models
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
12、添加日志
13、数据模型的创建和数据迁移
"""

app = create_app("dev")

manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0', port=8080))
Migrate(app, db)
manager.add_command('db', MigrateCommand)

""" 数据模型初始化和迁移
    python manage.py db init
    python manage.py db migrate -m"initial"
    python manage.py db upgrade
"""
if __name__ == '__main__':
    manager.run()
