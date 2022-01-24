from telnetlib import SE
from database import Session
from models.Models import Sensor
import matplotlib.pyplot as plt 
from Utils import get_sn
from WriteSensor import CSVtoJson
import time 
import pandas as pd

def get_time():
	return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

## Create
IV = CSVtoJson("share/IMEv2_W4_III_D2_1-4.csv")
CV = CSVtoJson("share/IMEv1_W7_IV_B4_L1-15-100_10kHz.csv")
SN = get_sn("Sensor")
sensor1 = Sensor(SensorId = SN,CreateTime = get_time(), UpdateTime = get_time(),IV=IV,CV=CV)
Session.add(sensor1)
Session.commit()

## Read
metadata = Session.query(Sensor).filter_by(SensorId = SN).first()
print(metadata)
dic = metadata.IV 
plt.plot(dic['Signal Current[A]'],dic["Bias Voltage[V]"])
plt.show()

## Update
metadata.Vendor = "NDL"
metadata.UpdateTime = get_time()
Session.commit()

## Delete
metadata.delete()
Session.commit()