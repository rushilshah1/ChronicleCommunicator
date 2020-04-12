from app.models.message import Message
from flask import request, jsonify
from app import db
from app.api import api


@api.route("/messages")
def get_messages():
    messages = Message.get(db.session)
    return jsonify([message.serialize for message in messages])


@api.route("/message", methods=["POST"])
def create_message():
    payload = request.get_json()
    new_message = Message(channel_type=payload['channelType'],
                          message=payload['message'],
                          group_id=payload['groupId'],
                          company_id=payload['companyId']
                          )
    db.session.add(new_message)
    db.session.commit()
    return jsonify(f"{new_message} successfully created")
