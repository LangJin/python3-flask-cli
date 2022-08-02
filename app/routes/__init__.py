# -*- coding:utf-8 -*-
__author__ = 'LangJin'
__date__ = "2022-2-28"
__doc__ = "蓝图定义和钩子"

import json
from flask import Blueprint,request,g
from app.utils.commomFunc import verify_token
from app.utils.redisFunc import RedisDb as redis
from app.utils.responseFunc import resultMsg


authbp = Blueprint("demo", __name__,url_prefix="/demo")
userbp = Blueprint("user", __name__,url_prefix="/user")


@userbp.before_request
def before_request():
    token = request.headers.get("token")
    if token in (None,""):
        return resultMsg(code=0,msg="用户未登录")
    userInfo = verify_token(token)
    if userInfo == False:
        return resultMsg(code=0,msg="token不合法，请输入正确token")
    username = userInfo.get("username")
    redisRes = redis().get_value(username)
    if redisRes is None:
        return resultMsg(code=0,msg="token已过期，请重新登录")
    redisRes = json.loads(redisRes)
    if redisRes.pop("token") == token:
        g.userInfo = redisRes
    else:
        return resultMsg(code=0,msg="token已过期，请重新登录")
