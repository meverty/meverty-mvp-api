from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

from db.dbconfig import LocalDBConfig

Base = declarative_base()

class CampaignModel(Base):
    __tablename__ = 'campaigns'
    id = Column(Integer, primary_key=True)
    campaign_name = Column(String(100))
    member_name = Column(String(30))
    impression = Column(Integer)
    image_url = Column(String(100))
    setup_date = Column(DateTime, default = datetime.utcnow)
    