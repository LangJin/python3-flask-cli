# -*- coding:utf-8 -*-
__author__ = 'liuyun'
__date__ = "2022-2-28"
__doc__ = "数据库连接池和redis连接池的实现"
import pymysql
from logger import logs as logger
from dbutils.pooled_db import PooledDB
from config import flaskConfig



pool = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=1000,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=0,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=1000,  # 链接池中最多闲置的链接，0和None不限制
    maxshared=1000,  # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。
    # 如：0 = None = never,
    # 1 = default = whenever it is requested,
    # 2 = when a cursor is created,
    # 4 = when a query is executed,
    # 7 = always
    **flaskConfig.MySQLConfig
)


class MySQLDB:
    '''
        数据的工具类
    '''
    def __init__(self):
        self.conn = pool.connection()
        self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)


    def close_conn(self):
        """
        断开数据库连接
        """
        self.cursor.close()
        self.conn.close()

    def query(self,sql='',kwargs=()):
        '''
            用法：query('select * from t_user;')\n
            说明：查询数据库工具,返回查询结果
        '''
        try:
            self.cursor.execute(sql,kwargs)  # 执行sql语句
            results = self.cursor.fetchall()
        except Exception as e:
            logger.error(e)
            results = False
        finally:
            self.close_conn()
            return results


    def commit(self,sql="",kwargs=()):
        '''
            用法：commit('insert into t_user (id,username) values (1,'张三');')\n
            说明：更改数据库工具，支持插入、修改、删除
        '''
        try:
            self.cursor.execute(sql,kwargs)
            self.conn.commit()
            results = True
        except Exception as e:
            logger.error(e)
            results = False
            self.conn.rollback()
        finally:
            self.close_conn()
            return results
