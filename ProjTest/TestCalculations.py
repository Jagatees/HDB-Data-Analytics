import pandas as pd
import csv

df = pd.read_csv('ProjTest\Excel Data\Cleaned_HistoryData.csv', index=False)
df['Profit'] = df['Predicted_Price'] - df['Price']

print(df.head())
df.to_csv("Cleaned_HistoryData.csv", index=False)
