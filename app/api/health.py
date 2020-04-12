from flask import jsonify
from app.api import api

@api.route("/health")
def health_check():
    return jsonify(status="up", returnCode=200)