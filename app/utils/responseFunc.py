# -*- coding:utf-8 -*-
__author__ = 'LangJin'
__date__ = "2022-1-13"
__doc__ = "响应结果处理"



def resultMsg(code=1,msg="操作成功",data=None):
    """
    @功能    :操作类型的接口的返回结果的封装
    @参数    :
    @返回值  :
    @时间    :2022/04/28 16:21:16
    @作者    :浪晋
    @版本    :1.0
    """
    
    if data == None:
        result = {"code":code,"message":msg}
    else:
        result = {"code":code,"message":msg,"data":data}
    return result

