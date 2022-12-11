# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from . import demobp
from flask import g,request
from app.utils.responseFunc import resultMsg




@demobp.route("/test", methods=["get"])
def test():
    return resultMsg(code=1,msg="success",data=g.userInfo)