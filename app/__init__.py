import imp
import os
from re import I
from flask import Flask
from flask import Blueprint
#from ..db import Session
from .main import main 
from .db_crud import db_crud
#main = Blueprint('main',__name__)

def create_app():#(config_name):
	app = Flask(__name__)
	#app.config.from_object()
	app.register_blueprint(main)
	app.register_blueprint(db_crud)
	app.config['SECRET_KEY'] = os.urandom(32)
	return app


