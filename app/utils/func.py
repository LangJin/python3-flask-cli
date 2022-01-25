# -*- coding:utf-8 -*-
__author__ = 'LangJin'
__date__ = "2022-1-13"
__doc__ = "这是框架所用到的一些公共的方法"



def resultMsg(code=200,msg="操作成功",data={}):
    """
    操作类型的接口的返回结果的封装
    """
    res = {"code":code,"message":msg,"data":data}
    return res


def queryData(code=200,msg="操作成功",**kw):
    """
    查询类型的接口的返回结果的封装
    code:状态码，默认200
    msg:返回提示
    rows:查询的数据
    total:数据数量，默认0
    page:页码，默认1
    pageSize:一页多少条数据，默认20
    summary：默认{}
    """
    rows = kw.get("rows")
    total = kw.get("total")
    page = kw.get("page")
    pageSize = kw.get("pageSize")
    summary = kw.get("summary")
    if type(rows) != list:
        return resultMsg(403,"rows数据格式不正确")
    if total != None:
        total = total[0].get("count")
    else:
        total = 0
    if page == None:
        page = 1
    if pageSize == None:
        pageSize = 20
    if summary == None:
        summary = {}
    data = {
            "rows":rows,
            "total":total,
            "page":page,
            "pageSize":pageSize,
            "summary":summary
            }
    res = {"code":code,"message":msg,"data":data}
    return res



class Parse:
    """
    参数校验的类
    """
    def __init__(self):
        self.data = []
    def parseRule(self,**kw):
        """
        接收需要校验的参数
        value,valueName,lenMax,lenMin,valueType,required
        """
        data = {
            "value":kw.get("value"),
            "valueName":kw.get("valueName"),
            "max":kw.get("lenMax"),
            "min":kw.get("lenMin"),
            "type":kw.get("valueType"),
            "required":kw.get("required")
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
            if required == True:
                if value is None:
                    return resultMsg(401,"{}参数不能为空".format(valueName))
            if valueType is not None:
                res = isinstance(value,eval(valueType))
                if res != True:
                    return resultMsg(401,"{}参数类型不正确".format(valueName))
            if lenMax is not None:
                if len(value) >= lenMax:
                    return resultMsg(401,"{}参数超出允许长度".format(valueName))
            if lenMin is not None:
                if len(value) <= lenMin:
                    return resultMsg(401,"{}参数低于允许长度".format(valueName))
            
        return True
