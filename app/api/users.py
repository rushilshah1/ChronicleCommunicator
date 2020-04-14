from flask import request, jsonify
from app import db
from app.models.user import User
from app.api import api


@api.route("/users", methods=["GET"])
@api.route("/users/<user_id>", methods=["GET"])
def get_users(user_id=None):
    if user_id is not None:
        user = User.get(db.session, user_id)
        return jsonify(user.serialize) if user is not None else {}
    else:
        users = User.get(db.session)
        return jsonify([user.serialize for user in users])


@api.route("/users", methods=["POST"])
def create_user():
    payload = request.get_json()
    new_user = User(first_name=payload["firstName"],
                    last_name=payload['lastName'],
                    email=payload['email'],
                    phone=payload['phone'],
                    group_id=payload['groupId'],
                    company_id=payload['companyId'],
                    account_id=payload['accountId'])
    created_user = User.add(db.session, new_user)
    return jsonify(created_user.serialize)
