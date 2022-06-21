from asyncio import events
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

    def all_events(self):
        events = self._session.query(EventModel)
        return [e.toEntity() for e in events]

    def select_event_by_campaign(self, campaign_id):
        events = self._session.query(EventModel).filter_by(campaign_id = campaign_id)
        return [e.toEntity() for e in events]