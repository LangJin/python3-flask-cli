# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from . import authbp
from flask import request
from app.utils.dbfunc import MySQLDB as mysql


@authbp.route("/test",methods=["post"])
def regist():
    body = request.get_json()
    dbres = mysql().query("select * from t_user limit %s;",(1))
    return body
