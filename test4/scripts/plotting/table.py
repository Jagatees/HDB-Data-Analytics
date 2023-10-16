import pandas as pd
import dash
from dash import html, dash_table, dcc, Input, Output

# Read the filtered CSV
filtered_df = pd.read_csv(
    'https://raw.githubusercontent.com/Jagatees/Python_Data_Scrapper_Anyaltics/main/test4/scripts/algo/Excel/output/UpdatedUserHse.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the filter components
app.layout = html.Div([
    html.H1('Filtered Housing Data Table'),
    dcc.Dropdown(
        id='location-type-filter',
        options=[
            {'label': location_type, 'value': location_type}
            for location_type in filtered_df['Location_Type'].unique()
        ],
        multi=True,
        placeholder="Filter by Location Type"
    ),
    dcc.RangeSlider(
        id='floor-area-filter',
        min=filtered_df['floor_area_sqm'].min(),
        max=filtered_df['floor_area_sqm'].max(),
        step=10,
        marks={i: str(i) for i in range(
            filtered_df['floor_area_sqm'].min(),
            filtered_df['floor_area_sqm'].max() + 1
        )},
        value=[filtered_df['floor_area_sqm'].min(), filtered_df['floor_area_sqm'].max()],
        allowCross=False
    ),
    dash_table.DataTable(
        id='table',
        columns=[
            {'name': 'Area', 'id': 'Area'},
            {'name': 'Location_Type', 'id': 'Location_Type'},
            {'name': 'floor_area_sqm', 'id': 'floor_area_sqm'},
            {'name': 'remaining_lease', 'id': 'remaining_lease'},
            {'name': 'Sale_Price', 'id': 'Sale_Price'},
            {'name': 'Profit', 'id': 'Profit'}
        ],
    ),
])




