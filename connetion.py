from config_utils import HGTD_config
from sshtunnel import SSHTunnelForwarder

import pathlib
import logging
import getpass

logger = logging.getLogger("hgtd_db")
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

bind_port = None

def ConnHandler(Config):
	"""Main Handler for initializing connection """
		db_config = get_config(Config)
		print_config(Config)
		if db_config.server:
			connect_ssh(db_config)

def connect_ssh(db_config):
	server = db_config.server
	db     = db_config.db
	pwd = get_passwd(db_config,'server')
	logger.debug(f"> {server} {db}")
	ssh_server = SSHTunnelForwarder(
            (server['host'], server['port']),
            ssh_password= self.pwd,
            ssh_username=server['user'],
            remote_bind_address=(db['host'], db['port']),
			logger=None)
	ssh_server.start()
	logger.info(f">> Sucessfully connect to {db['host']} at {server['host']} !")
	
def close_ssh(self):
	self.ssh_server.stop()

def get_local_bind_port(ssh_server):
	bind_port = ssh_server.local_bind_port
	
def get_passwd(db_config,type):
	if type == 'server':
		return getpass.getpass(f"Enter {db_config.server['user']}@{db_config.server['host']}'s password:")
	elif type == 'db':
		return getpass.getpass(f"Enter {db_config.db['user']}@{db_config.db['host']}'s password:")

def get_config(Config):
	"""Retrieves configurations from yaml file"""
	if not pathlib.Path(Config).is_file():
		logger.critical(f"Config {Config} is not a file !")
		raise FileNotFoundError
		df_config_temp = HGTD_config(Config)
		return df_config_temp 


def get_engine_string(db_config):
	server = db_config.server
	db     = db_config.db
	pwd = db['pwd'] 
	if not db['pwd']:
		pwd = get_passwd(db_config,'get_passwd')
	return f"mysql+pymysql://{db['user']}:{pwd}@localhost:{bind_port}/{db['database']}"


def print_config(db_config,Config):
	logger.info("*" * 100)
	logger.info(f">> Read from {Config}")
	logger.info(f">> Server: {db_config.server}")
	logger.info(f">> DB:     {db_config.db}")
	logger.info("*" * 100)	
	#def __exit__(self):
		#self.close_ssh()

