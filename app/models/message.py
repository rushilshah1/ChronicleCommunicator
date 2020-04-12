from sqlalchemy import MetaData, Column, Integer, String, Text, Boolean, Enum, TIMESTAMP, update
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime as dt
from app import db
import enum

Base = declarative_base(metadata=MetaData(schema="chronicle"))


class ChannelType(enum.Enum):
    SMS = "sms"
    EMAIL = "email"
    APP = "app"
    PUSH = "push"


class Message(db.Model):
    __tablename__ = 'message'

    message_id = Column(Integer, primary_key=True, autoincrement=True)
    channel_type = Column(Enum(ChannelType), nullable=False)
    message = Column(Text, nullable=False)
    group_id = Column(Integer, nullable=False)
    company_id = Column(Integer, nullable=False)
    created_ts = Column(TIMESTAMP, nullable=False, default=dt.now())
    updated_ts = Column(TIMESTAMP, nullable=False, default=dt.now())
    active = Column(Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"Message {self.message_id} associated with group: {self.group_id} and company: {self.company_id}"

    @staticmethod
    def get(session, message_id=None):
        return session.query(Message).all() if message_id is None else session.query(
            Message).filter_by(message_id=message_id).first()

    @staticmethod
    def add(session, new_message):
        session.add(new_message)
        session.commit()
        return Message.get(session, new_message.message_id)

    @staticmethod
    def update(session, updated_message):
        current_message = session.query(
            Message).filter_by(message_id=updated_message.message_id).first()
        if current_message:
            current_message.channel_type = updated_message.channel_type
            current_message.message = updated_message.message
            current_message.group_id = updated_message.group_id
            current_message.company_id = updated_message.company_id
            current_message.updated_ts = dt.now()
            current_message.active = updated_message.active
        session.commit()
        return current_message
    @property
    def serialize(self):
        return {
            "messageId": self.message_id,
            "channelType": self.channel_type.name,
            "message": self.message,
            "groupId": self.group_id,
            "companyId": self.company_id,
            "createdTimestamp": self.created_ts,
            "updatedTimestamp": self.updated_ts,
            "active": self.active
        }
