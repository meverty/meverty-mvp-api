from db.dbconfig import DBConfig
from db.model.event_model import EventModel
from entity.event import Event
from injector import inject

class EventDAO:
    @inject
    def __init__(self, db_config:DBConfig):
        self._engine = db_config.engine
        self._session = db_config.session
        EventModel.__table__.create(bind = self._engine, checkfirst = True)

    def insert_event(self, event:Event):
        model = EventModel(event)
        self._session.add(model)
        self._session.commit()