from datetime import datetime
from db.dbconfig import DBConfig
from db.model.campaign_model import CampaignModel
from sqlalchemy.sql import func
from entity.campaign import Campaign
from injector import inject

class CampaignDAO:
    @inject
    def __init__(self, db_config:DBConfig):
        self._engine = db_config.engine
        self._session = db_config.session
        CampaignModel.__table__.create(bind = self._engine, checkfirst = True)

    def get_random_campaign(self) -> Campaign:
        query_result = self._session.query(CampaignModel).filter_by(activated = True).order_by(func.random()).first()
        result = query_result.toEntity()
        return result

    def insert_campaign(self, campaign:Campaign):
        model = CampaignModel(campaign)

        self._session.add(model)
        self._session.commit()