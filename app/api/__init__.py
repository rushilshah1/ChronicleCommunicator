from flask import Blueprint

api = Blueprint("api", __name__, url_prefix="/chronicle")

from . import health, users, groups, messages, communication