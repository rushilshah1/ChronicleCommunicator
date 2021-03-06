import os
import smtplib, ssl
import logging
from app.api import api
from flask import request, jsonify
from app import db
from app.models.message import Message
from app.models.user import User
from app.models.message import ChannelType


logging.basicConfig(level=logging.INFO)


@api.route("/communication", methods=["POST"])
def send_communication():
    """
    This POST endpoint is used to trigger a communication.
    At a minimum, requires companyId, groupId, messageId, channelType.
    Just for a POC this will only support emails for a groupId. It will populate the message with two variables (first name and account id)
    """
    payload = request.get_json()
    company_id = payload.get('companyId', None)
    group_id = payload.get('groupId', None)
    message_id = payload.get('messageId', None)
    channel_type = payload.get('channelType', None)
    if None in [company_id, group_id, message_id, channel_type]:
        return jsonify("Missing required field in request in order to send a communication")

    recipients = db.session.query(Message, User) \
        .join(User, Message.group_id == User.group_id) \
        .filter(Message.company_id == company_id) \
        .filter(Message.group_id == group_id) \
        .filter(Message.message_id == message_id) \
        .filter(Message.active == True) \
        .filter(User.active == True) \
        .filter(Message.channel_type == ChannelType.EMAIL).all()

    logging.info(f"{len(recipients)} recipients of desired communication")
    email_statuses = list(map(lambda receipient_data: populate_message_template(receipient_data), recipients))
    if len(email_statuses) == 0:
        return jsonify("There are no emails to send")
    elif all(email_statuses):
        return jsonify("Emails successfully sent")
    else:
        return jsonify("Error in sending emails")


def populate_message_template(communication_data):
    """
    Unpacks the tuple containing message and user info, populates predefined message template with user account_id and first_name, and sends email
    :param communication_data: tuple
    :return: status of sent email
    """
    message = communication_data[0]
    user = communication_data[1]
    email_address = user.email
    populated_message = message.message_template.replace(":account_id", str(user.account_id))
    populated_message = populated_message.replace(":first_name", user.first_name)
    return send_email(email_address, populated_message)


def send_email(receiver_email, message):
    """
    Sends email to specified receipient email with sepecified message
    * Sender_email and sender_password must be set as env variables for this to work correctly *
    :param receiver_email: str
    :param message: str
    :return:
    """
    try:
        port = 465
        smtp_server = "smtp.gmail.com"
        logging.info("Sending email")
        sender_email = os.environ.get("sender_email", None)
        password = os.environ.get("sender_password", None)
        if sender_email is None or password is None:
            logging.error("Cannot send email. Need to establish sender email and password as environment variables")
            return False
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    except Exception:
        logging.error("Error in sending email")
        return False
    logging.info(f"Email successfully sent to {receiver_email}")
    return True
