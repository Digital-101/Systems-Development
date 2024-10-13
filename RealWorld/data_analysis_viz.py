#Data Analysis and Visualization 
#Finance, Healthcare and Marketing
#PANDAS USED TO READ AND MANIPULATE DATA
#SOURCES - CSV, Excel, SQL

import pandas as pd
df = pd.read_csv('data.csv')
dfx = pd.read_excel('data.xlsx', sheet_name='Sheet1')
print(df)

#READ from PostgreSQL
import pandas as pd
import psycopg2
conn = psycopg2.connect(
host="localhost",
database="mydatabase",
user="myusername",
password="mypassword"
)
dfq = pd.read_sql('SELECT * FROM mytable', conn)
print(dfq)

#DATA CLEANING AND PREPARATION
#Handling missing data
#fillna() dropna() interpolate()
#import numpy as np
data = df.fillna(df.mean()) 

#Data Normalization and Scaling
#involve transforming data into a standard format to ensure fair comparison between variables.
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
dat_norm = scaler.fit_transform(df)

#EDA is a crucial step in understanding and summarizing the main characteristics of a dataset.
#Statistical and Visualization techniques
#meean() median() std(), head() tail() info() describe()

#Hypothesis Testing
#is a statistical method used to determine the validity of a hypothesis regarding a population parameter.
from scipy.stats import ttest_ind

group1 = [1,2,3,4,5]
group2 = [6,7,8,9,10]
stat, p = ttest_ind(group1, group2)
print("Test Statistic:",stat)
print("P-Vakue:",p)