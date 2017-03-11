# -*- coding:utf-8 -*-
from flask import Flask
#简单地创建应用对象
app = Flask(__name__)
app.config.from_object('config')

from app import views