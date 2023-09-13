import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as py
import json
from statistics import mean
from sklearn.linear_model import LinearRegression

from data import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data


root = tk.Tk()
root.geometry('1000x600')
root.title('Test Side Nav')
TestDataCSV = pd.read_csv("ProjTest\Excel Data\TestRentalData.csv", header=None)

#Function to show home page
def Home_Page():
    Home_frame = tk.Frame(main_frame)
    #Code here for Home page

    lb = tk.Label(Home_frame, text='Home \npage', font=('Bold', 30))
    lb.pack()

    Home_frame.pack(pady=20)

#Function to show Upload page 
def Upload_Page():
    Upload_frame = tk.Frame(main_frame)

    #Code here for Upload page
    FilePath = ""
    ColList = ""
    
    lb = tk.Label(Upload_frame, text='Upload \npage', font=('Bold', 30))
    lb.pack()

    label3_text = tk.StringVar()
    label3_text.set("PENDING LOCATION")

    def getfiledirectory():
        filenames = filedialog.askopenfilenames()
        if filenames:
            print("Selected files:")
            for filename in filenames:
                print(filename)
                label3_text.set(filenames[0])
                FilePath = filenames[0]
        else:
            label3_text.set('No File got')

    def ShowGraph():
        #Read JSON File
        Scamdata = pd.read_json(label3.cget("text"))
        Years = [i["Year"] for i in Scamdata["Scam"]]
        Amt = [i["Amt Fallen"] for i in Scamdata["Scam"]]

        fig, ax = plt.subplots(figsize=(10,7))
        ax.bar(Years,Amt, color='maroon')
        ax.set_xlim(xmin=0.0)
        ax.set_xlabel('Years',fontsize=14)
        ax.set_ylabel('Amt Fallen to Scam',fontsize=14)
        ax.set_title('Test Graph from JSON',fontsize=14)

        canvas1 = FigureCanvasTkAgg(fig, Upload_frame)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side="left", expand=False)

    button = tk.Button(Upload_frame, text="Browse", command=getfiledirectory)
    label2 = tk.Label(Upload_frame, text="File Location :")
    label3 = tk.Label(Upload_frame, textvariable=label3_text)  
 
    ShowGraphBtn = tk.Button(Upload_frame, text="Show Graph", command=ShowGraph)

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
        Xaxis = Predicted_Data['Year']
        Yaxis = Predicted_Data['Average_Price']
        print(Xaxis)

        fig, ax = plt.subplots()

        for years, Predicted_Data in Predict_DF.groupby('Year'):
            ax.plot(Predicted_Data['Year'], Predicted_Data['Average_Price'], label=years)

        #ax.plot(Xaxis, Yaxis, marker='o', label='Historical Data')

        ax.plot(2024, Price_Predicted, marker='o', color='red', label=f'Predicted Price: {Price_Predicted:.2f}')
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