from typing import List
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import Session
from importlib import import_module


__factory = None


def _db_init(database_uri: str, database: DeclarativeMeta) -> None:
    global __factory

    if __factory:
        return

    conn_str = f'{database_uri}?check_same_thread=False'

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    database.metadata.create_all(engine)


def create_session(database_uri: str, database: DeclarativeMeta) -> Session:
    if not __factory:
        _db_init(database_uri, database)
    return __factory()


def add_urls(urlpatterns: List[str]):
    for file in urlpatterns:
        import_module(file)
