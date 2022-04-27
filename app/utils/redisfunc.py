# -*- coding:utf-8 -*-
__author__ = 'liuyun'
__date__ = "2022-2-28"
__doc__ = "数据库连接池和redis连接池的实现"
import json
from redis import StrictRedis
from config import REDIS_CONFIG

class RedisDb:
    '''
        Redis的工具类
    '''
    def __init__(self):
        self.db_config = REDIS_CONFIG
        self.redis = StrictRedis(**self.db_config, max_connections=2000)
        
    def setredisvalue(self,k,value, ex=60*60*30):
        '''
            设置用户缓存，并返回结果
        '''
        if type(value) is dict:
            value = json.dumps(value)
        try:
            res = self.redis.set(k, value, ex)  # 返回True
        except Exception as e:
            res = '{}'.format(e)
        finally:
            return res
    
    def getredisvalue(self,k):
        '''
            根据token读取用户缓存
        '''
        try:
            res = self.redis.get(k)  # 返回json对象
            res = res if res is None else str(res, encoding='utf-8')
        except Exception as e:
            res = '{}'.format(e)
        finally:
            self.redis.close()
            return res

    def delredisvalue(self,k):
        '''
            清空用户缓存
        '''
        try:
            res = self.redis.delete(k)  # 返回1
        except Exception as e:
            res = '{}'.format(e)
        finally:
            self.redis.close()
            return res
    
    def get_redis(self, k):
        try:
            res = self.redis.get(k)
            res = res if res is None else str(res, encoding='utf-8')
        except Exception as e:
            res = '{}'.format(e)
        finally:
            return res


if __name__ == "__main__":
    # db = MySQLDB()
    # a = db.query("select * from tb_user where id='liuyun1'")
    # print(a)
    
    # mysqldb = MySQLDB()
    redisdb = RedisDb()
    a = redisdb.getredisvalue('123')
    print(a)
    
