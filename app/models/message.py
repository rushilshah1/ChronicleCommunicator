from sqlalchemy import MetaData, Column, Integer, String, Text, Boolean, Enum, TIMESTAMP
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
    def get(session):
        return session.query(Message).filter_by(active=True).all()

    @property
    def serialize(self):
        return {
            "messageId": self.message_id,
            "channelType": self.channel_type,
            "message": self.message,
            "groupId": self.group_id,
            "companyId": self.company_id,
            "createdTimestamp": self.created_ts,
            "updatedTimestamp": self.updated_ts,
            "active": self.active
        }

