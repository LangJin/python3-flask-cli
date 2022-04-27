import os
import multiprocessing
from gevent import monkey
monkey.patch_all()


bind = "0.0.0.0:2333"
worker_class = 'gevent'
workers = multiprocessing.cpu_count() * 2 + 1
threads = multiprocessing.cpu_count() * 2
daemon = True
loglevel = 'debug'
x_forwarded_for_header = 'X-FORWARDED-FOR'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" "%({X-Real-IP}i)s"'
pidfile = "logs/gunicorn.pid"
accesslog = "logs/access.log"
errorlog = "logs/debug.log"


