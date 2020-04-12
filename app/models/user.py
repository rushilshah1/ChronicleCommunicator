from sqlalchemy import MetaData, Column, Integer, String, Text, Boolean, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime as dt
from app import db

Base = declarative_base(metadata=MetaData(schema="chronicle"))

class User(db.Model):

    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(Text, nullable=False)
    last_name = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    phone = Column(Text, nullable=True)
    group_id = Column(Integer, nullable=True)
    company_id = Column(Integer, nullable=False)
    account_id = Column(Integer, nullable=False)
    created_ts = Column(TIMESTAMP, nullable=False, default=dt.now())
    updated_ts = Column(TIMESTAMP, nullable=False, default=dt.now())
    active = Column(Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"User {self.first_name} {self.last_name} (user id {self.user_id}) associated with company {self.company_id} and group {self.group_id}"

    @staticmethod
    def get(session):
        return session.query(User).filter_by(active=True).all()
    @property
    def serialize(self):
        return {
            "userId": self.user_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "groupId": self.group_id,
            "companyId": self.company_id,
            "accountId": self.account_id,
            "createdTimestamp": self.created_ts,
            "updatedTimestamp": self.updated_ts,
            "active": self.active
        }

