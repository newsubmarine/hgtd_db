#Time: 2021-8-20 15:04
#Author: Shuiting Xin
#To upload Sensor information to database
#the file name of IV is saved as VD
## IV,CV format : json style with "key" - "array" 
#  example:
#           {
#           "VOLTAGE": 
#                   [700, 700, 700],
#           "CAPACITANCE":
#                   [7, 7, 7]
#           }
from os import EX_PROTOCOL
from old.ReadCSV import ReadCSV
import json
import time
import os,argparse,subprocess,sys

###############################
## Set up Input Options
###############################

parser = argparse.ArgumentParser()
parser.add_argument("--ivfile","-iv", help="IV file",default="")
parser.add_argument("--cvfile","-cv", help="CV file",default="")
parser.add_argument("--sensorid","-id", help="The ID of sensor, PRIMARY KEY!!!",default="")
parser.add_argument("--verbosity","-v", help="increase ouput verbosity",action="store_true")
parserd = parser.parse_args()

def CSVtoJson(csvfile):
    if csvfile == "" : sys.exit("ERROR: no csvfile input!!")
    df = ReadCSV(csvfile)
    head = df.columns.values
    values = df.values
    values = [[row[i] for row in values] for i in range(len(values[0]))] ##transport the list
    dic = dict(zip(head,values))
    return json.loads(json.dumps(dic))

def WriteSensorIVCV(table,File,datatype):
    if( File == "") :
        print(" At least one file is needed!")
        sys.exit("ERROR: no IV data")
    DB = SQLManager.SQLManager("config.yaml")
    ##Construct IV data if IV file exsits, Convert csv to json format here
    ID = "\'" + parserd.sensorid  + "\'"
    data = "\'" + CSVtoJson(File) + "\'"
    
    CurrentTime = str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    CT = "\'" + CurrentTime + "\'"
    UT = "\'" + CurrentTime + "\'"
    VD = "\'"+ parserd.ivfile.split("/")[-1][:-4] + "\'" # last [:-4] to remove .csv suffix 
    ## should add "" by hand
    election = True
    sql = f"INSERT INTO {table}(SensorId,CreateTime,UpdateTime,Vendor,{datatype}) VALUES({ID},{CT},{UT},{VD},{data}) ON DUPLICATE KEY UPDATE UpdateTime = {UT},{datatype}={data},Vendor={VD}"
    if parserd.verbosity: print(sql)
    DB.ExecuteSQL(sql)

if __name__ == '__main__':
    if parserd.ivfile == "" and parserd.cvfile =="":
        sys.exit("ERROR: --ivfile and --ivfile missing. Cannot proceed\nexample file:  share/IMEv2_W4_III_D2_1-4.csv, share/IMEv1_W7_IV_B4_L1-15-100_10kHz.csv ")
    if parserd.sensorid == "":
        sys.exit("ERROR: Please provide sensor id ")
    if parserd.ivfile != "": WriteSensorIVCV("Sensor",parserd.ivfile,"IV")
    if parserd.cvfile != "": WriteSensorIVCV("Sensor",parserd.cvfile,"CV")
