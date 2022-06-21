from db.dao.campaign_dao import CampaignDAO
from db.dao.event_dao import EventDAO
from db.dao.media_dao import MediaDAO
from entity.event import Event
from injector import inject
from entity.media import Media

class DashboardService:
    @inject
    def __init__(self, event_dao:EventDAO, campaign_dao:CampaignDAO, media_dao:MediaDAO):
        self._event_dao = event_dao
        self._campaign_dao = campaign_dao
        self._media_dao = media_dao

    def get_advertisement_statistics(self):
        campaigns = self._campaign_dao.all_campaigns()

        result = []
        for c in campaigns:
            data = dict()

            data['id'] = c.id
            data['name'] = c.campaign_name
            data['impression'] = 0
            data['interaction'] = 0
            
            events = self._event_dao.select_event_by_campaign(c.id)

            for e in events:
                if e.event_type == 'impression':
                    data['impression'] += 1
                
                if e.event_type == 'interaction':
                    data['interaction'] += 1
            
            result.append(data)
        
        return result