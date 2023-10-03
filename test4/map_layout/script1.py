import tkinter as tk
import script2
import chrolopleth_maps

def open_new_window():
    script2.show_window()


# Create the main application window
root = tk.Tk()
root.title("Main Meun")

# Create a button to open script2's window
button_open = tk.Button(root, text="Scrapping_Dashboard", command=open_new_window)
button_open.pack()

# Start the main window's main loop
root.mainloop()
