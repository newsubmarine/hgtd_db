#import 
from os import EX_PROTOCOL
import SQLManager
import ReadCSV
def WriteHybridCSV(table,csvfile):
	'''
	Example 

	INSERT INTO Hybrid(HybridId,CreateTime,UpdateTime,Vendor,Batch,MetroX,MetroY,MetroZ) 
	VALUES('200001','2021-07-29 15:34:30','2021-07-29 15:34:32','NDL','100000',30,31,32);

	'''
	DB = SQLManager.SQLManager("config.yaml")
	df = ReadCSV.ReadCSV(csvfile)	
	'''
	for index,value in df.iterrows():
		ID = value['HybridId']
		CT = str(value['CreateTime'])
		UT = str(value['UpdateTime'])
		Vd = str(value['Vendor'])
		Bt = str(value['Batch'])
		X = value['MetroX']
		Y = value['MetroY']
		Z = value['MetroZ']
		User = 1000
		sql =  f"INSERT INTO {table}(HybridId,CreateTime,UpdateTime,Vendor,Batch,MetroX,MetroY,MetroZ,UserId) VALUES({ID},{CT},{UT},{Vd},{Bt},{X},{Y},{Z},{User});"
	'''
	
	values = df.values.tolist()
	for value in values:
		sql =  f"INSERT INTO {table}(HybridId,CreateTime,UpdateTime,Vendor,Batch,MetroX,MetroY,MetroZ,UserId) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,1000);"
		print(sql,value)
		DB.ExecuteSQL(sql,value)
	DB.Close()

def main():
	WriteHybridCSV("Hybrid","example.csv")

if __name__ == '__main__':
    main()
