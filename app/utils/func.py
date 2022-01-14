# -*- coding:utf-8 -*-
__author__ = 'LangJin'
__date__ = "2022-1-13"
__doc__ = "接口接受的参数校验的类"
"""
# 1.创建解析器对象 
		parser = reqparse.RequestParser() 

		#2.利用解析器对象添加 需要验证的参数
		parser.add_argument('uname',type=str,help='用户名验证错误！',required=True,trim=True) 
		parser.add_argument('pwd', type=str, help='密码验证错误！',default="123456") 
		parser.add_argument('age',type=int,help='年龄验证错误！')
		parser.add_argument('gender',type=str,choices=['男','女','双性'])
		parser.add_argument('birthday',type=inputs.date,help='生日字段验证错误！')
		parser.add_argument('phone',type=inputs.regex(r'1[3578]\d{9}'))
		parser.add_argument('phomepage',type=inputs.url,help='个人中心链接验证错误！')

		#3.利用解析器对象进行验证
		args = parser.parse_args()
"""

"""
参数校验的方案
1、模仿flask自带的校验方式，自己实现一个校验方法类.https://blog.csdn.net/weixin_44733660/article/details/103996953
2、使用jsonschema,https://www.cnblogs.com/c-keke/p/14888876.html
3、使用marshmallow
4、https://blog.csdn.net/w178191520/article/details/85201722
"""
class RequestParser:
    def __init__(self,):
        pass

