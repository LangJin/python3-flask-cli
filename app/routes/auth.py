# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from . import authbp
from app.utils.dbfunc import MySQLDB as mysql


@authbp.route("/regist",methods=["POST","GET"])
def regist():
    return {}
