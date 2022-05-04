from datetime import datetime

class Media:
    def __init__(self, member_id, metaverse, media_type, id=0, setup_timestamp=datetime.now()):
        self._id = id
        self._member_id = member_id
        self._metaverse = metaverse
        self._media_type = media_type
        self._setup_timestamp = setup_timestamp

    @property
    def id(self):
        return self._id

    @property
    def member_id(self):
        return self._member_id

    @member_id.setter
    def member_id(self, value):
        self._member_id = value

    @property
    def metaverse(self):
        return self._metaverse

    @property
    def media_type(self):
        return self._media_type
    
    @property
    def setup_timestamp(self):
        return self._setup_timestamp