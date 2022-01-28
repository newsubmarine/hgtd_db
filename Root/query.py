import argparse
from sqlalchemy import column
from Root.database import Session
import models.hgtdpdb_models as models 
from sqlalchemy.inspection import inspect
from utils.series_numbers import get_sn
import logging

logger = logging.getLogger(__name__)
parser = argparse.ArgumentParser()
parser.add_argument("action",help="actions to be processed", choices=['list_all_tables','list_all_columns','query_all','query_first'])
parser.add_argument("--type",'-type',help="the table name")
parserd = parser.parse_args()


def list_all_tables():
	tables = [table.__name__ for table in models.HGTDModel.__subclasses__()]
	print(tables)
	#return tables

class SessionHandler(object):
	def __init__(self,type):
		self.session = Session
		self.type = getattr(models,type)


	def get_all_columns(self):		
		columns = inspect(self.type).c
		return columns

	def print_all_colums(self):
		columns = self.get_all_columns()
		print(f"Column names {[c.name for c in columns]}")
		print(f"Column types {[c.type for c in columns]}")

		
class Write(SessionHandler):
	def __init__(self, type, input, output):
		super().__init__(type)
		self.input = input
	def upload(self):
		#metadata = Session.query(Sensor).filter_by(SensorId = SN).first()
		return True
	def check_input(self):
		return True


class Query(SessionHandler):
	def __init__(self, type, input = ""):
		super().__init__(type)
		self.input = input
		#self.expression = self.get_expression()

	def query_all(self):
		metadata =(Session.query(self.type).all())
		#for data in metadata:
		return metadata

	def query_first(self):
		metadata = Session.query(self.type).first()
		return metadata	

	def get_expression(self):
		strings = input("Enter your query command:")
		if strings:
			logger.info(f"Dncoding query commands is not ready now.")
			#logger.info(f"Start to query table {type}:")
		else:
			logger.info(f"There is no input, will list the first row of table {type}")
		return strings
	
	def print_tables(self):
		columns = self.get_all_columns()
		#datas = 
		[ getattr(self.type,c.name) for c in columns]


def main():	
	if parserd.action == 'list_all_tables':
		list_all_tables()
	else:
		if not parserd.type:
			logger.error("--type <table> is not provided!")
		test = Query(parserd.type)
		columns = test.get_all_columns()
		
		if parserd.action == 'list_all_columns':
			test.print_all_colums()
		elif parserd.action == 'query_all':
				datas = test.query_all()
				test.print_all_colums()
				for data in datas:
					for c in columns:
						print([ getattr(data,c.name) for c in columns])
		elif parserd.action == 'query_first':
				datas = test.query_first()
				test.print_all_colums()
				print([getattr(datas,c.name) for c in columns])

if __name__ == "__main__":
	main()


 