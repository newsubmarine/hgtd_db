# -*- coding:utf-8 -*-
import pymysql
import pandas as pd
from sshtunnel import SSHTunnelForwarder
import sys 
import config

class SQLManager(object):
    def __init__(self,Config):
        self.cfg = config.ReadConfig(Config)
        Server = self.cfg['Server']
        DB = self.cfg['DB']
        self.conn = None
        self.cursor = None
        self.server = SSHTunnelForwarder(
                (Server['host'], Server['port']),    
                ssh_password=Server['pwd'],
                ssh_username=Server['user'],
                remote_bind_address=(DB['host'], DB['port']))
        
        try:
            self.server.start()
            self.bind = self.server.local_bind_port
        
        except Exception as e:
            sys.exit("Error Cannot connect to lxplus", e.args)
        try:    
            self.Connect()
        except Exception as e:
            sys.exit("Error Cannot connect to database", e.args)
    
    def Connect(self):
        DB = self.cfg['DB']
        print(" the local bind is %s" %self.bind)
        self.conn = pymysql.Connect(host= '127.0.0.1',              
                           port=self.bind,
                           user=DB['user'],
                           passwd=DB['pwd'],
                           db=DB['database'])
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
    
    def QuerySQL(self,sql):
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            sys.exit('ERROR: ',e.args)

    #def CheckData(self,table,ID):

    def ExecuteSQL(self,sql,args = None):
        try:
            self.cursor.execute(sql,args)
            self.conn.commit()
            print('Sucessful executed !')
        except Exception as e:
            print('Execution error occured !')
            print('ERROR: ',e.args)
            self.conn.rollback()

    
    def Close(self):
        self.cursor.close()
        self.conn.close()
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Close()


def main():
    DB = SQLManager("config.yaml")
    data = DB.QuerySQL("SELECT * FROM Hybrid LIMIT 10")
    print(data)
    DB.Close()

if __name__ == '__main__':
    main()
