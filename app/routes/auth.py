# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Blueprint,request,g
from app.utils.dbFunc import MySQLDB as mysql
from app.utils.redisFunc import RedisDb as redis
from app.utils.responseFunc import resultMsg
from app.utils.requetParse import Parse
from app.utils.commomFunc import create_token


authbp = Blueprint("demo", __name__,url_prefix="/demo")


@authbp.route('/regist', methods=['POST'])
def regist():
    """
    注册账号
    """
    body = request.get_json()
    username = body.get('username')
    password = body.get('password')
    parse = Parse()
    parse.parseRule(value=username,valueName="用户名",valueRule="用户名长度为4-16位",required=True,regexp="^[a-zA-Z0-9]{4,16}$")
    parse.parseRule(value=password,valueName="密码",valueRule="密码长度为6-16位",required=True,regexp="^[a-zA-Z0-9]{6,16}$")
    result = parse.checkRule()
    if result != True:
        return resultMsg(code=0,msg=result)
    sql = "select * from t_user where username = '{}'".format(username)
    dbres = mysql().query(sql)
    if dbres:
        return resultMsg(code=0,msg="用户名已存在")
    return resultMsg(code=1,msg="注册成功",data=dbres)


@authbp.route('/login', methods=['POST'])
def login():
    """
    登录账号
    """
    body = request.get_json()
    username = body.get('username')
    password = body.get('password')
    parse = Parse()
    parse.parseRule(value=username,valueName="用户名",valueRule="用户名长度为4-16位",required=True,regexp="^[a-zA-Z0-9]{4,16}$")
    parse.parseRule(value=password,valueName="密码",valueRule="密码长度为6-16位",required=True,regexp="^[a-zA-Z0-9]{6,16}$")
    result = parse.checkRule()
    if result != True:
        return resultMsg(code=0,msg=result)
    sql = "select * from t_user where username = '{}' and password = '{}'".format(username,password)
    dbres = mysql().query(sql)
    # if dbres:
    userInfo = {"username":username}
    token = create_token(userInfo)
    userInfo.update(token=token)
    if redis().set_value(username,userInfo):
        return resultMsg(code=1,msg="登录成功",data=userInfo)
    else:
        return resultMsg(code=0,msg="用户名或密码错误",data=dbres)