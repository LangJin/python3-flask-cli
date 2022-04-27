# -*- coding:utf-8 -*-
__author__ = 'LangJin'
__date__ = "2022-1-13"
__doc__ = "请求参数校验方法"

import re


class Parse:
    """
    参数校验的类
    """
    def __init__(self):
        self.data = []
    def parseRule(self,**kw):
        """
        接收需要校验的参数\n
        value：参数\n
        valueName：参数的中文解释\n
        lenMax：字符串类型的长度最长限制\n
        lenMin：lenMax：字符串类型的长度最短限制\n
        valueType：参数类型，如int/str\n
        required:是否必填，True/Flase\n
        ranges:参数范围，如：(1,2)
        regexp:正则表达式
        """
        data = {
            "value":kw.get("value"),
            "valueName":kw.get("valueName"),
            "max":kw.get("lenMax"),
            "min":kw.get("lenMin"),
            "type":kw.get("valueType"),
            "required":kw.get("required"),
            "range":kw.get("ranges"),
            "regexp":kw.get("regexp")
        }
        self.data.append(data)
    def checkRule(self):
        data = self.data
        for i in data:
            value = i.get("value")
            valueName = i.get("valueName")
            lenMax = i.get("max")
            lenMin = i.get("min")
            valueType = i.get("type")
            required = i.get("required")
            ranges = i.get("range")
            regexp = i.get("regexp")
            if required == True:
                if value is None or value == "":
                    return "{}不能为空".format(valueName)
            if valueType is not None and value  not in (None,""):
                res = isinstance(value,eval(valueType))
                if res != True:
                    return "{}类型不正确".format(valueName)
            if lenMax is not None and value not in (None,""):
                if len(value) >= lenMax:
                    return "{}超出允许长度".format(valueName)
            if lenMin is not None and value not in (None,""):
                if len(value) < lenMin:
                    return "{}低于允许长度".format(valueName)
            if ranges is not None and value not in (None,""):
                if value not in ranges:
                    return "{}输入范围错误".format(valueName)
            if regexp is not None and value not in (None,""):
                result = re.match(regexp,str(value))
                if result == None:
                    return "{}不符合要求".format(valueName)
        return True

