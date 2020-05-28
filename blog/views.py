#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2019/11/15 0015 21:06
# @Author  : P.D
# @Site    : 
# @File    : views.py
from flask import Blueprint, render_template

blue = Blueprint("blue", __name__)


@blue.route("/")
def index():
    return render_template("index.html")



