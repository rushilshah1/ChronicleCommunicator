from app.models.message import Message
from flask import request, jsonify
from app import db
from app.api import api


@api.route("/messages", methods=["GET"])
@api.route("/messages/<message_id>", methods=["GET"])
def get_messages(message_id=None):
    if message_id is not None:
        message = Message.get(db.session, message_id)
        return jsonify(message.serialize) if message is not None else {}
    else:
        messages = Message.get(db.session)
        return jsonify([message.serialize for message in messages])


@api.route("/messages", methods=["POST"])
def create_message():
    payload = request.get_json()
    new_message = Message(channel_type=payload.get('channelType', None),
                          message_template=payload.get('message', None),
                          group_id=payload.get('groupId', None),
                          company_id=payload.get('companyId', None)
                          )
    #TODO: Add validation of request before hitting the database
    created_message = Message.add(db.session, new_message)
    return jsonify(created_message.serialize)


@api.route("/messages", methods=["PUT"])
def update_message():
    payload = request.get_json()
    updated_message = Message(
        message_id=payload.get('messageId', None),
        channel_type=payload.get('channelType', None),
        message_template=payload.get('message', None),
        group_id=payload.get('groupId', None),
        company_id=payload.get('companyId', None),
        active=payload.get('active', True)
    )
    #TODO: Add validation of request before hitting the database
    updated_message = Message.update(db.session, updated_message)
    return jsonify(updated_message.serialize)
