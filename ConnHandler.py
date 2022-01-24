from pickle import NONE
from config_utils import HGTD_config
from sshtunnel import SSHTunnelForwarder

import pathlib
import logging
import getpass
import os,re

logger = logging.getLogger("hgtd_db")
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

class ConnHandler():
	"""Main Handler for initializing connection """
	def __init__(self,Config):
		self.db_config = None ## server and db
		#self.ssh_server = None
		self.get_config(Config)
		self.print_config(Config)
		if not self.get_engine_string or self.db_config.server or re.match(r'lxplus\d{3}.cern.ch',os.popen("hostname").read()):
			self.connect_ssh()
			self.local_bt = self.get_local_bind_port()
	
	def connect_ssh(self):
		server = self.db_config.server
		db     = self.db_config.db
		if not server["password"]:
			self.pwd = self.get_passwd('server')
		else: self.pwd = server["password"] 
		logger.debug(f"> {server} {db}")
		self.ssh_server = SSHTunnelForwarder(
            (server['host'], server['port']),
            ssh_password= self.pwd,
            ssh_username=server['user'],
            remote_bind_address=(db['host'], db['port']),
			logger=None)
		self.ssh_server.start()
		
		logger.info(f">> Sucessfully connect to {db['host']} at {server['host']} !")
	
	def close_ssh(self):
		self.ssh_server.stop()

	def get_local_bind_port(self):
		return self.ssh_server.local_bind_port
	
	def get_passwd(self, type):
		if type == 'server':
			return getpass.getpass(f"Enter {self.db_config.server['user']}@{self.db_config.server['host']}'s password:")
		elif type == 'db':
			return getpass.getpass(f"Enter {self.db_config.db['user']}@{self.db_config.db['host']}'s password:")
	
	def get_config(self,Config):
		"""Retrieves configurations from yaml file"""
		if not pathlib.Path(Config).is_file():
			logger.critical(f"Config {Config} is not a file !")
			raise FileNotFoundError
		df_config_temp = HGTD_config(Config)
		self.db_config = df_config_temp


	def get_engine_string(self):
		server = self.db_config.server
		db     = self.db_config.db
		pwd = db['pwd'] 
		if not db['pwd']:
			pwd = self.get_passwd('get_passwd')
		if not server or re.match(r'lxplus\d{3}.cern.ch',os.popen("hostname").read()):
			string = f"mysql+pymysql://{db['user']}:{pwd}@{db['host']}/{db['database']}" ##locally connect
		else: 
			string =  f"mysql+pymysql://{db['user']}:{pwd}@localhost:{self.local_bt}/{db['database']}" ##remotely connect
		return string

	def print_config(self,Config):
		logger.info("*" * 100)
		logger.info(f">> Read from {Config}")
		logger.info(f">> Server: {self.db_config.server}")
		logger.info(f">> DB:     {self.db_config.db}")
		logger.info("*" * 100)	
	#def __exit__(self):
		#self.close_ssh()


def main():
	logger.info(">> Test database connection ")
	sql = ConnHandler('.config.yaml')

if __name__ == '__main__':
	main()
