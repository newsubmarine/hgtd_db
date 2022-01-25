from Root.database import Session
from models.hgtdpdb_models import Sensor
import matplotlib.pyplot as plt 
from utils.series_numbers import get_sn
#from WriteSensor import CSVtoJson
import time 
import pandas as pd


metadata = Session.query(Sensor).filter_by(id = 2).first()
print(metadata.vendor)
