from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from injector import inject
from metaverse.metaverse_service import MetaverseService
from entity.event import Event
from entity.media import Media

Metaverse = Namespace('Metaverse')

@Metaverse.route("/newevent")
class MetaverseNewEvent(Resource):

    event_model = Metaverse.model('Event', {
        'campaign_id': fields.Integer(description='시청한 캠페인 ID', required=True, example="1"),
        'media_id': fields.Integer(description='해당 매체 ID', required=True, example="1"),
        'fingerprint': fields.String(description='사용자 fingerprint 정보', required=True, example="fingerprint"),
        'event_type': fields.String(description='이벤트의 type', required=True, example="interaction")
    })

    @inject
    def __init__(self, metaverse_service:MetaverseService, api):
        self._metaverse_service = metaverse_service
        super().__init__(api)

    @Metaverse.expect(event_model)
    def post(self):
        """광고 발생 이벤트를 등록합니다."""
        params = request.get_json()
        event = Event(params['campaign_id'], params['media_id'], params['fingerprint'], params['event_type'])
        result = self._metaverse_service.new_event(event)
        return jsonify(message={'result': result})


@Metaverse.route("/newmedia")
class MetaverseNewMedia(Resource):

    media_model = Metaverse.model('Media', {
        'member_id': fields.Integer(description='매체를 소유한 사용자의 ID', required=True, example="1"),
        'metaverse': fields.String(description='소속 메타버스 이름', required=True, example="Decentraland"),
        'media_type': fields.String(description='매체 타입(iAB기준)', required=True, example="Medium Rectangle"),
    })
    
    @inject
    def __init__(self, metaverse_service:MetaverseService, api):
        self._metaverse_service = metaverse_service
        super().__init__(api)

    @Metaverse.expect(media_model)
    def post(self):
        """새로운 매체를 등록합니다."""
        params = request.get_json()
        media = Media(params['member_id'], params['metaverse'], params['media_type'])
        result = self._metaverse_service.new_media(media)
        return jsonify(message=result)


@Metaverse.route("/getad")
class MetaverseGetAdURL(Resource):
    @inject
    def __init__(self, metaverse_service:MetaverseService, api):
        self._metaverse_service = metaverse_service
        super().__init__(api)

    def get(self):
        """무작위 광고 정보를 반환합니다."""
        campaign= self._metaverse_service.get_random_ad()

        return jsonify(message = {
            'campaign_name': campaign.campaign_name,
            'campaign_id':campaign.id, 
            'image_url': campaign.image_url, 
            'campaign_type':campaign.campaign_type, 
            'interaction_url':campaign.interaction_url
        })