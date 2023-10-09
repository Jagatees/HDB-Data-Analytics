import KerwinFunction
import pandas as pd

MDollarHseFilePath = 'ProjTest\\Excel Data\\MillionDollarHse.csv'
HistoryFilePath = 'ProjTest\\Excel Data\\HistoryResaleData.csv'

#Add scrapping code here
MDollarHseDT =  pd.read_csv(MDollarHseFilePath)
MDollarHseDT['Concat_Add'] = MDollarHseDT['Blk_No'] + ' ' + MDollarHseDT['Address']

HistoryHseDT = pd.read_csv(HistoryFilePath)
HistoryHseDT['Concat_Add'] = HistoryHseDT['block'] + ' ' + HistoryHseDT['street_name']

#df3 = MDollarHseDT[MDollarHseDT['Concat_Add'].isin(HistoryHseDT['Concat_Add'])]

#merged_df = pd.merge(MDollarHseDT, HistoryHseDT, left_on='Concat_Add', right_on='Concat_Add', how='inner')

#df3.drop_duplicates()

#df3.to_csv('ProjTest\\Excel Data\\TestRun.csv', index=True)

merged_df = MDollarHseDT.merge(HistoryHseDT, on='Concat_Add')

MDollarHseDT['remaining_lease'] = merged_df['remaining_lease']
MDollarHseDT['floor_area_sqm'] = merged_df['floor_area_sqm']

merged_df.drop_duplicates()
MDollarHseDT.to_csv('ProjTest\\Excel Data\\MillionDollarHse.csv', index=True)
print('done')