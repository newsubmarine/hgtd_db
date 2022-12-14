from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, engine
import logging
import os
from Root.ConnHandler import ConnHandler
logger = logging.getLogger("hgtd_db")
logging.basicConfig()
logging.getLogger().setLevel(logging.WARNING)

## Only be calling creat_engine and session once !

Base = declarative_base()
connect = ConnHandler(".config.yaml")
engine = create_engine(connect.get_engine_string())
Session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

