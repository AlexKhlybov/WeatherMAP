from os.path import join

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import BASEDIR, DB_NAME, DB_NAME_TEST, TESTING


def create_sqlite_uri(db_name):
    return "sqlite:///" + join(BASEDIR, db_name)


if TESTING == "True":
    # Use separate DB for tests
    SQLALCHEMY_DATABASE_URL = create_sqlite_uri(DB_NAME_TEST)

    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
else:
    SQLALCHEMY_DATABASE_URL = create_sqlite_uri(DB_NAME)

    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
