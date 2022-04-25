from datetime import datetime
from db.dbconfig import DBConfig
from db.model.campaign_model import CampaignModel
from injector import inject

class CampaignDAO:
    @inject
    def __init__(self, db_config:DBConfig):
        self._engine = db_config.engine
        self._session = db_config.session
        CampaignModel.__table__.create(bind = self._engine, checkfirst = True)