import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as py
import json
import csv
from statistics import mean

from data import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data


root = tk.Tk()
root.geometry('1000x600')
root.title('Test Side Nav')

#Function to show home page
def Home_Page():
    Home_frame = tk.Frame(main_frame)
    #Code here for Home page
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
    TestRentalCSV.to_csv('ProjTest\Excel Data\Cleaned_Rent_2022.csv', index=False)
    #print(TestRentalCSV)
    
    #Get unique value from a col
    AreaNames = TestRentalCSV['Area'].unique().tolist()
    unique_Year = TestRentalCSV['Year'].unique().tolist()

    #Create empty list
    FilterResult_List = []
    for year in unique_Year:
        for FilterColName in AreaNames:
            FilterTypeofRent = 'Room for Rent'
            #YearRent = '2023'
            FilterRentalCol = TestRentalCSV.copy()
            FilterRentalCol = FilterRentalCol[FilterRentalCol['Year'].str.contains(year) & FilterRentalCol['Area'].str.contains(FilterColName) & FilterRentalCol['Type'].str.contains(FilterTypeofRent)]

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
    print(Filter_DF)
    
    lb = tk.Label(Home_frame, text='Home \npage', font=('Bold', 30))
    lb.pack()
    Home_frame.pack(pady=20)

#Function to show Upload page 
def Upload_Page():
    Upload_frame = tk.Frame(main_frame)

    lb = tk.Label(Upload_frame, text='Upload \npage', font=('Bold', 30))
    lb.pack()
    Upload_frame.pack(pady=20)

#Function to show Analytics page
def Analytics_Page():
    Analytics_frame = tk.Frame(main_frame)
   
    lb = tk.Label(Analytics_frame, text='Analytics \npage', font=('Bold', 30))
    lb.pack()

    Analytics_frame.pack(pady=20)

#Function to show Data page
def Data_Page():
    Data_frame = tk.Frame(main_frame)

    #Code here for Data page
    lb = tk.Label(Data_frame, text='Data page', font=('Bold', 30))
    lb.pack()

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