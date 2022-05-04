from db.dao.campaign_dao import CampaignDAO
from db.dao.event_dao import EventDAO
from db.dao.media_dao import MediaDAO
from entity.event import Event
from injector import inject
from entity.member import Member
from entity.media import Media

class MetaverseService:
    @inject
    def __init__(self, event_dao:EventDAO, campaign_dao:CampaignDAO, media_dao:MediaDAO):
        self._event_dao = event_dao
        self._campaign_dao = campaign_dao
        self._media_dao = media_dao

    def new_event(self, event:Event):
        self._event_dao.insert_event(event)

    def get_random_ad(self):
        campaign = self._campaign_dao.get_random_campaign()
        return campaign

    def new_media(self, media:Media):
        id = self._media_dao.insert_media(media)
        return id
