from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from injector import inject
from advertisement.advertisement_service import AdvertisementService
from entity.campaign import Campaign
from entity.event import Event
from entity.media import Media
from storage.s3connection import S3Connection


Advertisement = Namespace('Advertisement')

@Advertisement.route("/newcampaign")
class AdvertisementNewCampign(Resource):

    campaign_model = Advertisement.model('Campaign', {
        'campaign_name': fields.String(description='캠페인 이름', required=True, example="TestAdvertisement"),
        'member_id': fields.Integer(description='캠페인 소유자 ID', required=True, example="1"),
        'campaign_type': fields.String(description='캠페인 종류(iAB 기준)', required=True, example="Medium Rectangle"),
        'interaction_url': fields.String(description='interaction 시 연결되는 url', required=True, example="http://naver.com")
    })

    @inject
    def __init__(self, advertisement_service:AdvertisementService, api):
        self._advertisement_service = advertisement_service

        super().__init__(api)

    @Advertisement.expect(campaign_model)
    def post(self):
        """새로운 캠페인을 등록합니다."""
        params = request.get_json()
        campaign = Campaign(params['campaign_name'], params['member_id'], params['campaign_type'], params['interaction_url'])

        result = self._advertisement_service.new_campaign(campaign)
        return jsonify(message={'result': result})


@Advertisement.route("/setcampaignimage")
class AdvertisementSetCampaignImage(Resource):
    @inject
    def __init__(self, advertisement_service:AdvertisementService, api):
        self._advertisement_service = advertisement_service
        super().__init__(api)

    def post(self):
        params = request.get_json()
        file = request.files['file']
        file.save['./temp']
        result = self._advertisement_service.upload_image(params['campaign_name'])
        return jsonify(message={'result': result})
