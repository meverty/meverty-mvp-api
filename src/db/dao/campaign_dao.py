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

    def update_campaign(self, campaign:Campaign):
        model = self._session.query(CampaignModel).filter_by(campaign_name = campaign.campaign_name).first()
        model.image_url = campaign.image_url

        self._session.commit()

    def search_campaign(self, campaign_name) -> Campaign:
        query_result = self._session.query(CampaignModel).filter_by(campaign_name = campaign_name).first()

        if query_result is None:
            return None

        result = query_result.toEntity()
        return result

    def search_campaign_by_id(self, campaign_id) -> Campaign:
        query_result = self._session.query(CampaignModel).filter_by(id = campaign_id).first()

        if query_result is None:
            return None

        result = query_result.toEntity()
        return result

    def all_campaigns(self):
        campaigns = self._session.query(CampaignModel)
        return [c.toEntity() for c in campaigns]