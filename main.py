# -*- coding:utf-8 -*-
__author__ = 'LangJin'
import logging
from app import create_app


app = create_app()


if __name__ != "__main__":  
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


if __name__ == "__main__":  
    app.run(host="0.0.0.0",port=3456)
