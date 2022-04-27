# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from . import authbp
from flask import request
from app.utils.dbfunc import MySQLDB as mysql
from app.utils.responseFunc import resultMsg

@authbp.route("/test",methods=["get"])
def regist():
    dbres = mysql().query("selet * from t_user limit %s;",(1))
    return resultMsg(data=dbres)
