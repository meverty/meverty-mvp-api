from datetime import datetime
from db.dbconfig import DBConfig
from db.model.media_model import MediaModel
from entity.media import Media
from injector import inject

class MediaDAO:
    @inject
    def __init__(self, db_config:DBConfig):
        self._engine = db_config.engine
        self._session = db_config.session
        MediaModel.__table__.create(bind = self._engine, checkfirst = True)

    def insert_media(self, media:Media):
        model = MediaModel(media)
        self._session.add(model)
        self._session.commit()
        return model.id
