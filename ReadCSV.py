import pandas as pd
from pandas.core.frame import DataFrame
##Function to decorate data from csv file 
def ReadCSV(csvfile):
    data = pd.read_csv(csvfile)
    return data
