# config.py
import os
import gevent.monkey
gevent.monkey.patch_all()

import multiprocessing

# debug = True
loglevel = 'debug'
bind = "0.0.0.0:2333"
pidfile = "logs/gunicorn.pid"
accesslog = "logs/access.log"
errorlog = "logs/debug.log"
daemon = True

# 启动的进程数
workers = multiprocessing.cpu_count()
worker_class = 'gevent'
x_forwarded_for_header = 'X-FORWARDED-FOR'