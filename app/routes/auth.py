# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Blueprint
from flask import request
from app.utils import tools
from config import Config

authbp = Blueprint("user", __name__,url_prefix="/auth")

config = Config()

dbconfig = {
    "host":config.MYSQL_HOST,
    "port":config.MYSQL_PORT,
    "user":config.MYSQL_USER,
    "password":config.MYSQL_PASSWORD,
    "db":config.MYSQL_DB_NAME
}
db = tools.Db(dbconfig)


@authbp.route("/login",methods=["post"])
def login():
    body = request.get_json()
    username = body.get("username")
    password = body.get("password")
    dbres =  db.query("select * from t_system_user where username = '{}';".format(username))
    if len(dbres) == 1:
        if password == dbres[0].get("password"):
            return {"code":1,"msg":"登录成功！","data":{"token":"sdkjfsedkjfsel;kfsekjfwsek;jfwsekfj","userInfo":{
                "userId": "1",
                "userName": "Administrator",
                "dashboard": "0",
                "role": [
                    "SA",
                    "admin",
                    "Auditor"
                ]
            }}}
        else:
            return {"code":0,"msg":"密码错误！"}
    else:
        return {"code":0,"msg":"账号不存在"}


@authbp.route("/regist")
def regist():
    return {},400