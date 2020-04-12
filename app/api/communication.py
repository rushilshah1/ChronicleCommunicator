import os
from app.api import api
from flask import request, jsonify
from app import db
from app.models.message import Message
from app.models.user import User
from sqlalchemy import join, select
import smtplib, ssl


@api.route("/communication", methods=["POST"])
def send_communication():
    """
    Payload dictates the communication the customer wants to send
    At a minimum, requires companyId, groupId, messageId, channelType.
    Just for a POC this will only support emails for a groupId. It will populate the message with two variables (user name and account number)
    :account_id, :first_name
    """
    payload = request.get_json()
    company_id = payload.get('companyId', None)
    group_id = payload.get('groupId', None)
    message_id = payload.get('messageId', None)
    channel_type = payload.get('channelType', None)
    if None in [company_id, group_id, message_id, channel_type]:
        return jsonify("Missing required field in request in order to send a communication")

    recipients = db.session.query(Message, User) \
        .filter(Message.company_id == company_id) \
        .filter(Message.group_id == group_id) \
        .filter(Message.message_id == message_id) \
        .filter(Message.active == True) \
        .filter(User.active == True) \
        .filter(Message.channel_type == 'EMAIL') \
        .filter(Message.group_id == User.group_id).all()


    email_statuses = list(map(lambda receipient_data: populate_message_template(receipient_data), recipients))
    if all(email_statuses):
        return jsonify("Emails successfully sent")
    else:
        return jsonify("Error in sending emails")


def populate_message_template(communication_data):
    message = communication_data[0]
    user = communication_data[1]
    email_address = user.email
    populated_message = message.message.replace(":account_id", str(user.account_id))
    populated_message = populated_message.replace(":first_name", user.first_name)
    send_emails(email_address, populated_message)


def send_emails(receiver_email, message):
    try:
        port = 465
        smtp_server = "smtp.gmail.com"
        sender_email = os.environ.get("sender_email", None)
        password = os.environ.get("sender_password", None)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except Exception:
        return False
    print(f"Email successfull send to {receiver_email}")
    return True

