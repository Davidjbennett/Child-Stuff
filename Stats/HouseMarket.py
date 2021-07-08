import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('UTSTHPI.csv')

# df.info()
# print(df.head())
print(df['DATE'].value_counts().head())

#!Get data from csv
#!Display data on a graph
#!Put data into a table
#!Take table and calculate next 10 years of possible house cost
#!display new data on a table
#!Include descriptions on the graphs and data 
