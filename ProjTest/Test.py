import KerwinFunction
import pandas as pd
import requests
import time

CSV = 'ProjTest\\Excel Data\\csv_merged_final.csv'
#Read the CSV File
UserDF = pd.read_csv(CSV)

Row_Count_Start = len(UserDF)

print("Row COunt with duplicates: " + str(Row_Count_Start))

UserDF.drop_duplicates(subset='Full Address', keep='first', inplace=True)

Row_Count_Drop = len(UserDF)

print("Row Count without duplicates: " + str(Row_Count_Drop))

if Row_Count_Drop > 4500:
    # If there are more than 4500 rows, drop rows beyond the first 4500
    UserDF = UserDF.head(4500)

Row_Count_MoreDrop = len(UserDF)

print("Count of rows after dropping those exceeding 4500 is: " + str(Row_Count_MoreDrop))

