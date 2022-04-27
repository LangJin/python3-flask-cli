# -*- coding:utf-8 -*-
__author__ = 'LangJin'
import logging

handler = logging.FileHandler('logs/debug.log', encoding='UTF-8')
handler.setLevel(logging.DEBUG)
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)