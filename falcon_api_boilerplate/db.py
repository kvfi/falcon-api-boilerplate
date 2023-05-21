from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from falcon_api_boilerplate.utils.config import get_config

engine = create_engine(get_config('db.main.database-uri'), connect_args={'client_encoding': 'utf8'})

inspector = inspect(engine)

Base = declarative_base()

session_factory = sessionmaker(bind=engine)
session = scoped_session(session_factory)

