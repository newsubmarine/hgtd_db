import sys
import yaml
def ReadConfig(config):
	with open(config, 'r') as ymlfile:
		try:
			cfg = yaml.load(ymlfile,Loader=yaml.FullLoader)
			return cfg
		except:
			return False
