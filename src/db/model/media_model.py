from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from entity.media import Media

from db.dbconfig import LocalDBConfig

Base = declarative_base()

class MediaModel(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    member_id = Column(Integer)
    metaverse = Column(String(20))
    media_type = Column(String(20))
    setup_timestamp = Column(DateTime, default = datetime.utcnow)
    
    def __init__(self, media:Media):
        self.member_id = media.member_id
        self.metaverse = media.metaverse
        self.media_type = media.media_type
        self.setup_timestamp = media.setup_timestamp

    def toEntity(self) -> Media:
        media = Media(self.member_id, self.metaverse, self.media_type, id=self.id, setup_timestamp=self.setup_timestamp)
        return media