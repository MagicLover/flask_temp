#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2019/8/28 0028 22:16
# @Author  : P.D
# @Site    : 
# @File    : config.py
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "!@#$%^&*()_+"
    EXCEPTIONAL_API_KEY = "exceptional_forty_character_unique_key"
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_ENABLED = True


class Development(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"


class Production(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost:3306/blog?charset=utf8"

