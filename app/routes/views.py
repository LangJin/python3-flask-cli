# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Blueprint,request,g
from werkzeug.utils import secure_filename
from app.utils.dbFunc import MySQLDB as mysql
from app.utils.redisFunc import RedisDb as redis
from app.utils.responseFunc import resultMsg
from app.utils.requetFunc import Parse
from app.utils.commomFunc import create_token


views = Blueprint("views", __name__)


@views.route('/version', methods=['get'])
def version():
    data = {
        "version":"1.0",
        "info":"完成了各种功能的封装"
    }
    return resultMsg(data=data)



@views.route('/upload', methods=['post'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))