# -*- coding:utf-8 -*-
import pymysql
import pandas as pd
from sshtunnel import SSHTunnelForwarder
 
import config
class SQLManager(object):
    def __init__(self,Config):
        self.cfg = config.ReadConfig(Config)
        Server = self.cfg['Server']
        DB = self.cfg['DB']
        self.conn = None
        self.cursor = None
        self.server = SSHTunnelForwarder(
                (Server['host'], Server['port']),    #B机器的配置
                ssh_password=Server['pwd'],
                ssh_username=Server['user'],
                remote_bind_address=(DB['host'], DB['port'] ))  #A机器的配置
        self.server.start()
        self.Connect()

    def Connect(self):
        DB = self.cfg['DB']
        print(self.server.local_bind_port)
        self.conn = pymysql.Connect(host='127.0.0.1',              #此处必须是是127.0.0.1
                           port=self.server.local_bind_port,
                           user=DB['user'],
                           passwd=DB['pwd'],
                           db=DB['database'])
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
    
    def Test(self,sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        print(data)
        return data

    def ExecuteSQL(self,sql,args = None):
        try:
            self.cursor.execute(sql,args)
            self.conn.commit()
        except:
            print('execution error occured !')
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
    data = DB.Test("SELECT * FROM Hybrid LIMIT 10")
    print(data)
    DB.Close()

if __name__ == '__main__':
    main()
