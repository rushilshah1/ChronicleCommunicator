from flask import request, jsonify
from app import db
from app.models.user import User
from app.api import api


@api.route("/users")
def get_all_users():
    users = User.get(db.session)
    return jsonify([i.serialize for i in users])

@api.route("/user", methods=["POST"])
def create_user():
    payload = request.get_json()
    new_user = User(first_name=payload["firstName"],
                    last_name=payload['lastName'],
                    email=payload['email'],
                    phone=payload['phone'],
                    company_id=payload['companyId'],
                    account_id=payload['accountId'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(f"{new_user} successfully created")


