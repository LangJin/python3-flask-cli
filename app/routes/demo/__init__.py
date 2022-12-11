from flask import Blueprint

demobp = Blueprint("demoTest",__name__,url_prefix="/demo")

from . import user