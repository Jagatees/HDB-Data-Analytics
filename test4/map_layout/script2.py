import tkinter as tk
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

# Initialize Dash app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Global variable to store a reference to the script2 window
script2_window = None

# Load the carshare data
print('getting data...')
df = px.data.carshare()

# Create a Dash component for the Plotly map
map_fig = px.scatter_mapbox(df,
                            lon=df['centroid_lon'],
                            lat=df['centroid_lat'],
                            zoom=10,
                            color=df['peak_hour'],
                            size=df['car_hours'],
                            width=1200,
                            height=900,
                            title='Car Share Scatter Map',
                            )
map_fig.update_layout(mapbox_style="open-street-map")
map_fig.update_layout(margin={"r": 0, "t": 50, "l": 0, "b": 10})

# Create a layout function for your Tkinter window
def create_layout(root):
    # Create widgets and layout for script2
    label = tk.Label(root, text="This is the layout from script2")
    label.pack()

    # Add a Dash component to the Tkinter window
    app.layout = html.Div([
        html.H1("Car Share Scatter Map"),
        dcc.Graph(figure=map_fig),
    ])

def show_window():
    global script2_window

    if script2_window is None:
        script2_window = tk.Toplevel()
        script2_window.title("Scrapping Dashboard")
        create_layout(script2_window)
        script2_window.protocol("WM_DELETE_WINDOW", hide_window)

    script2_window.deiconify()

def hide_window():
    global script2_window
    if script2_window is not None:
        script2_window.withdraw()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Scrapping Dashboard")

    create_layout(root)

    root.protocol("WM_DELETE_WINDOW", hide_window)

    root.mainloop()
