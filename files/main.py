import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

window = tk.Tk()
window.geometry("800x600")
window.title("Data_Scraper_Analytics")

# Create a StringVar to hold the text for label3 (pending review)
label3_text = tk.StringVar()
label3_text.set("PENDING LOCATION")

# Function: To open os directory and get a file path as return (return value pending)
def getfiledirectory():
    filenames = filedialog.askopenfilenames()
    if filenames:
        print("Selected files:")
        for filename in filenames:
            print(filename)
            label3_text.set(filenames[0])
    else:
        label3_text.set('No File got')

# Function: To plot a graph
def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    fig, ax = plt.subplots()
    ax.hist(house_prices, 50)
    
    # Embed the Matplotlib Figure in the Tkinter tab2_frame using FigureCanvasTkAgg
    canvas = FigureCanvasTkAgg(fig, master=tab2_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

# Overall Tab
notebook = ttk.Notebook(window)
notebook.pack(fill='both', expand=True)

# Tab 1
tab1_frame = ttk.Frame(notebook)
notebook.add(tab1_frame, text="Web Scrapping")

# Function Buttons
button = tk.Button(tab1_frame, text="Browse", command=getfiledirectory)
button2 = tk.Button(tab1_frame, text="Start Scrapping")

# Widgets Layout
label1 = tk.Label(tab1_frame, text="Which Website You Want to Scrap:")
label2 = tk.Label(tab1_frame, text="Save File Location:")
label3 = tk.Label(tab1_frame, textvariable=label3_text)
label3_text.set("")

# Dropdown
website_choices = ["Website 1", "Website 2", "Website 3"]  # Replace with your website choices
selected_website = tk.StringVar()
website_combobox = ttk.Combobox(tab1_frame, textvariable=selected_website, values=website_choices)
selected_website.set(website_choices[0])  # Set the default selection

# Grid Layout for Tab 1
label1.grid(row=1, column=0, padx=10, pady=10)
website_combobox.grid(row=1, column=1, padx=10, pady=10)
label2.grid(row=0, column=0, padx=10, pady=10)
label3.grid(row=0, column=1, padx=10, pady=10)
button.grid(row=0, column=2, padx=10, pady=10)
button2.grid(row=3, column=0, padx=10, pady=10)

# Tab 2
tab2_frame = ttk.Frame(notebook)
notebook.add(tab2_frame, text="Analytics")

# Add a button to plot the graph in Tab 2
graph_button = tk.Button(tab2_frame, text="Plot Graph", command=graph)
graph_button.pack(padx=10, pady=10)

window.mainloop()
