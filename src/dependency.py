from db.dbconfig import DBConfig, LocalDBConfig, RemoteDBConfig
from injector import singleton
from service.member_service import MemberService

def configure(binder):
    binder.bind(MemberService, to = MemberService, scope=singleton)
    binder.bind(DBConfig, to = RemoteDBConfig, scope=singleton)