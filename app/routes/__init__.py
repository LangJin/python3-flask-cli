# -*- coding:utf-8 -*-
__author__ = 'LangJin'
from flask import Blueprint


authbp = Blueprint("user", __name__)

from . import user