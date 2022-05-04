from flask_restx import Namespace, Resource
from flask import request, jsonify
from injector import inject
from metaverse.metaverse_service import MetaverseService
from entity.event import Event
from entity.media import Media

Metaverse = Namespace('Metaverse')

@Metaverse.route("/newevent")
class MetaverseNewEvent(Resource):
    @inject
    def __init__(self, metaverse_service:MetaverseService, api):
        self._metaverse_service = metaverse_service
        super().__init__(api)

    def post(self):
        params = request.get_json()
        event = Event(params['campaign_id'], params['media_id'], params['fingerprint'], params['event_type'])
        result = self._metaverse_service.new_event(event)
        return jsonify(message=result)


@Metaverse.route("/newmedia")
class MetaverseNewMedia(Resource):
    @inject
    def __init__(self, metaverse_service:MetaverseService, api):
        self._metaverse_service = metaverse_service
        super().__init__(api)

    def post(self):
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
        campaign= self._metaverse_service.get_random_ad()

        return jsonify(message = {
            'campaign_id':campaign.id, 
            'image_url': campaign.image_url, 
            'campaign_type':campaign.campaign_type, 
            'interaction_url':campaign.interaction_url
        })