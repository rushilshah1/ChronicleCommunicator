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
    new_message = Message(channel_type=payload['channelType'],
                          message_template=payload['message'],
                          group_id=payload['groupId'],
                          company_id=payload['companyId']
                          )
    created_message = Message.add(db.session, new_message)
    return jsonify(created_message.serialize)


@api.route("/messages", methods=["PUT"])
def update_message():
    payload = request.get_json()
    updated_message = Message(
        message_id=payload['messageId'],
        channel_type=payload['channelType'],
        message_template=payload['message'],
        group_id=payload['groupId'],
        company_id=payload['companyId'],
        active=payload['active']
    )
    updated_message = Message.update(db.session, updated_message)
    return jsonify(updated_message.serialize)
