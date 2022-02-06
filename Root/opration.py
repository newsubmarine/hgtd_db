## Next: maybe print in dataframe style is better
import ast
import logging
import argparse

import pymysql

logger = logging.getLogger("hgtd_db")
parser = argparse.ArgumentParser()
subparsers= parser.add_subparsers(dest = "command", help = "type of opration")
#parser.add_argument("--opration",'-opration',help="oprations towards database", choices=['query','insert','update','delate'])

query_parser = subparsers.add_parser("query")
insert_parser= subparsers.add_parser("insert")
query_parser.add_argument("--action",help="actions to be processed", choices=['list_all_tables','list_all_columns','query_all','query_first'])
query_parser.add_argument("--type",'-type',help="the table name")
query_parser.add_argument("--expression",'-exp', action='store_true', default=False)
insert_parser.add_argument("--type",'-type',help="the table name")
insert_parser.add_argument("--action",help="actions to be processed")
insert_parser.add_argument("--input",help="input file")
insert_parser.add_argument("--update",'-up', action='store_true', default=False)
parserd = parser.parse_args()

from re import I
from sqlalchemy import column
from Root.database import Session,engine
import models.hgtdpdb_models as models 
from sqlalchemy.inspection import inspect
from utils.series_numbers import get_sn
import pandas as pd
import numpy as np
import re


def yes_or_no():
	answer = None
	while answer not in ("yes","no"):
		answer = input("Enter yes or no: ")
		if answer == "yes":
			return True
		elif answer == "no":
			return False
		else:
			logger.warning("Please enter yes or no")


def list_all_tables():
	## Return table names
	tables = [table.__tablename__ for table in models.HGTDModel.__subclasses__()]
	print("Following tables are defined: ")
	print(tables)
	#return tables

def input_from_csv(path):
	pass

class SessionHandler(object):
	def __init__(self,type):
		self.session = Session
		self.type = getattr(models,type.title()) #classes are defined with a capital letter


	def get_all_columns(self):		
		columns = inspect(self.type).c
		return columns

	def print_all_columns(self):
		columns = self.get_all_columns()
		#print(f"Column names {[c.name for c in columns]}")
		print("table: %s" %self.type.__tablename__)
		print("%-10s  %s" %( "column", "type"))
		print("-"*20)
		[print("%-10s %s" % (c.name,c.type)) for c in columns]
	
	def get_operator(self,key,value):
		if re.match(r"^!", value):
			''' ! '''
			val = re.sub(r"!","",value)
			return key.__ne__(val)
		elif re.match(r">(?!=)", value):
			''' > '''
			val = re.sub(r">(?!=)","",value)
			return key.__gt__(val)
		elif re.match(r"<(?!=)", value):
			''' < '''
			val = re.sub(r"<(?!=)","",value)
			return key.__lt__(val)
		elif re.match(r">=", value):
			''' >= '''
			val = re.sub(r">=","",value)
			return key.__ge__(val)
		elif re.match(r"<=", value):
			''' <= '''
			val = re.sub(r"<=","",value)
			return key.__le__(val)
		elif re.match(r"(\w*),(\w*)", value):
			''' between '''
			a, b = re.split(r',',value)
			return key.between(a,b)
		else:
			''' == '''
			return key.__eq__(value)

	def get_filter_by_args(self,dic_args: dict):
		filters = []
		for key, value in dic_args.items():
			filters.append(self.get_operator(getattr(self.type, key),value))
		return filters

		
class Write(SessionHandler):
	def __init__(self, type, input):
		super().__init__(type)
		#self.input = input_from_csv(input)
		self.tablename = self.type.__tablename__ # classes name == tables name
		self.temp = f"{type}_template.csv"
		self.input= input
	
	def upload(self):
		#if parserd.opration not in ["insert","replace"]:
		#	logger.error(f"unvalid option {parserd.opration} for action {parserd.action}")
		#metadata = Session.query(Sensor).filter_by(SensorId = SN).first()
		#Basiclly there are two ways to upload datas:
		#1)Create table instance and excute by models.table_class.add(tableXXX)
		#  In this way a function to code tableXXX is necessary
		#2)By assembling RAW SQL commands: "INSERT INTO table_name (column1, column2, column3, ...)"
		#3)By using pandas to_sql utils: df.to_sql(table_name, sqlalchemy.engine)
		## Find to be potentially problematic dealing with the data type
		
		if parserd.command != "insert":
			logger.error(f"You should use insert!")
		df = self.check_inputs()
		if_exists = "append"  ## "replace will delate old records"
		
		print(f"\n {df}")
		logger.warning(f"The above row will be added to table {self.tablename}")
		if yes_or_no():
			try:
				df.to_sql(self.tablename,con=engine, if_exists = if_exists, index = False)
				Session.commit()	
				logger.info("Record uploading success !")
			except Exception as e:
				logger.exception(e)
				logger.error("Check if the data already exsits! If so please turn on --update")
				#for index, row in df.iterrows():
					#print(row)

		else:
				logger.warning(f"Change isn't commited ")
		logger.debug(engine.execute(f"SELECT * FROM {self.tablename}").fetchall())
	
	def update(self):
		df = self.check_inputs()
		change = 0 
		for data in df.itertuples(index=False):
				if np.isnan(data.SN):
					logger.error("SN doesn't exist!")
				metadata = Session.query(self.type).filter_by(id=data.id).first()
				for c in df.columns:  # loop each columns
					target = getattr(data, c)  # values to be changed
					attr = getattr(self.type, c)  # corresponded attribute
					org  = getattr(metadata,c)
					if pd.isna(target):
						continue
					#attr = target
					print(type(org),attr,type(target))
					if str(org) == str(target):
						continue
					setattr(metadata, c, target)
					change = change + 1
		print(f"You have {change} change")
		Session.commit()
		
	def gen_csv_template(self):
		table = Query(self.type.__name__) ## the class name
		header = [c.name for c in table.get_all_columns()]
		out = open(self.temp,"w")
		out.write(",".join(header))# column name of target tabla
		out.close()

	def check_inputs(self):
		pd_reader = pd.read_csv(self.input,delimiter=',')
		pd_reader.reset_index(drop=True, inplace = True)
		return pd_reader
	

class Query(SessionHandler):
	def __init__(self, type, input = ""):
		super().__init__(type)
		self.input = input
		#self.expression = self.get_expression()

	def query_all(self):
		if parserd.expression:
			from clause import dic_args
			filters = self.get_filter_by_args(dic_args)
			logger.info("Reading selections from clause.py")
			df = pd.read_sql(Session.query(self.type).filter(*filters).statement,Session.bind) 
		else:
			df = pd.read_sql(Session.query(self.type).statement,Session.bind)
		return df

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
		[ getattr(self.type,c.name) for c in columns]
	
			



class Delete(SessionHandler):
	def __init__(self, type, SN):
		super().__init__(type)
		self.SN = SN
	def delete_by_SN(self):
		metadata =Session.query(self.type).filter_by(SN = self.SN).all()
		logger.warning(f"The following row will be deleted!")




def main():	
	if parserd.command == "query":
		if parserd.action == 'list_all_tables':
			list_all_tables()
		else:
			if not parserd.type:
				logger.error("--type <table> is not provided!")
			test = Query(parserd.type)
			columns = test.get_all_columns()
		
			if parserd.action == 'list_all_columns':
				test.print_all_columns()
			elif parserd.action == 'query_all':
					datas = test.query_all()
					print(datas)
			elif parserd.action == 'query_first':
					datas = test.query_first()
					test.print_all_columns()
					print([getattr(datas,c.name) for c in columns])
	elif parserd.command == "insert":
		if not parserd.type:
			logger.error("--type <table> is not provided!")
		test = Write(parserd.type,parserd.input)
		test.gen_csv_template()
		if parserd.update:
			test.update()
		else:
			test.upload()
	
if __name__ == "__main__":
	main()


 