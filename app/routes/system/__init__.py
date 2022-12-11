from flask import Blueprint

systembp = Blueprint("system",__name__,url_prefix="/system")

from . import user