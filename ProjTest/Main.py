import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
import numpy as py
import json

from data import sales_data, inventory_data, product_data, sales_year_data, inventory_month_data


root = tk.Tk()
root.geometry('1000x600')
root.title('Test Side Nav')
TestDataCSV = pd.read_csv("ProjTest\Excel Data\Test Data.csv", header=None)

#Function to show home page
def Home_Page():
    Home_frame = tk.Frame(main_frame)
    #Code here for Home page
    rowcount  = 0
    rowcount = TestDataCSV.shape[0] - 1
    Xaxis = TestDataCSV[0]
    Yaxis = TestDataCSV[1]

    lb = tk.Label(Home_frame, text='Home \npage\n There are ' + str(rowcount) + " column in the csv file ", font=('Bold', 30))
    lb.pack()

    fig, ax = plt.subplots(figsize=(10,7))
    ax.bar(Xaxis,Yaxis)
    ax.set_xlim(xmin=0.0)
    ax.set_xlabel('Name',fontsize=14)
    ax.set_ylabel('Age',fontsize=14)
    ax.set_title('Test Graph from CSV',fontsize=14)


    canvas = FigureCanvasTkAgg(fig, Home_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side="left", expand=False)

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
        #ColList = Scamdata.columns.values.tolist()
        #print (ColList)

        #Read CSV File
        #ReadCSV = pd.read_csv(label3.cget("text"), header=None)
        #Years = ReadCSV[0]
        #Amt = ReadCSV[1]

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
 

    label4 = tk.Label(Upload_frame, text="X axis: ")
    Xparameter_choices = ["Website 1", "Website 2", "Website 3"]
    selected_parameters = tk.StringVar()
    Xparameters_combobox = ttk.Combobox(Upload_frame, textvariable=selected_parameters, values=Xparameter_choices)
    selected_parameters.set(Xparameter_choices[0])  # Set the default selection

    label5 = tk.Label(Upload_frame, text="Y axis: ")
    Yparameter_choices = ["Website 1", "Website 2", "Website 3"] 
    selected_parameters = tk.StringVar()
    Yparameters_combobox = ttk.Combobox(Upload_frame, textvariable=selected_parameters, values=Yparameter_choices)
    selected_parameters.set(Yparameter_choices[0])  # Set the default selection

    ShowGraphBtn = tk.Button(Upload_frame, text="Show Graph", command=ShowGraph)

    label3_text.set("") 

    button.pack(expand=True, fill='both', pady=20)
    label2.pack()
    label3.pack()
    label4.pack(side='left') 
    Xparameters_combobox.pack(side='left', padx=5) 
    label5.pack(side='left') 
    Yparameters_combobox.pack(side='left', padx=5)
    ShowGraphBtn.pack()


    Upload_frame.pack(pady=20)



#Function to show Analytics page
def Analytics_Page():
    Analytics_frame = tk.Frame(main_frame)
    #Code here for Analytics page

    Scamdata = pd.read_json('ProjTest\ScamData.json')
    Years = [i["Year"] for i in Scamdata["Scam"]]
    Amt = [i["Amt Fallen"] for i in Scamdata["Scam"]]

    fig, ax = plt.subplots(figsize=(10,7))
    ax.bar(Years,Amt, color='maroon')
    ax.set_xlim(xmin=0.0)
    ax.set_xlabel('Years',fontsize=14)
    ax.set_ylabel('Amt Fallen to Scam',fontsize=14)
    ax.set_title('Test Graph from JSON',fontsize=14)

    canvas1 = FigureCanvasTkAgg(fig, Analytics_frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side="left", expand=False)

    lb = tk.Label(Analytics_frame, text='Analytics \npage', font=('Bold', 30))
    lb.pack()

    Analytics_frame.pack(pady=20)

#Function to show Data page
def Data_Page():
    Data_frame = tk.Frame(main_frame)

    #Code here for Data page
    lb = tk.Label(Data_frame, text='Data page', font=('Bold', 30))
    lb.pack()

    # 1st graph (Bar Chart), .keys = column name, .values = row value
    fig1, ax1 = plt.subplots()
    ax1.bar(sales_data.keys(), sales_data.values())
    ax1.set_title("Sales of Product") #Set graph title
    ax1.set_xlabel("Product")
    ax1.set_ylabel("Sales")
    fig1.set_figheight(4)
    fig1.set_figwidth(6)

    canvas1 = FigureCanvasTkAgg(fig1, Data_frame)
    canvas1.draw()
    canvas1.get_tk_widget().pack(side="left", expand=False)
    

    # Chart 2: Horizontal bar chart of inventory data
    fig2, ax2 = plt.subplots()
    ax2.barh(list(inventory_data.keys()), inventory_data.values())
    ax2.set_title("Inventory by Product")
    ax2.set_xlabel("Inventory")
    ax2.set_ylabel("Product")
    fig2.set_figheight(4)
    fig2.set_figwidth(6)

    canvas2 = FigureCanvasTkAgg(fig2, Data_frame)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side="left", expand=False)

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