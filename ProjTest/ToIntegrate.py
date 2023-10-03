import pandas as pd
import numpy as np
import KerwinFunction

#CSV File Paths
FairpriceFilePath = 'ProjTest\\Excel Data\\fairprice.csv'
HospitalFilePath = 'ProjTest\\Excel Data\\HospitalClinic.csv'
MallsFilePath = 'ProjTest\\Excel Data\\Malls.csv'
MRTDataFilePath = 'ProjTest\\Excel Data\\MRTData.csv'
ParksFilePath = 'ProjTest\\Excel Data\\Parks.csv'
PriSchFilePath = 'ProjTest\\Excel Data\\primaryschool.csv'
SecSchFilePath = 'ProjTest\\Excel Data\\secondaryschool.csv'
TertiaryFilePath = 'ProjTest\\Excel Data\\tertiaryschool.csv'
UniversityFilePath = 'ProjTest\\Excel Data\\univeristies.csv'
MDollarHseFilePath = 'ProjTest\\Excel Data\\MillionDollarHse.csv'

#Add scrapping code here
UserHseFilePath = 'ProjTest\\Excel Data\\DummyUserAddress.csv'

#Amenties Points
Hospital_ClinicPoint = 5
SchoolsPoint = 4
MRTPoint = 3
Supermarket_MallPoint = 2
ParksPoint = 1

#Read the CSV File
UserAddressArray = KerwinFunction.ReadCSVFile(UserHseFilePath)

#Convert User Address into coordinates
KerwinFunction.GetLongLatFromAddress(UserAddressArray, UserHseFilePath)

#get long and lat from all csv file save into datatable
FairpriceDT = KerwinFunction.GetCoordinatesfromcsv(FairpriceFilePath)
HospitalDT = KerwinFunction.GetCoordinatesfromcsv(HospitalFilePath)
MallsDT = KerwinFunction.GetCoordinatesfromcsv(MallsFilePath)
MRTDataDT = KerwinFunction.GetCoordinatesfromcsv(MRTDataFilePath)
ParksDT = KerwinFunction.GetCoordinatesfromcsv(ParksFilePath)
PriSchDT = KerwinFunction.GetCoordinatesfromcsv(PriSchFilePath)
SecSchDT = KerwinFunction.GetCoordinatesfromcsv(SecSchFilePath)
TertairyDT = KerwinFunction.GetCoordinatesfromcsv(TertiaryFilePath)
UniversityDT = KerwinFunction.GetCoordinatesfromcsv(UniversityFilePath)
MDollarHseDT =  KerwinFunction.GetCoordinatesfromcsv(MDollarHseFilePath)
UserHseDT = KerwinFunction.GetCoordinatesfromcsv(UserHseFilePath)

#Remove all the duplicated values
MDollarHseDF = MDollarHseDT.drop_duplicates() 
UserHseDF = UserHseDT.drop_duplicates()


#Retrieve the long and lat and store them indivually into a list
FairpriceLong = FairpriceDT['Long'].tolist()
FairpriceLat = FairpriceDT['Lat'].tolist()
HospitalLong = HospitalDT['Long'].tolist()
HospitalLat = HospitalDT['Lat'].tolist()
MallsLong = MallsDT['Long'].tolist()
MallsLat = MallsDT['Lat'].tolist()
MRTLong = MRTDataDT['Long'].tolist()
MRTLat = MRTDataDT['Lat'].tolist()
ParksLong = ParksDT['Long'].tolist()
ParksLat = ParksDT['Lat'].tolist()
PriSchLong = PriSchDT['Long'].tolist()
PriSchLat = PriSchDT['Lat'].tolist()
SecSchLong = SecSchDT['Long'].tolist()
SecSchLat = SecSchDT['Lat'].tolist()
TertairyLong = TertairyDT['Long'].tolist()
TertairyLat = TertairyDT['Lat'].tolist()
UniLong = UniversityDT['Long'].tolist()
UniLat = UniversityDT['Lat'].tolist()
MDollarHseLong = MDollarHseDF['Long'].tolist()
MDollarHseLat = MDollarHseDF['Lat'].tolist()
UserHseLong = UserHseDF['Long'].tolist()
UserHseLat = UserHseDF['Lat'].tolist()

#Convert string list to float list
FairpriceLat_Float = [eval(x) for x in FairpriceLat]
FairpriceLong_Float = [eval(x) for x in FairpriceLong]
HospitalLat_Float = [eval(x) for x in HospitalLat]
HospitalLong_Float = [eval(x) for x in HospitalLong]
MallsLat_Float = [eval(x) for x in MallsLat]
MallsLong_Float = [eval(x) for x in MallsLong]
MRTLat_Float = [eval(x) for x in MRTLat]
MRTLong_Float = [eval(x) for x in MRTLong]
ParksLat_Float = [eval(x) for x in ParksLat]
ParksLong_Float = [eval(x) for x in ParksLong]
PriSchLat_Float = [eval(x) for x in PriSchLat]
PriSchLong_Float = [eval(x) for x in PriSchLong]
SecSchLat_Float = [eval(x) for x in SecSchLat]
SecSchLong_Float = [eval(x) for x in SecSchLong]
TertairyLat_Float = [eval(x) for x in TertairyLat]
TertairyLong_Float = [eval(x) for x in TertairyLong]
UniLat_Float = [eval(x) for x in UniLat]
UniLong_Float = [eval(x) for x in UniLong]
MDollarHseLat_Float = [eval(x) for x in MDollarHseLat]
MDollarHseLong_Float = [eval(x) for x in MDollarHseLong]
UserHseLat_Float = [eval(x) for x in UserHseLat]
UserHseLong_Float = [eval(x) for x in UserHseLong]

#Calculate distance between MDollarhse and the amenties
MDollarHse_FairpriceDist = KerwinFunction.Calculate_Hse_Amenities_Dist(MDollarHseLat_Float, MDollarHseLong_Float, FairpriceLat_Float, FairpriceLong_Float, 'Fairprice')
MDollarHse_FairpriceDT = pd.DataFrame(MDollarHse_FairpriceDist)

MDollarHse_HosDist = KerwinFunction.Calculate_Hse_Amenities_Dist(MDollarHseLat_Float, MDollarHseLong_Float, HospitalLat_Float, HospitalLong_Float, 'HosClinic')
MDollarHse_HosDT = pd.DataFrame(MDollarHse_HosDist)

MDollarHse_MallsDist = KerwinFunction.Calculate_Hse_Amenities_Dist(MDollarHseLat_Float, MDollarHseLong_Float, MallsLat_Float, MallsLong_Float, 'Malls')
MDollarHse_MallsDT = pd.DataFrame(MDollarHse_MallsDist)

MDollarHse_MRTDist = KerwinFunction.Calculate_Hse_Amenities_Dist(MDollarHseLat_Float, MDollarHseLong_Float, MRTLat_Float, MRTLong_Float, 'MRT')
MDollarHse_MRTDT = pd.DataFrame(MDollarHse_MRTDist)

MDollarHse_ParksDist = KerwinFunction.Calculate_Hse_Amenities_Dist(MDollarHseLat_Float, MDollarHseLong_Float, ParksLat_Float, ParksLong_Float, 'Parks')
MDollarHse_ParksDT = pd.DataFrame(MDollarHse_ParksDist)

MDollarHse_PriSchDist = KerwinFunction.Calculate_Hse_Amenities_Dist(MDollarHseLat_Float, MDollarHseLong_Float, PriSchLat_Float, PriSchLong_Float, 'Primary School')
MDollarHse_PriSchDT = pd.DataFrame(MDollarHse_PriSchDist)

MDollarHse_SecSchDist = KerwinFunction.Calculate_Hse_Amenities_Dist(MDollarHseLat_Float, MDollarHseLong_Float, SecSchLat_Float, SecSchLong_Float, 'Secondary School')
MDollarHse_SecSchDT = pd.DataFrame(MDollarHse_SecSchDist)

MDollarHse_TertairyDist = KerwinFunction.Calculate_Hse_Amenities_Dist(MDollarHseLat_Float, MDollarHseLong_Float, TertairyLat_Float, TertairyLong_Float, 'Tertairy')
MDollarHse_TertairyDT = pd.DataFrame(MDollarHse_TertairyDist)

MDollarHse_UniDist = KerwinFunction.Calculate_Hse_Amenities_Dist(MDollarHseLat_Float, MDollarHseLong_Float, UniLat_Float, UniLong_Float, 'Uni')
MDollarHse_UniDT = pd.DataFrame(MDollarHse_UniDist)

#Calculate distance between Userhse and the amenties

UserHse_FairpriceDist = KerwinFunction.Calculate_Hse_Amenities_Dist(UserHseLat_Float, UserHseLong_Float, FairpriceLat_Float, FairpriceLong_Float, 'Fairprice')
UserHse_FairpriceDT = pd.DataFrame(UserHse_FairpriceDist)

UserHse_HosDist = KerwinFunction.Calculate_Hse_Amenities_Dist(UserHseLat_Float, UserHseLong_Float, HospitalLat_Float, HospitalLong_Float, 'HosClinic')
UserHse_HosDT = pd.DataFrame(UserHse_HosDist)

UserHse_MallsDist = KerwinFunction.Calculate_Hse_Amenities_Dist(UserHseLat_Float, UserHseLong_Float, MallsLat_Float, MallsLong_Float, 'Malls')
UserHse_MallsDT = pd.DataFrame(UserHse_MallsDist)

UserHse_MRTDist = KerwinFunction.Calculate_Hse_Amenities_Dist(UserHseLat_Float, UserHseLong_Float, MRTLat_Float, MRTLong_Float, 'MRT')
UserHse_MRTDT = pd.DataFrame(UserHse_MRTDist)

UserHse_ParksDist = KerwinFunction.Calculate_Hse_Amenities_Dist(UserHseLat_Float, UserHseLong_Float, ParksLat_Float, ParksLong_Float, 'Parks')
UserHse_ParksDT = pd.DataFrame(UserHse_ParksDist)

UserHse_PriSchDist = KerwinFunction.Calculate_Hse_Amenities_Dist(UserHseLat_Float, UserHseLong_Float, PriSchLat_Float, PriSchLong_Float, 'Primary School')
UserHse_PriSchDT = pd.DataFrame(UserHse_PriSchDist)

UserHse_SecSchDist = KerwinFunction.Calculate_Hse_Amenities_Dist(UserHseLat_Float, UserHseLong_Float, SecSchLat_Float, SecSchLong_Float, 'Secondary School')
UserHse_SecSchDT = pd.DataFrame(UserHse_SecSchDist)

UserHse_TertairyDist = KerwinFunction.Calculate_Hse_Amenities_Dist(UserHseLat_Float, UserHseLong_Float, TertairyLat_Float, TertairyLong_Float, 'Tertairy')
UserHse_TertairyDT = pd.DataFrame(UserHse_TertairyDist)

UserHse_UniDist = KerwinFunction.Calculate_Hse_Amenities_Dist(UserHseLat_Float, UserHseLong_Float, UniLat_Float, UniLong_Float, 'Uni')
UserHse_UniDT = pd.DataFrame(UserHse_UniDist)

#Filter and get all amenties within 1km radius
DistanceinKM = 1

FilterMDollarHse_FairpriceDT = KerwinFunction.FilterDataTableByDistance(MDollarHse_FairpriceDT, DistanceinKM)
FilterMDollarHse_HosDT = KerwinFunction.FilterDataTableByDistance(MDollarHse_HosDT, DistanceinKM)
FilterMDollarHse_MallsDT = KerwinFunction.FilterDataTableByDistance(MDollarHse_MallsDT, DistanceinKM)
FilterMDollarHse_MRTDT = KerwinFunction.FilterDataTableByDistance(MDollarHse_MRTDT, DistanceinKM)
FilterMDollarHse_ParksDT = KerwinFunction.FilterDataTableByDistance(MDollarHse_ParksDT, DistanceinKM)
FilterMDollarHse_PriSchDT = KerwinFunction.FilterDataTableByDistance(MDollarHse_PriSchDT, DistanceinKM)
FilterMDollarHse_SecSchDT = KerwinFunction.FilterDataTableByDistance(MDollarHse_SecSchDT, DistanceinKM)
FilterMDollarHse_TertairyDT = KerwinFunction.FilterDataTableByDistance(MDollarHse_TertairyDT, DistanceinKM)
FIlterMDollarHse_UniDT = KerwinFunction.FilterDataTableByDistance(MDollarHse_UniDT, DistanceinKM)

FilterUserHse_FairpriceDT = KerwinFunction.FilterDataTableByDistance(UserHse_FairpriceDT, DistanceinKM)
FilterUserHse_HosDT = KerwinFunction.FilterDataTableByDistance(UserHse_HosDT, DistanceinKM)
FilterUserHse_MallsDT = KerwinFunction.FilterDataTableByDistance(UserHse_MallsDT, DistanceinKM)
FilterUserHse_MRTDT = KerwinFunction.FilterDataTableByDistance(UserHse_MRTDT, DistanceinKM)
FilterUserHse_ParksDT = KerwinFunction.FilterDataTableByDistance(UserHse_ParksDT, DistanceinKM)
FilterUserHse_PriSchDT = KerwinFunction.FilterDataTableByDistance(UserHse_PriSchDT, DistanceinKM)
FilterUserHse_SecSchDT = KerwinFunction.FilterDataTableByDistance(UserHse_SecSchDT, DistanceinKM)
FilterUserHse_TertairyDT = KerwinFunction.FilterDataTableByDistance(UserHse_TertairyDT, DistanceinKM)
FIlterUserHse_UniDT = KerwinFunction.FilterDataTableByDistance(UserHse_UniDT, DistanceinKM)

#Convert KM to Meters
FilterMDollarHse_FairpriceDT['Distance(M)'] = FilterMDollarHse_FairpriceDT['Distance (km)'] * 1000
FilterMDollarHse_HosDT['Distance(M)'] = FilterMDollarHse_HosDT['Distance (km)'] * 1000
FilterMDollarHse_MallsDT['Distance(M)'] = FilterMDollarHse_MallsDT['Distance (km)'] * 1000
FilterMDollarHse_MRTDT['Distance(M)'] = FilterMDollarHse_MRTDT['Distance (km)'] * 1000
FilterMDollarHse_ParksDT['Distance(M)'] = FilterMDollarHse_ParksDT['Distance (km)'] * 1000
FilterMDollarHse_PriSchDT['Distance(M)'] = FilterMDollarHse_PriSchDT['Distance (km)'] * 1000
FilterMDollarHse_SecSchDT['Distance(M)'] = FilterMDollarHse_SecSchDT['Distance (km)'] * 1000
FilterMDollarHse_TertairyDT['Distance(M)'] = FilterMDollarHse_TertairyDT['Distance (km)'] * 1000
FIlterMDollarHse_UniDT['Distance(M)'] = FIlterMDollarHse_UniDT['Distance (km)'] * 1000

FilterUserHse_FairpriceDT['Distance(M)'] = FilterUserHse_FairpriceDT['Distance (km)'] * 1000
FilterUserHse_HosDT['Distance(M)'] = FilterUserHse_HosDT['Distance (km)'] * 1000
FilterUserHse_MallsDT['Distance(M)'] = FilterUserHse_MallsDT['Distance (km)'] * 1000
FilterUserHse_MRTDT['Distance(M)'] = FilterUserHse_MRTDT['Distance (km)'] * 1000
FilterUserHse_ParksDT['Distance(M)'] = FilterUserHse_ParksDT['Distance (km)'] * 1000
FilterUserHse_PriSchDT['Distance(M)'] = FilterUserHse_PriSchDT['Distance (km)'] * 1000
FilterUserHse_SecSchDT['Distance(M)'] = FilterUserHse_SecSchDT['Distance (km)'] * 1000
FilterUserHse_TertairyDT['Distance(M)'] = FilterUserHse_TertairyDT['Distance (km)'] * 1000
FIlterUserHse_UniDT['Distance(M)'] = FIlterUserHse_UniDT['Distance (km)'] * 1000
 
#Calculate the points
FilterMDollarHse_FairpriceDT['FairpricePoints'] = Supermarket_MallPoint *( 1 / FilterMDollarHse_FairpriceDT['Distance(M)'])
FilterMDollarHse_HosDT['HosPoints'] = Hospital_ClinicPoint *( 1 / FilterMDollarHse_HosDT['Distance(M)'])
FilterMDollarHse_MallsDT['MallPoints'] = Supermarket_MallPoint *( 1 / FilterMDollarHse_MallsDT['Distance(M)'])
FilterMDollarHse_MRTDT['MRTPoints'] = MRTPoint *( 1 / FilterMDollarHse_MRTDT['Distance(M)'])
FilterMDollarHse_ParksDT['ParksPoints'] = ParksPoint *( 1 / FilterMDollarHse_ParksDT['Distance(M)'])
FilterMDollarHse_PriSchDT['PriSchPoints'] = SchoolsPoint *( 1 / FilterMDollarHse_PriSchDT['Distance(M)'])
FilterMDollarHse_SecSchDT['SecSchPoints'] = SchoolsPoint *( 1 / FilterMDollarHse_SecSchDT['Distance(M)'])
FilterMDollarHse_TertairyDT['TertairyPoints'] = SchoolsPoint *( 1 / FilterMDollarHse_TertairyDT['Distance(M)'])
FIlterMDollarHse_UniDT['UniPoints'] = SchoolsPoint *( 1 / FIlterMDollarHse_UniDT['Distance(M)'])

FilterUserHse_FairpriceDT['FairpricePoints'] = Supermarket_MallPoint *( 1 / FilterUserHse_FairpriceDT['Distance(M)'])
FilterUserHse_HosDT['HosPoints'] = Hospital_ClinicPoint *( 1 / FilterUserHse_HosDT['Distance(M)'])
FilterUserHse_MallsDT['MallPoints'] = Supermarket_MallPoint *( 1 / FilterUserHse_MallsDT['Distance(M)'])
FilterUserHse_MRTDT['MRTPoints'] = MRTPoint *( 1 / FilterUserHse_MRTDT['Distance(M)'])
FilterUserHse_ParksDT['ParksPoints'] = ParksPoint *( 1 / FilterUserHse_ParksDT['Distance(M)'])
FilterUserHse_PriSchDT['PriSchPoints'] = SchoolsPoint *( 1 / FilterUserHse_PriSchDT['Distance(M)'])
FilterUserHse_SecSchDT['SecSchPoints'] = SchoolsPoint *( 1 / FilterUserHse_SecSchDT['Distance(M)'])
FilterUserHse_TertairyDT['TertairyPoints'] = SchoolsPoint *( 1 / FilterUserHse_TertairyDT['Distance(M)'])
FIlterUserHse_UniDT['UniPoints'] = SchoolsPoint *( 1 / FIlterUserHse_UniDT['Distance(M)'])


#Group the amenties points to the coordinates 
MDollarHse_FairpricePoint = FilterMDollarHse_FairpriceDT.groupby('Coordinates')['FairpricePoints'].sum().reset_index()
MDollarHse_HosPoint = FilterMDollarHse_HosDT.groupby('Coordinates')['HosPoints'].sum().reset_index()
MDollarHse_MallsPoint = FilterMDollarHse_MallsDT.groupby('Coordinates')['MallPoints'].sum().reset_index()
MDollarHse_MRTPoint = FilterMDollarHse_MRTDT.groupby('Coordinates')['MRTPoints'].sum().reset_index()
MDollarHse_ParksPoint = FilterMDollarHse_ParksDT.groupby('Coordinates')['ParksPoints'].sum().reset_index()
MDollarHse_PriSchPoint = FilterMDollarHse_PriSchDT.groupby('Coordinates')['PriSchPoints'].sum().reset_index()
MDollarHse_SecSchPoint = FilterMDollarHse_SecSchDT.groupby('Coordinates')['SecSchPoints'].sum().reset_index()
MDollarHse_TertairyPoint = FilterMDollarHse_TertairyDT.groupby('Coordinates')['TertairyPoints'].sum().reset_index()
MDollarHse_UniPoint = FIlterMDollarHse_UniDT.groupby('Coordinates')['UniPoints'].sum().reset_index()

UserHse_FairpricePoint = FilterUserHse_FairpriceDT.groupby('Coordinates')['FairpricePoints'].sum().reset_index()
UserHse_HosPoint = FilterUserHse_HosDT.groupby('Coordinates')['HosPoints'].sum().reset_index()
UserHse_MallsPoint = FilterUserHse_MallsDT.groupby('Coordinates')['MallPoints'].sum().reset_index()
UserHse_MRTPoint = FilterUserHse_MRTDT.groupby('Coordinates')['MRTPoints'].sum().reset_index()
UserHse_ParksPoint = FilterUserHse_ParksDT.groupby('Coordinates')['ParksPoints'].sum().reset_index()
UserHse_PriSchPoint = FilterUserHse_PriSchDT.groupby('Coordinates')['PriSchPoints'].sum().reset_index()
UserHse_SecSchPoint = FilterUserHse_SecSchDT.groupby('Coordinates')['SecSchPoints'].sum().reset_index()
UserHse_TertairyPoint = FilterUserHse_TertairyDT.groupby('Coordinates')['TertairyPoints'].sum().reset_index()
UserHse_UniPoint = FIlterUserHse_UniDT.groupby('Coordinates')['UniPoints'].sum().reset_index()

#Mergae the dataframe into 1
MDollarHSe_Meraged_Points = MDollarHse_FairpricePoint.merge(MDollarHse_HosPoint, on='Coordinates', how='outer')
MDollarHSe_Meraged_Points = MDollarHSe_Meraged_Points.merge(MDollarHse_MallsPoint, on='Coordinates', how='outer')
MDollarHSe_Meraged_Points = MDollarHSe_Meraged_Points.merge(MDollarHse_MRTPoint, on='Coordinates', how='outer')
MDollarHSe_Meraged_Points = MDollarHSe_Meraged_Points.merge(MDollarHse_ParksPoint, on='Coordinates', how='outer')
MDollarHSe_Meraged_Points = MDollarHSe_Meraged_Points.merge(MDollarHse_PriSchPoint, on='Coordinates', how='outer')
MDollarHSe_Meraged_Points = MDollarHSe_Meraged_Points.merge(MDollarHse_SecSchPoint, on='Coordinates', how='outer')
MDollarHSe_Meraged_Points = MDollarHSe_Meraged_Points.merge(MDollarHse_TertairyPoint, on='Coordinates', how='outer')
MDollarHSe_Meraged_Points = MDollarHSe_Meraged_Points.merge(MDollarHse_UniPoint, on='Coordinates', how='outer')

UserHse_Meraged_Points = UserHse_FairpricePoint.merge(UserHse_HosPoint, on='Coordinates', how='outer')
UserHse_Meraged_Points = UserHse_Meraged_Points.merge(UserHse_MallsPoint, on='Coordinates', how='outer')
UserHse_Meraged_Points = UserHse_Meraged_Points.merge(UserHse_MRTPoint, on='Coordinates', how='outer')
UserHse_Meraged_Points = UserHse_Meraged_Points.merge(UserHse_ParksPoint, on='Coordinates', how='outer')
UserHse_Meraged_Points = UserHse_Meraged_Points.merge(UserHse_PriSchPoint, on='Coordinates', how='outer')
UserHse_Meraged_Points = UserHse_Meraged_Points.merge(UserHse_SecSchPoint, on='Coordinates', how='outer')
UserHse_Meraged_Points = UserHse_Meraged_Points.merge(UserHse_TertairyPoint, on='Coordinates', how='outer')
UserHse_Meraged_Points = UserHse_Meraged_Points.merge(UserHse_UniPoint, on='Coordinates', how='outer')

#Replace empty values with 0 
MDollarHSe_Meraged_Points['FairpricePoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
MDollarHSe_Meraged_Points['HosPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
MDollarHSe_Meraged_Points['MallPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
MDollarHSe_Meraged_Points['MRTPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
MDollarHSe_Meraged_Points['ParksPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
MDollarHSe_Meraged_Points['PriSchPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
MDollarHSe_Meraged_Points['SecSchPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
MDollarHSe_Meraged_Points['TertairyPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
MDollarHSe_Meraged_Points['UniPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)

UserHse_Meraged_Points['FairpricePoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
UserHse_Meraged_Points['HosPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
UserHse_Meraged_Points['MallPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
UserHse_Meraged_Points['MRTPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
UserHse_Meraged_Points['ParksPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
UserHse_Meraged_Points['PriSchPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
UserHse_Meraged_Points['SecSchPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
UserHse_Meraged_Points['TertairyPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
UserHse_Meraged_Points['UniPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)

#Calculate the total points starting from the thrid column
MDollarHSe_Meraged_Points['Total_Points'] = MDollarHSe_Meraged_Points.iloc[:, 2:].sum(axis=1)
UserHse_Meraged_Points['Total_Points'] = UserHse_Meraged_Points.iloc[:, 2:].sum(axis=1)

#calculate average points
MDollar_AveragePoint = MDollarHSe_Meraged_Points['Total_Points'].mean()

print("Average point for the Million Dollar House is: " + str(MDollar_AveragePoint))

##Compare all the user address points towards the average points and get those above average out.
Filtered_UserHse = UserHse_Meraged_Points[UserHse_Meraged_Points['Total_Points'] > MDollar_AveragePoint]

#pass the dataframe into a CSV file
MDollarHSe_Meraged_Points.to_csv('ProjTest\\Excel Data\\FilteredMillionDollarHse.csv', index=True)
Filtered_UserHse.to_csv('ProjTest\\Excel Data\\FilteredUserHse.csv', index=True)
