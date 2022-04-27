# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from app import create_app
from logger import handler


app = create_app()


if __name__ == "__main__":  
    app.logger.addHandler(handler)
    app.run(host="0.0.0.0",port=2333)
