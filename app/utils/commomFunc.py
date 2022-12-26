# -*- coding:utf-8 -*-
__author__ = 'LangJin'
__date__ = "2022-4-13"
__doc__ = "token校验方法"
from authlib.jose import jwt
import hashlib
import json
import time
import xmltodict
from config import flaskConfig



def create_token(userInfo):
    """
    @功能    :生成token
    @参数    :dict
    @返回值  :token
    @时间    :2022/04/28 16:08:36
    @作者    :浪晋
    @版本    :1.0
    """
    header = {'alg': 'HS256','typ': 'JWT'}
    key = flaskConfig.SECRET_KEY
    data = {"iat": time.time()}
    data.update(userInfo)
    try:
        token = jwt.encode(header=header, payload=data, key=key)
        return token.decode('utf-8')
    except Exception as e:
        # logger.error(e)
        return False


def verify_token(token):
    """
    @功能    :解析token
    @参数    :token
    @返回值  :userInfo
    @时间    :2022/04/28 16:11:49
    @作者    :浪晋
    @版本    :1.0
    """
    key = flaskConfig.SECRET_KEY
    try:
        userInfo = jwt.decode(token,key)
        return userInfo
    except Exception as e:
        # logger.error(e)
        return False


def xml_to_json(xml_str):
    """
    @功能    :xml格式转json格式
    @参数    :xml_str字符串
    @返回值  :json对象
    @时间    :2022/04/28 16:17:19
    @作者    :浪晋
    @版本    :1.0
    """
    try:
        xml_parse = xmltodict.parse(xml_str)
        json_str = json.dumps(xml_parse, indent=1)
        json_dict = json.loads(json_str)
        return json_dict
    except Exception as e:
        # logger.error(e)
        return False


def encry(k):
    """
    @功能    :字符串md5加密
    @参数    :k字符串
    @返回值  :md5加密后的字符串
    @时间    :2022/04/28 16:17:57
    @作者    :浪晋
    @版本    :1.0
    """
    try:
        if type(k) is not str:
            raise Exception("加密失败，参数不是字符串类型")
        m = hashlib.md5()
        m.update(k.encode('utf-8'))
        return m.hexdigest()
    except Exception as e:
        # logger.error(e)
        return False