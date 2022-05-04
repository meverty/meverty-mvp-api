from datetime import datetime
from db.dbconfig import DBConfig
from db.model.member_model import MemberModel
from entity.member import Member
from injector import inject

class MemberDAO:
    @inject
    def __init__(self, db_config:DBConfig):
        self._engine = db_config.engine
        self._session = db_config.session
        MemberModel.__table__.create(bind = self._engine, checkfirst = True)

    def insert_member(self, member:Member):
        model = MemberModel(member)

        self._session.add(model)
        self._session.commit()

    def search_member(self, member_name) -> Member:
        query_result = self._session.query(MemberModel).filter_by(member_name = member_name).first()

        if query_result is None:
            return None

        result = query_result.toEntity()
        return result