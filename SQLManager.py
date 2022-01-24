# -*- coding:utf-8 -*-
import pymysql
import pandas as pd
from sshtunnel import SSHTunnelForwarder
<<<<<<< HEAD
 
import setup
class SQLManager(object):
    def __init__(self,Config):
        self.cfg = setup.ReadConfig(Config)
=======
import sys 
import config

class SQLManager(object):
    def __init__(self,Config):
        self.cfg = config.ReadConfig(Config)
>>>>>>> 93794ce6c983bb8780729e2513b7193688902252
        Server = self.cfg['Server']
        DB = self.cfg['DB']
        self.conn = None
        self.cursor = None
        self.server = SSHTunnelForwarder(
                (Server['host'], Server['port']),    
                ssh_password=Server['pwd'],
                ssh_username=Server['user'],
<<<<<<< HEAD
                remote_bind_address=(DB['host'], DB['port'] )) 
        self.server.start()
        self.Connect()

    def Connect(self):
        DB = self.cfg['DB']
        print(self.server.local_bind_port)
        self.conn = pymysql.Connect(host='127.0.0.1',              
                           port=self.server.local_bind_port,
=======
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
>>>>>>> 93794ce6c983bb8780729e2513b7193688902252
                           user=DB['user'],
                           passwd=DB['pwd'],
                           db=DB['database'])
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
    
<<<<<<< HEAD
    def Test(self,sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print(data)
        return data
=======
    def QuerySQL(self,sql):
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            sys.exit('ERROR: ',e.args)

    #def CheckData(self,table,ID):
>>>>>>> 93794ce6c983bb8780729e2513b7193688902252

    def ExecuteSQL(self,sql,args = None):
        try:
            self.cursor.execute(sql,args)
            self.conn.commit()
<<<<<<< HEAD
        except:
            print('execution error occured !')
            self.conn.rollback()
=======
            print('Sucessful executed !')
        except Exception as e:
            print('Execution error occured !')
            print('ERROR: ',e.args)
            self.conn.rollback()

>>>>>>> 93794ce6c983bb8780729e2513b7193688902252
    
    def Close(self):
        self.cursor.close()
        self.conn.close()
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.Close()


def main():
<<<<<<< HEAD
    DB = SQLManager(".config.yaml")
    data = DB.Test("SELECT * FROM Hybrid LIMIT 10")
=======
    DB = SQLManager("config.yaml")
    data = DB.QuerySQL("SELECT * FROM Hybrid LIMIT 10")
>>>>>>> 93794ce6c983bb8780729e2513b7193688902252
    print(data)
    DB.Close()

if __name__ == '__main__':
    main()
