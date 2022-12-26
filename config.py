# -*- coding:utf-8 -*-
__author__ = 'LangJin'
__date__ = "2022-2-28"
__doc__ = "flask配置文件"


class Config:
    DEBUG = False
    JSON_AS_ASCII = False #json 中文支持
    BABEL_DEFAULT_LOCALE = 'zh'
    SECRET_KEY = "cd2e4fc86aa568e7d735a7c8235607ff"    # SESSION配置
    MAX_CONTENT_LENGTH = 20 * 1024 * 1024  # 2MB


class DevelopConfig(Config):
    DEBUG = True
    PORT = 3456
    MySQLConfig = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "db": "ljtestdb",
        'charset': 'utf8mb4'
    }
    REDISConfig = {
        "host": "127.0.0.01",
        "port": 6379,
        "password": "123456",
        "db": 0
    }


class ProductionConfig(Config):
    MySQLConfig = {
        "host": "mysql",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "db": "ljtest",
        'charset': 'utf8mb4'
    }
    REDISConfig = {
        "host": "redis",
        "port": 6379,
        "password": "123456",
        "db": 0
    }



config = {
    "DevelopConfig": DevelopConfig,
    "ProductionConfig": ProductionConfig
    }

flaskConfig = config.get("DevelopConfig")