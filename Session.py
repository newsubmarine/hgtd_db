from re import I
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy import create_engine
from flask_config import mysetup
import ConnHandler

connect = ConnHandler.ConnHandler(".config.yaml")
engine = create_engine(connect.get_engine_string())

Session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

from Models import Sensor

mySession = Session()
for row in mySession.query(Sensor).all():
	print(row.IV)
