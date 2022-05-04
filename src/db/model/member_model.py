from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from db.dbconfig import LocalDBConfig
from entity.member import Member


Base = declarative_base()

class MemberModel(Base):
    __tablename__ = 'members'
    id = Column(Integer, primary_key=True)
    member_name = Column(String(30))
    member_type = Column(String(10))
    join_timestamp = Column(DateTime, default = datetime.utcnow)

    def __init__(self, member:Member):
        self.member_name = member.member_name
        self.member_type = member.member_type
        self.join_timestamp = member.join_timestmap

    def toEntity(self) -> Member:
        member = Member(self.member_name, self.member_type, id=self.id, join_timestamp=self.join_timestamp)
        return member