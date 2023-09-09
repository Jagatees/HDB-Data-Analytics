import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from matplotlib import pyplot as plt
import matplotlib
import os

matplotlib.rcParams["figure.figsize"] = (20, 10)

df = pd.read_csv('ProjTest\Excel Data\RentalDummyData.csv')
df.head() #Show table
df.shape #Return Rol count, Col count
df.loc[30] #Return Row Number

df2 = df.copy()
df2['Avg_Rent'] = df2['Average_Rental_Price'] + 1
print(df2.head())
len(df2.town.unique())

#df2.town = df2.town.apply(lambda x: x.strip())

Location_stats = df2.groupby('town')['Avg_Rent'].mean()
#print(Location_stats)
print(Location_stats[Location_stats<=850])

Rent_Location_Less_Than_850 = len(Location_stats[Location_stats<=850])
print(Rent_Location_Less_Than_850)
print(df2.shape)

df3 = df2[~(df2.Avg_Rent)-1 <= 850]
print(df3.Average_Rental_Price.describe())