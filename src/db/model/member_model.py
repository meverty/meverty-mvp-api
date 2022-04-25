from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from db.dbconfig import LocalDBConfig


Base = declarative_base()

class MemberModel(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    member_name = Column(String(30))
    join_date = Column(DateTime, default = datetime.utcnow)