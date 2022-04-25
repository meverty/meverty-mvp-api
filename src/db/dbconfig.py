from abc import ABC, abstractmethod
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from injector import inject

class DBConfig(ABC):
    @abstractmethod
    def engine():
        raise NotImplementedError("Must define get_engine().")
    
    @abstractmethod
    def session():
        raise NotImplementedError("Must define get_session().")


class LocalDBConfig(DBConfig):
    def __init__(self):
        self._engine = create_engine("sqlite:///test.db", echo=True)
        self._session = sessionmaker(bind=self._engine)()

    @property
    def engine(self):
        return self._engine

    @property
    def session(self):
        return self._session


class RemoteDBConfig(DBConfig):
    def __init__(self):
        db_host = os.environ.get('DB_HOST')
        db_id = os.environ.get('DB_ID')
        db_password = os.environ.get('DB_PASSWORD')
        db_name = os.environ.get('DB_NAME')
        db_port = os.environ.get('DB_PORT')

        url = "mysql+pymysql://"+db_id+':'+db_password+'@'+db_host+':'+db_port+'/'+db_name

        self._engine = create_engine(url, echo=True)
        self._session = sessionmaker(bind=self._engine)()

    @property
    def engine(self):
        return self._engine

    @property
    def session(self):
        return self._session