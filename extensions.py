#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 0029 20:32
# @Author  : P.D
# @Site    : 
# @File    : extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension


db = SQLAlchemy()
migrate = Migrate(db)
toolbar = DebugToolbarExtension()





