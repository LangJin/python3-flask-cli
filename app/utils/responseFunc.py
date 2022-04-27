# -*- coding:utf-8 -*-
__author__ = 'LangJin'
__date__ = "2022-1-13"
__doc__ = "响应结果处理"



def resultMsg(code=200,msg="操作成功",data={}):
    """
    操作类型的接口的返回结果的封装
    """
    res = {"code":code,"message":msg,"data":data}
    return res

