from typing import List, Optional
import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import Session
from importlib import import_module

__factory = None


def db_init(database_uri: str, database: DeclarativeMeta, check_same_thread: Optional[bool] = False,
            echo=False) -> None:
    """Create session factory. Use before creating the first session"""

    global __factory

    if __factory:
        return

    conn_str = f'{database_uri}?check_same_thread={check_same_thread}' if isinstance(check_same_thread,
                                                                                     bool) else database_uri

    engine = sa.create_engine(conn_str, echo=echo)
    __factory = orm.sessionmaker(bind=engine)

    database.metadata.create_all(engine)


def create_session() -> Session:
    return __factory()


def add_urls(urlpatterns: List[str]) -> None:
    for file in urlpatterns:
        import_module(file)
