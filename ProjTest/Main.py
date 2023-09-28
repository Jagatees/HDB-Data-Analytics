import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import KerwinFunction
from statistics import mean
from sklearn.linear_model import LinearRegression

root = tk.Tk()
root.geometry('1000x600')
root.title('Test Side Nav')

#Function to show home page
def Home_Page():
    Home_frame = tk.Frame(main_frame)
    #Code here for Home page

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
    UserHseFilePath = 'ProjTest\Excel Data\DummyUserAddress.csv'

    #Dummy user add
    UserAddress = "443A Fernvale Road" #NO unit number, NO postal code
    UserArea = "Sengkang"

    #Amenties Points
    Hospital_ClinicPoint = 5
    SchoolsPoint = 4
    MRTPoint = 3
    Supermarket_MallPoint = 2
    ParksPoint = 1

    #convert user address into long and lat
    UserCoordinates = KerwinFunction.GetLongLatFromAddress(UserAddress).split(",")
    UserLong = UserCoordinates[1].strip()
    UserLat = UserCoordinates[0].strip()

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

    ###Million Dollar Hse to Admenties###

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

    #Filter and get all amenties within 0.5km radius
    DistanceinKM = 0.5

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

    """
    ###User Address to Admenties###
    #Calculate Distance between user and all Fairprice
    User_FairpriceDistResult = []

    for lat2, lon2 in zip(FairpriceLat, FairpriceLong):
        distance_km = KerwinFunction.DistanceBetween2Coordinates(float(UserLat), float(UserLong), float(lat2), float(lon2))
        User_FairpriceDistResult.append({'Table_Name': 'User_FairpriceDist', 'Latitude': lat2, 'Longitude': lon2, 'Distance (km)': distance_km})

    User_FairpriceDistDT = pd.DataFrame(User_FairpriceDistResult)

    #Calculate Distance between user and all Hospital/Clinic
    User_HospitalClinicDistResult = []

    for lat2, lon2 in zip(HospitalLat, HospitalLong):
        distance_km = KerwinFunction.DistanceBetween2Coordinates(float(UserLat), float(UserLong), float(lat2), float(lon2))
        User_HospitalClinicDistResult.append({'Table_Name': 'User_HospitalCLinicDist', 'Latitude': lat2, 'Longitude': lon2, 'Distance (km)': distance_km})

    User_HospitalClinicDistDT = pd.DataFrame(User_HospitalClinicDistResult)

    #Calculate Distance between user and all Malls
    User_MallsDistResult = []

    for lat2, lon2 in zip(MallsLat, MallsLong):
        distance_km = KerwinFunction.DistanceBetween2Coordinates(float(UserLat), float(UserLong), float(lat2), float(lon2))
        User_MallsDistResult.append({'Table_Name': 'User_MallsDist', 'Latitude': lat2, 'Longitude': lon2, 'Distance (km)': distance_km})

    User_MallsDistDT = pd.DataFrame(User_MallsDistResult)

    #Calculate Distance between user and all MRT
    User_MRTDistResult = []

    for lat2, lon2 in zip(MRTLat, MRTLong):
        distance_km = KerwinFunction.DistanceBetween2Coordinates(float(UserLat), float(UserLong), float(lat2), float(lon2))
        User_MRTDistResult.append({'Table_Name': 'User_MRTDist', 'Latitude': lat2, 'Longitude': lon2, 'Distance (km)': distance_km})

    User_MRTDistDT = pd.DataFrame(User_MRTDistResult)

    #Calculate Distance between user and all Parks
    User_ParksDistResult = []

    for lat2, lon2 in zip(ParksLat, ParksLong):
        distance_km = KerwinFunction.DistanceBetween2Coordinates(float(UserLat), float(UserLong), float(lat2), float(lon2))
        User_ParksDistResult.append({'Table_Name': 'User_ParksDist', 'Latitude': lat2, 'Longitude': lon2, 'Distance (km)': distance_km})

    User_ParksDistDT = pd.DataFrame(User_ParksDistResult)

    #Calculate Distance between user and all Primary school
    User_PriSchDistResult = []

    for lat2, lon2 in zip(PriSchLat, PriSchLong):
        distance_km = KerwinFunction.DistanceBetween2Coordinates(float(UserLat), float(UserLong), float(lat2), float(lon2))
        User_PriSchDistResult.append({'Table_Name': 'User_PriSchDist', 'Latitude': lat2, 'Longitude': lon2, 'Distance (km)': distance_km})

    User_PriSchDistDT = pd.DataFrame(User_PriSchDistResult)

    #Calculate Distance between user and all Secondary School
    User_SecSchDistResult = []

    for lat2, lon2 in zip(SecSchLat, SecSchLong):
        distance_km = KerwinFunction.DistanceBetween2Coordinates(float(UserLat), float(UserLong), float(lat2), float(lon2))
        User_SecSchDistResult.append({'Table_Name': 'User_SecSchDist', 'Latitude': lat2, 'Longitude': lon2, 'Distance (km)': distance_km})

    User_SecSchDistDT = pd.DataFrame(User_SecSchDistResult)

    #Calculate Distance between user and all Tertairy School
    User_TertairyDistResult = []

    for lat2, lon2 in zip(TertairyLat, TertairyLong):
        distance_km = KerwinFunction.DistanceBetween2Coordinates(float(UserLat), float(UserLong), float(lat2), float(lon2))
        User_TertairyDistResult.append({'Table_Name': 'User_TertiaryDist', 'Latitude': lat2, 'Longitude': lon2, 'Distance (km)': distance_km})

    User_TertiaryDistDT = pd.DataFrame(User_TertairyDistResult)

    #Calculate Distance between user and all Uni
    User_UniDistResult = []

    for lat2, lon2 in zip(UniLat, UniLong):
        distance_km = KerwinFunction.DistanceBetween2Coordinates(float(UserLat), float(UserLong), float(lat2), float(lon2))
        User_UniDistResult.append({'Table_Name': 'User_UniDist', 'Latitude': lat2, 'Longitude': lon2, 'Distance (km)': distance_km})

    User_UniDistDT = pd.DataFrame(User_UniDistResult)

    UserDistanceinKM = 1.0
    FilterFairpriceDistDT = KerwinFunction.FilterDataTableByDistance(User_FairpriceDistDT, UserDistanceinKM)
    FilterHosClinicDistDT = KerwinFunction.FilterDataTableByDistance(User_HospitalClinicDistDT, UserDistanceinKM)
    FilterMallDistDT = KerwinFunction.FilterDataTableByDistance(User_MallsDistDT, UserDistanceinKM)
    FilterMRTDistDT = KerwinFunction.FilterDataTableByDistance(User_MRTDistDT, UserDistanceinKM)
    FilterParkDistDT = KerwinFunction.FilterDataTableByDistance(User_ParksDistDT, UserDistanceinKM)
    FilterPriSchDistDT = KerwinFunction.FilterDataTableByDistance(User_PriSchDistDT, UserDistanceinKM)
    FilterSecSchDistDT = KerwinFunction.FilterDataTableByDistance(User_SecSchDistDT, UserDistanceinKM)
    FilterTertiaryDistDT = KerwinFunction.FilterDataTableByDistance(User_TertiaryDistDT, UserDistanceinKM)
    FIlterUniDistDT = KerwinFunction.FilterDataTableByDistance(User_UniDistDT, UserDistanceinKM)

    FilterFairpriceCount = "There are " + str(len(FilterFairpriceDistDT)) + " Fairprice within 1km from the address\n"
    FilterHosClinicCount = "There are " + str(len(FilterHosClinicDistDT)) + " Hospital or clinic within 1km from the address\n"
    FilterMallsCount = "There are " + str(len(FilterMallDistDT)) + " Malls within 1km from the address\n"
    FilterMRTCount = "There are " + str(len(FilterMRTDistDT)) + " MRT within 1km from the address\n"
    FilterParkCount = "There are " + str(len(FilterParkDistDT)) + " Park within 1km from the address\n"
    FilterPriSchCount = "There are " + str(len(FilterPriSchDistDT)) + " Primary School within 1km from the address\n"
    FilterSecSchCount = "There are " + str(len(FilterSecSchDistDT)) + " Secondary School within 1km from the address\n"
    FilterTertiaryCount = "There are " + str(len(FilterTertiaryDistDT)) + " Tertiary School within 1km from the address\n"
    FIlterUniCount = "There are " + str(len(FIlterUniDistDT)) + " Universities within 1km from the address"

    #print(FilterFairpriceCount + FilterHosClinicCount + FilterMallsCount + FilterMRTCount + FilterParkCount + FilterPriSchCount + FilterSecSchCount + FilterTertiaryCount + FIlterUniCount)
    User_TotalPoint = int(len(FilterFairpriceDistDT)) + int(len(FilterHosClinicDistDT)) + int(len(FilterMallDistDT)) + int(len(FilterMRTDistDT)) + int(len(FilterParkDistDT)) + int(len(FilterPriSchDistDT)) + int(len(FilterSecSchDistDT)) + int(len(FilterTertiaryDistDT)) + int(len(FIlterUniDistDT))
    print("User total point is: " + str(User_TotalPoint))

    """
    lb = tk.Label(Home_frame, text='Home \npage', font=('Bold', 30))
    lb.pack()

    Home_frame.pack(pady=20)

#Function to show Upload page 
def Upload_Page():
    Upload_frame = tk.Frame(main_frame)

    #Code here for Upload page
    FilePath = ""
    ColList = ""

    #Store address in this array
    AddressArray = []
    
    lb = tk.Label(Upload_frame, text='Upload \npage', font=('Bold', 30))
    lb.pack()

    label3_text = tk.StringVar()
    label3_text.set("PENDING LOCATION")
    AddressDataFrame = pd.DataFrame()

    def getfiledirectory():
        filenames = filedialog.askopenfilenames()
        if filenames:
            #print("Selected files:")
            for filename in filenames:
                print(filename)
                label3_text.set(filenames[0])
                FilePath = filenames[0]
        else:
            label3_text.set('No File got')
        
        #Read CSV File
        TestAddressCSV = pd.read_csv(FilePath, header=None)
        TestAddressCSV.columns = ['Location_Name', 'Location_Type', 'Blk_No' ,'Address', 'Postal_Code', 'Full_Address', 'Long', 'Lat']
        TestAddressCSV = TestAddressCSV.drop(0)
        # Iterate through the DataFrame
        for index, row in TestAddressCSV.iterrows():
            # Extract values from the two columns and concatenate them

            value1 = row['Blk_No']
            value2 = row['Address']
            concatenated = str(value1) + " " + str(value2)  # Convert to string if not already

            # Append the concatenated value to the list
            AddressArray.append(concatenated)

        print(AddressArray)

    def GetLongLatFromAddress():
        #LocationIQ API key
        api_key = "pk.02ff73880ec7a133cfe62191e54c3bd1"

        # Initialize an empty list to store the coordinates
        coordinatesLong = []
        coordinatesLat = []

        # Iterate through the addresses and convert them to coordinates
        for address in AddressArray:
            # Construct the API request URL
            url = f"https://us1.locationiq.com/v1/search.php?key={api_key}&q={address}&format=json"
            
            try:
                # Make the API request
                response = requests.get(url)

                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    # Parse the JSON response
                    data = response.json()

                    if data:
                        # Extract and append the latitude and longitude to the coordinates list
                        latitude = data[0]["lat"]
                        longitude = data[0]["lon"]
                        coordinatesLong.append((longitude))
                        coordinatesLat.append((latitude))
                        
                    else:
                        print(f"Location not found for address: {address}")
                else:
                    print(f"Error: Unable to access the LocationIQ API for address: {address}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")

        #Store data back into excel
        File = label3.cget("text")
        AddressDataFrame = pd.read_csv(File, header=None)
        AddressDataFrame.columns = ['Location_Name', 'Location_Type', 'Blk_No' ,'Address', 'Postal_Code', 'Full_Address', 'Long', 'Lat']
        AddressDataFrame = AddressDataFrame.drop(0)

        AddressDataFrame['Long'] = coordinatesLong
        AddressDataFrame['Lat'] = coordinatesLat

        AddressDataFrame.to_csv(File, index=False)
        print("Generate Sucessful")

    button = tk.Button(Upload_frame, text="Browse", command=getfiledirectory)
    label2 = tk.Label(Upload_frame, text="File Location :")
    label3 = tk.Label(Upload_frame, textvariable=label3_text)  
 
    ShowGraphBtn = tk.Button(Upload_frame, text="Generate Long&Lat", command=GetLongLatFromAddress)

    label3_text.set("") 

    button.pack(expand=True, fill='both', pady=20)
    label2.pack()
    label3.pack()
    ShowGraphBtn.pack()

    Upload_frame.pack(pady=20)

#Function to show Analytics page
def Analytics_Page():
    Analytics_frame = tk.Frame(main_frame)
    #Code here for Analytics page
    csv_file = 'ProjTest\Excel Data\TestRentalData.csv'
    TestRentalCSV = pd.read_csv(csv_file, header=None)

    #Clean data
    Col_ToClean = [2]
    for column in Col_ToClean:
        TestRentalCSV[column] = TestRentalCSV[column].str.replace('$', '').str.replace(',', '')

    #Take only selected col
    TestRentalCSV = TestRentalCSV[[1, 2, 3, 4]]
    #Change col name
    TestRentalCSV.columns = ['Year', 'Price', 'Type' ,'Area']
    #Drop first row
    TestRentalCSV = TestRentalCSV.drop(0)
    #Save dataframe into new csv file
    TestRentalCSV.to_csv('ProjTest\Excel Data\Cleaned_Rent.csv', index=False)
    #print(TestRentalCSV)
    
    #Get unique value from a col
    AreaNames = TestRentalCSV['Area'].unique().tolist()
    unique_Year = TestRentalCSV['Year'].unique().tolist()
    #Filter_DF = pd.DataFrame()
    #TestAreaName = []

    def ShowGraph():
        #Create empty list
        TestAreaName = [Y1parameters_combobox.get(), Y2parameters_combobox.get()]

        FilterResult_List = []
        for year in unique_Year:
            for FilterColName in TestAreaName:
                FilterTypeofRent = 'Room for Rent'
                #YearRent = '2023'
                FilterRentalCol = TestRentalCSV.copy()
                FilterRentalCol = FilterRentalCol[FilterRentalCol['Year'].str.contains(year) & FilterRentalCol['Type'].str.contains(FilterTypeofRent) & FilterRentalCol['Area'].str.contains(FilterColName) ]

                # Check if the df is empty
                if not FilterRentalCol.empty:
                    AverageRentList = list(FilterRentalCol['Price'])
                    RentList = [eval(x) for x in AverageRentList]
                    
                    # Calculate the average rent
                    AverageRent = round(sum(RentList) / len(RentList), 2)
                    
                    # Append the location and average rent to the FilterResult_List
                    FilterResult_List.append((year, FilterColName, AverageRent))

        #Store FilterResult_List in a dataframe
        Filter_DF = pd.DataFrame(FilterResult_List, columns=['Year','Location','Average_Price'])
        #print(Filter_DF)

        fig, ax = plt.subplots()

        for location, location_data in Filter_DF.groupby('Location'):
            ax.plot(location_data['Year'], location_data['Average_Price'], label=location)

        ax.set_xlabel('Year')
        ax.set_ylabel('Average Price')
        ax.set_title('Line Chart')
        
        canvas = FigureCanvasTkAgg(fig, Analytics_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side="left", expand=False)
        ax.legend()

        #Data prediction
        Predict_DF = Filter_DF.copy()
        print(Predict_DF)

        Predicted_Data = Predict_DF[Predict_DF['Location'] == Y1parameters_combobox.get()]

        PredictX = Predicted_Data[['Year']]
        PredictY = Predicted_Data[['Average_Price']]

        model = LinearRegression()

        model.fit(PredictX, PredictY)

        Predict_2024 = [[2024]]
        predicted_price = model.predict(Predict_2024)[0]

        print(predicted_price)

    #Take col name and store in dropdown 
    label4 = tk.Label(Analytics_frame, text="Y1 axis: ")
    Y1parameter_choices = AreaNames
    selected_parameters = tk.StringVar()
    Y1parameters_combobox = ttk.Combobox(Analytics_frame, textvariable=selected_parameters, values=Y1parameter_choices)
    selected_parameters.set("Please select")

    label5 = tk.Label(Analytics_frame, text="Y2 axis: ")
    Y2parameter_choices = AreaNames
    selected_parameters = tk.StringVar()
    Y2parameters_combobox = ttk.Combobox(Analytics_frame, textvariable=selected_parameters, values=Y2parameter_choices)
    selected_parameters.set("Please select")  # Set the default selection

    ShowGraphBtn = tk.Button(Analytics_frame, text="Show Graph", command=ShowGraph)

    label4.pack(side='left') 
    Y1parameters_combobox.pack(side='left', padx=5) 
    label5.pack(side='left') 
    Y2parameters_combobox.pack(side='left', padx=5)
    ShowGraphBtn.pack()

    Analytics_frame.pack(pady=20)




#Function to show Data page
def Data_Page():
    Data_frame = tk.Frame(main_frame)

    #Code here for Data page
    csv_file = 'ProjTest\Excel Data\TestRentalData.csv'
    TestRentalCSV = pd.read_csv(csv_file, header=None)

    #Clean data
    Col_ToClean = [2]
    for column in Col_ToClean:
        TestRentalCSV[column] = TestRentalCSV[column].str.replace('$', '').str.replace(',', '')

    #Take only selected col
    TestRentalCSV = TestRentalCSV[[1, 2, 3, 4]]
    #Change col name
    TestRentalCSV.columns = ['Year', 'Price', 'Type' ,'Area']
    #Drop first row
    TestRentalCSV = TestRentalCSV.drop(0)
    #Save dataframe into new csv file
    TestRentalCSV.to_csv('ProjTest\Excel Data\Cleaned_Rent.csv', index=False)
    #print(TestRentalCSV)
    
    #Get unique value from a col
    AreaNames = TestRentalCSV['Area'].unique().tolist()
    unique_Year = TestRentalCSV['Year'].unique().tolist()
    #Filter_DF = pd.DataFrame()
    #TestAreaName = []

    def ShowGraph():
        #Create empty list
        TestAreaName = Y1parameters_combobox.get()

        FilterResult_List = []
        for year in unique_Year:
            FilterTypeofRent = 'Room for Rent'
            #YearRent = '2023'
            FilterRentalCol = TestRentalCSV.copy()
            FilterRentalCol = FilterRentalCol[FilterRentalCol['Year'].str.contains(year) & FilterRentalCol['Type'].str.contains(FilterTypeofRent) & FilterRentalCol['Area'].str.contains(TestAreaName) ]

            # Check if the df is empty
            if not FilterRentalCol.empty:
                AverageRentList = list(FilterRentalCol['Price'])
                RentList = [eval(x) for x in AverageRentList]
                    
                # Calculate the average rent
                AverageRent = round(sum(RentList) / len(RentList), 2)
                    
                # Append the location and average rent to the FilterResult_List
                FilterResult_List.append((year, TestAreaName, AverageRent))

        #Store FilterResult_List in a dataframe
        Filter_DF = pd.DataFrame(FilterResult_List, columns=['Year','Location','Average_Price'])
        #print(Filter_DF)

        #Data prediction
        Predict_DF = Filter_DF.copy()
        #print(Predict_DF)

        Predicted_Data = Predict_DF[Predict_DF['Location'] == Y1parameters_combobox.get()]

        PredictX = Predicted_Data[['Year']]
        PredictY = Predicted_Data[['Average_Price']]

        model = LinearRegression()

        model.fit(PredictX, PredictY)

        Predict_2024 = [[2024]]
        predicted_price = model.predict(Predict_2024)[0]

        Price_Predicted = float(predicted_price)

        #Plotting Graph with predicted values
        Xaxis = [int(Data_Year) for Data_Year in Predicted_Data['Year'].values]
        Yaxis = Predicted_Data['Average_Price']
        Predict_Year = 2024

        #Creat new array to store predicted year tgt with the rest and used it to set the range of X axis
        Xaxis_Array = Predicted_Data['Year'].values
        Xaxis_Array = np.append(Xaxis_Array, str(Predict_Year))
        Xaxis_Range = [int(XaxisA) for XaxisA in Xaxis_Array]

        fig, ax = plt.subplots()

        ax.plot(Xaxis, Yaxis, marker='o', linestyle='-', label='Historical Data')
        ax.plot(Predict_Year, Price_Predicted, marker='o', color='red', linestyle='-', label=f'Predicted Price: {Price_Predicted:.2f}')
        ax.set_xticks(Xaxis_Range)
        ax.set_xlabel('Year')
        ax.set_ylabel('Average Price')
        ax.set_title('Line Chart')
        
        canvas = FigureCanvasTkAgg(fig, Data_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side="left", expand=False)
        ax.legend()


    #Take col name and store in dropdown 
    label4 = tk.Label(Data_frame, text="Y1 axis: ")
    Y1parameter_choices = AreaNames
    selected_parameters = tk.StringVar()
    Y1parameters_combobox = ttk.Combobox(Data_frame, textvariable=selected_parameters, values=Y1parameter_choices)
    selected_parameters.set("Please select")

    ShowGraphBtn = tk.Button(Data_frame, text="Show Graph", command=ShowGraph)

    label4.pack(side='left') 
    Y1parameters_combobox.pack(side='left', padx=5) 
    ShowGraphBtn.pack()

    Data_frame.pack(pady=20)

#Function to change Label Color so that it will be hidden at first
def hide_Label():
    HomeLBL.config(bg='#c3c3c3')
    UploadLBL.config(bg='#c3c3c3')
    AnalyticsLBL.config(bg='#c3c3c3')
    DataLBL.config(bg='#c3c3c3')
    
#Funtion to delete the frame before showing new one
def Delete_Frame():
    for frame in main_frame.winfo_children():
        frame.destroy()

#Function to change Label Color so that it will be shown on click
def indicate(lb, page):
    hide_Label()
    lb.config(bg='#158aff')
    Delete_Frame()
    page()

#Side Nav

options_frame = tk.Frame(root, bg='#c3c3c3')

#1st Button Home 
#On button click Label and page will show
HomeBTN = tk.Button(options_frame, text='Home', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', 
                         command=lambda: indicate(HomeLBL, Home_Page))
HomeBTN.place(x=8, y=80)

#To show user they at Dashboard page
HomeLBL = tk.Label(options_frame, text='', bg='#c3c3c3')
HomeLBL.place(x=3, y=80, width=5, height=37)

#2nd Button Upload
#On button click Label and page will show
UploadBTN = tk.Button(options_frame, text='Upload', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', 
                         command=lambda: indicate(UploadLBL, Upload_Page))
UploadBTN.place(x=8, y=160)

#To show user they at Upload page
UploadLBL = tk.Label(options_frame, text='', bg='#c3c3c3')
UploadLBL.place(x=3, y=160, width=5, height=37)

#3rd Button Analytics
#On button click Label and page will show
AnalyticsBTN = tk.Button(options_frame, text='Analytics', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', 
                         command=lambda: indicate(AnalyticsLBL, Analytics_Page))
AnalyticsBTN.place(x=8, y=240)

#To show user they at Analytics page
AnalyticsLBL = tk.Label(options_frame, text='', bg='#c3c3c3')
AnalyticsLBL.place(x=3, y=240, width=5, height=37)

#4th Button Data
#On button click Label and page will show
DataBTN = tk.Button(options_frame, text='Data', font=('Bold', 15), fg='#158aff', bd=0, bg='#c3c3c3', 
                         command=lambda: indicate(DataLBL, Data_Page))
DataBTN.place(x=8, y=320)

#To show user they at Data page
DataLBL = tk.Label(options_frame, text='', bg='#c3c3c3')
DataLBL.place(x=3, y=320, width=5, height=37)

#Make the nav frame align left 
options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=100, height=600)


#Main Frame

main_frame = tk.Frame(root, highlightbackground='black', highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=600, width=1000)

root.mainloop()