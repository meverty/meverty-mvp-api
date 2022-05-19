from db.dao.campaign_dao import CampaignDAO
from db.dao.event_dao import EventDAO
from db.dao.media_dao import MediaDAO
from entity.campaign import Campaign
from entity.event import Event
from injector import inject
from entity.member import Member
from entity.media import Media
import boto3
import constants


class AdvertisementService:
    @inject
    def __init__(self, event_dao:EventDAO, campaign_dao:CampaignDAO, media_dao:MediaDAO):
        self._event_dao = event_dao
        self._campaign_dao = campaign_dao
        self._media_dao = media_dao

    def new_campaign(self, campaign:Campaign):
        self._campaign_dao.insert_campaign(campaign)
        return True

    def upload_image(self, campaign_name):
        s3 = boto3.client('s3')

        campaign = self._campaign_dao.search_campaign(campaign_name)

        access_key = '.'+campaign.campaign_name+'-'+campaign.id
        s3.put_object(constants.AWS_S3_BUCKET_NAME, './temp', access_key)

        campaign.image_url = constants.BUCKET_ENDPOINT + '/' + access_key
        self._campaign_dao.insert_campaign(campaign)

