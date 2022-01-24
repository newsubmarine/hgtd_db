#Time: 2021-8-20 21:22
#Author: Shuiting Xin
#Read Sensor data

import json
import os,argparse,subprocess,sys
import SQLManager
################################
## Set up Input Options
################################

parser = argparse.ArgumentParser()
parser.add_argument("--sensorid")

def ReadSensor():
    data = "*"
    selection = True
<<<<<<< HEAD
    DB = SQLManager.SQLManager(".config.yaml")
=======
    DB = SQLManager.SQLManager("config.yaml")
>>>>>>> 93794ce6c983bb8780729e2513b7193688902252
    sql = f"SELECT {data} from Sensor where {selection}"
    output = DB.QuerySQL(sql)
    print(output)

if __name__ == '__main__':
    ReadSensor()
