from distutils.command.config import config


class Config:
    DEBUG = False
    MAX_CONTENT_LENGTH = 20 * 1024 * 1024  # 2MB
    MYSQL_HOST = "127.0.0.1"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PASSWORD = "123456"
    MYSQL_DB_NAME = "ljtest"
    REDIS_HOST = ""
    REDIS_PORT = ""
    REDIS_PASSWORD = ""

class DevelopConfig(config):
    DEBUG = True


class ProductionConfig(config):
    pass


config = {
    "DevelopConfig": DevelopConfig,
    "ProductionConfig": ProductionConfig
    }