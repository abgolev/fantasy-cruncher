import csv
import pandas as pd
import numpy as np

for y in range(1970, 2020):
	doc = r'data_v2/yearly_updated/' + str(y) + '.csv'
	df1 = pd.read_csv(doc)
	df1 = df1.drop(columns='Att.1')
	df1 = df1.drop(columns='Yds.1')
	df1 = df1.drop(columns='Yds.2')
	df1 = df1.drop(columns='GS')
	#df1 = df1.drop(columns='Unnamed: 0')
	df1.to_csv(r'data_v2/yearly_updated/'+str(y)+'.csv', index=False)
