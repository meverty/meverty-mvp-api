from xmlrpc.client import Boolean
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


from db.dbconfig import LocalDBConfig
from entity.campaign import Campaign

Base = declarative_base()

class CampaignModel(Base):
    __tablename__ = 'campaigns'
    id = Column(Integer, primary_key=True)
    campaign_name = Column(String(100))
    member_id = Column(Integer)
    image_url = Column(String(256))
    setup_date = Column(DateTime, default = datetime.utcnow)
    campaign_type = Column(String(20))
    interaction_url = Column(String(256))
    activated = Column(Boolean)

    def __init__(self, campaign:Campaign):
        self.campaign_name = campaign.campaign_name
        self.member_id = campaign.member_id
        self.image_url = campaign.image_url
        self.setup_date = campaign.setup_date
        self.campaign_type = campaign.campaign_type
        self.interaction_url = campaign.interaction_url
        self.activated = campaign.activated

    def toEntity(self) -> Campaign:
        campaign = Campaign(self.campaign_name, self.member_id, self.campaign_type, self.interaction_url, 
                            id=self.id, image_url=self.image_url, setup_date=self.setup_date, activated=self.activated)
        return campaign