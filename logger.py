# -*- coding:utf-8 -*-
__author__ = 'LangJin'
import logging
from loguru import logger
import time


class SetLogging(object):
    def __init__(self,file=f"logs/debug{time.strftime('%Y-%m-%d')}.log"):
        self.file = file
        """创建日志器"""
        self.log = logging.getLogger()
        """日志器设置日志级别"""
        self.log.setLevel(logging.DEBUG)

    def setFormatter(self):
        """
        设置格式器
        :return: tuple
        """
        self.formatter1 = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
        self.formatter2 = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
        return self.formatter1, self.formatter2

    def setStreamHandle(self):
        """
        创建控制台处理器,将控制台处理器添加进日志器，控制台处理器设置日志级别，设置日志打印格式
        """
        stream_handle=logging.StreamHandler()
        self.log.addHandler(stream_handle) 
        stream_handle.setLevel(logging.DEBUG)
        stream_handle.setFormatter(self.setFormatter()[0])
    
    def setFileHandle(self):
        """
        创建文件处理器，将文件处理器添加进格式器，给文件处理器添加日志输出格式，给文件处理器设置日志输出级别
        ;parom file: file nome
        retucn:
        """
        filehandle = logging.FileHandler(filename=self.file, mode="a",encoding="utf-8")
        self.log.addHandler(filehandle)
        filehandle.setFormatter(self.setFormatter()[1])
        filehandle.setLevel(logging.INFO)

    def get_logger(self):
        """
        返还日志器
        :param file:
        :return :
        """
        self.setStreamHandle()
        self.setFileHandle()
        return self.log





class SetLoguru(object):
    log = logger

    def __init__(self):
        # enqueue开启多线程写入，会和gunicorn冲突，导致gunicorn无法正常启动，无限重启
        logger.add(f"logs/debug{time.strftime('%Y-%m-%d')}.log",rotation="00:00",encoding="utf-8",enqueue=False,retention="7 days")
    
    def trace(self, *args, **kwargs):
        return self.log.trace(*args, **kwargs)

    def debug(self, *args, **kwargs):
        return self.log.debug(*args, **kwargs)

    def info(self, *args, **kwargs):
        return self.log.info(*args, **kwargs)

    def warning(self, *args, **kwargs):
        return self.log.warning(*args, **kwargs)

    def error(self, *args, **kwargs):
        return self.log.error(*args, **kwargs)

    def critical(self, *args, **kwargs):
        return self.log.critical(*args, **kwargs)
    
    def exception(self, *args, **kwargs):
        return self.log.exception(*args, **kwargs)


