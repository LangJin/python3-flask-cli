# -*- coding:utf-8 -*-
__author__ = 'LangJin'
__date__ = "2022-1-13"
__doc__ = "请求参数校验方法"

import re


class Parse:
    """
    @功能    :正则表达式参数校验
    @参数    :kwargs
    @返回值  :True
    @时间    :2022/04/28 18:29:08
    @作者    :浪晋
    @版本    :1.0
    """
    
    def __init__(self):
        self.data = []
    def parseRule(self,**kwargs):
        """
        接收需要校验的参数\n
        value：参数\n
        valueName：参数的中文解释\n
        valueRule:参数的校验规则说明\n
        required:是否必填，True/Flase\n
        regexp:正则表达式
        """
        data = {
            "value":kwargs.get("value"),
            "valueName":kwargs.get("valueName"),
            "valueRule":kwargs.get("valueRule"),
            "required":kwargs.get("required"),
            "regexp":kwargs.get("regexp")
        }
        self.data.append(data)


    def checkRule(self):
        """
        检查参数是否符合正则表达式规则
        """
        data = self.data
        for i in data:
            value = i.get("value")
            valueName = i.get("valueName")
            valueRule = i.get("valueRule")
            required = i.get("required")
            regexp = i.get("regexp")
            if required == True:
                if value in (None,""):
                    return "{}不能为空".format(valueName)
            if regexp  not in (None,""):
                result = re.match(regexp,str(value))
                if result == None:
                    return "{}要求{}".format(valueName,valueRule)
        return True

