import KerwinFunction

MDollarHseFilePath = 'ProjTest\\Excel Data\\MillionDollarHse.csv'


MDollarHseDT =  KerwinFunction.GetHistoryDatafromcsv(MDollarHseFilePath)
MDollarHseDF = MDollarHseDT.drop_duplicates() 

MDollarHseSQM = MDollarHseDF['floor_area_sqm'].tolist()
MDollarHseLease = MDollarHseDF['remaining_lease'].tolist()

MDollarHseSQM_Float = [eval(x) for x in MDollarHseSQM]
MDollarHseLease_Float = [eval(x) for x in MDollarHseLease]

MDollarHseDF['SQM_Points'] = MDollarHseDF['floor_area_sqm'].apply(KerwinFunction.calculate_sqm_points)
MDollarHseDF['Lease_Points'] = MDollarHseDF['remaining_lease'].apply(KerwinFunction.calculate_lease_points)

MDollarHseDF.to_csv('ProjTest\\Excel Data\\TestRun.csv', index=True)
