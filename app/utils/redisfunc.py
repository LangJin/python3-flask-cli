# -*- coding:utf-8 -*-
__author__ = '浪晋'
__date__ = "2022-2-28"
__doc__ = "数据库连接池和redis连接池的实现"
import json
from redis import StrictRedis
from config import flaskConfig


class RedisDb:
    '''
        Redis的工具类
    '''
    def __init__(self):
        self.db_config = flaskConfig.REDISConfig
        self.redis = StrictRedis(**self.db_config, max_connections=2000)
        
    def set_value(self,k,value, ex=24*60*60):
        '''
            设置用户缓存
        '''
        if type(value) is dict:
            value = json.dumps(value)
        try:
            results = self.redis.set(k, value, ex)  # 返回True
        except Exception as e:
            # logger.error(e)
            results = False
        finally:
            return results
    

    def del_value(self,k):
        '''
            清空用户缓存
        '''
        try:
            results = self.redis.delete(k)  # 返回1
        except Exception as e:
            # logger.error(e)
            results = False
        finally:
            self.redis.close()
            return results
    

    def get_value(self, k):
        try:
            results = self.redis.get(k)
            results = results if results is None else str(results, encoding='utf-8')
        except Exception as e:
            # logger.error(e)
            results = False
        finally:
            return results
