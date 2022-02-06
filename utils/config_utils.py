import yaml
import logging

logger = logging.getLogger("hgtd_db")

class Config(object):
	def __init__(self,config):
		self.config = self.get_config_dict(config)
	def get_config_dict(self,config):
		dict = yaml.load(open(config), Loader = yaml.SafeLoader)
		logger.debug(f"{dict}")
		return dict

class HGTD_config(Config):
	"""Utils class to deal with configs for developers"""
	def __init__(self,config):
		super(HGTD_config,self).__init__(config)
		self.server = None
		self.db     = None
		self.get_config(config)
	def get_config(self,config):
		dict = self.config
		if "Server" in dict:
			self.server = dict["Server"]
		else:
			logger.info(f"Server is not provided in {config}, you must have logined lxplus !")
		if "DB" in dict:
			self.db = dict["DB"]
		else:
			logger.critical(f"DB is not provided in {config} !")
		if "Verbose" in dict:
			self.verbose = dict['Verbose']
		logger.info(f"{dict}")
'''
class Flask_config(Config):
	"""Flask app configuration"""
	def __init__(self):

		super().__init__()
	SECRET_KEY = 
'''