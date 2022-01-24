from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, engine
from flask_config import mysetup
import logging
import os
import ConnHandler
logger = logging.getLogger("hgtd_db")
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

## Only be calling creat_engine and session once !

Base = declarative_base()
connect = ConnHandler.ConnHandler("/Users/xinst/work/db/hgtd_db/.config.yaml")
engine = create_engine(connect.get_engine_string())
Session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

