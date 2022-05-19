from db.dbconfig import DBConfig, LocalDBConfig, RemoteDBConfig
from injector import singleton

def configure(binder):
    binder.bind(DBConfig, to = LocalDBConfig, scope=singleton)