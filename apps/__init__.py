#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 0015 20:30
# @Author  : P.D
# @Site    : 
# @File    : __init__.py.py
import os
from flask import Flask, render_template
from config import Config
from extensions import db, migrate, toolbar
from blog.views import blue

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def create_app():
    app = Flask(__name__, static_folder=BASE_DIR + "/static", template_folder=BASE_DIR + "/templates")
    app.config.from_object(Config)
    register_extensions(app)
    register_blueprint(app)
    register_errors(app)
    return app


def register_extensions(app):
    """注册扩展"""
    db.init_app(app)
    migrate.init_app(app, db)
    toolbar.init_app(app)


def register_blueprint(app):
    """注册蓝图"""
    app.register_blueprint(blue)


def register_errors(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("error/404.html"), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('error/500.html'), 500
