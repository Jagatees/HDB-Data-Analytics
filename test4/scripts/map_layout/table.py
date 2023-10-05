import csv
import random
from flask import Flask, render_template
import numpy as np
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


def display_table():
    # Read the CSV file and parse its data
    csv_file = 'scripts/algo/Excel/output/MillionDollarHse.csv'
    df = pd.read_csv(csv_file)
    
    # Step 3: Create a Plotly table from the DataFrame
    table_fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns)),
        cells=dict(values=[df[col] for col in df.columns]))
    ])

    #Step 4: Convert the Plotly figure to HTML
    table_html = table_fig.to_html(full_html=False)

    return table_html