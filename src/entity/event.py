from datetime import datetime


class Event:
    def __init__(self, campaign_id, media_id, fingerprint, event_type, id=0, event_timestamp=datetime.now()):
        self._id = id
        self._campaign_id = campaign_id
        self._media_id = media_id
        self._fingerprint = fingerprint
        self._event_type = event_type
        self._event_timestamp = event_timestamp

    @property
    def id(self):
        return self._id
    
    @property
    def campaign_id(self):
        return self._campaign_id

    @property
    def media_id(self):
        return self._media_id

    @property
    def fingerprint(self):
        return self._fingerprint

    @property
    def event_type(self):
        return self._event_type

    @property
    def event_timestamp(self):
        return self._event_timestamp