from app.models.group import Group
from flask import request, jsonify
from app import db
from app.api import api


@api.route("/groups", methods=["GET"])
@api.route("/groups/<group_id>", methods=["GET"])
def get_groups(group_id=None):
    if group_id is not None:
        group = Group.get(db.session, group_id)
        return jsonify(group.serialize) if group is not None else {}
    else:
        groups = Group.get(db.session, group_id)
        return jsonify([group.serialize for group in groups])


@api.route("/groups", methods=["POST"])
def create_group():
    payload = request.get_json()
    new_group = Group(description=payload['description'],
                      company_id=payload['companyId'])
    created_group = Group.add(db.session, new_group)
    return jsonify(created_group.serialize)
