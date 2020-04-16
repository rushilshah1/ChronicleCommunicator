from flask import Blueprint
"""
Overall API:
Add common error handling mechanism with correct server response codes
Add validation to user input  - right now errors caught in internal server codes at the db level
"""
api = Blueprint("api", __name__, url_prefix="/chronicle")

from . import health, users, groups, messages, communication