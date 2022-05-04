from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from entity.event import Event

Base = declarative_base()

class EventModel(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer)
    media_id = Column(Integer)
    fingerprint = Column(String(256))
    event_type = Column(String(20))
    event_timestamp = Column(DateTime, default = datetime.utcnow)

    def __init__(self, event:Event):
        self.campaign_id = event.campaign_id
        self.media_id = event.media_id
        self.fingerprint = event.fingerprint
        self.event_type = event.event_type
        self.event_timestamp = event.event_timestamp

    def toEntity(self):
        event = Event(self.campaign_id, self.media_id, self.fingerprint, self.event_type, self.id, self.event_timestamp)
        return event