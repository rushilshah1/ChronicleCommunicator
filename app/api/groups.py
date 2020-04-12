from app.models.group import Group
from flask import request, jsonify
from app import db
from app.api import api

@api.route("/groups")
def get_groups():
    groups = Group.get(db.session)
    return jsonify([group.serialize for group in groups])

@api.route("/group", methods=["POST"])
def create_group():
    payload = request.get_json()
    new_group = Group(description=payload['description'],
                    company_id=payload['companyId'])
    db.session.add(new_group)
    db.session.commit()
    return jsonify(f"{new_group} successfully created")