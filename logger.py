# -*- coding:utf-8 -*-
__author__ = 'LangJin'
import logging
from logging.handlers import TimedRotatingFileHandler

formatter = logging.Formatter("[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s][%(thread)d] - %(message)s")
handler = TimedRotatingFileHandler("./log/flask.log", when="D", interval=1, backupCount=15,encoding="UTF-8", delay=False, utc=True)

