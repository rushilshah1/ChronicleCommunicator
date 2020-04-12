from sqlalchemy import MetaData, Column, Integer, String, Text, Boolean, Enum, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime as dt
from app import db

Base = declarative_base(metadata=MetaData(schema="chronicle"))

class Group(db.Model):

    __tablename__ = 'group'

    group_id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(Text, nullable=False)
    company_id = Column(Integer, nullable=False)
    created_ts = Column(TIMESTAMP, nullable=False, default=dt.now())
    updated_ts = Column(TIMESTAMP, nullable=False, default=dt.now())
    active = Column(Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"Group {self.group_id}: {self.description}"

    @staticmethod
    def get(session):
        return session.query(Group).filter_by(active=True).all()
    
    @property
    def serialize(self):
        return {
            "groupId": self.group_id,
            "description": self.description,
            "companyId": self.company_id,
            "createdTimestamp": self.created_ts,
            "updatedTimestamp": self.updated_ts,
            "active": self.active
        }