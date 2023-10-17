import pandas as pd
from flask import Flask, render_template
from dash import Dash, html, dcc, Input, Output, dash_table


def create_filtered_housing_data_app():
    # Create a Flask app instance
    server = Flask(__name__)

    # Create a Dash app instance and link it to the Flask server
    app = Dash(__name__, server=server)

    # Read the filtered CSV
    filtered_df = pd.read_csv(
        'scripts/algo/Excel/output/UpdatedUserHse.csv')

    app.layout = html.Div([
        html.H1('Filtered Housing Data Table'),

        # Define the filter components
        html.Div([  # Dropdown filter wrapped in a separate div
            dcc.Dropdown(
                id='location-type-filter',
                options=[
                    {'label': location_type, 'value': location_type}
                    for location_type in filtered_df['Location_Type'].unique()
                ],
                multi=True,
                placeholder="Filter by Location Type"
            )
        ]),

        html.Div([  # RangeSlider for Floor Area wrapped in a separate div
            html.Label("Filter by Floor Area:"),
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
            )
        ]),

        html.Div([  # RangeSlider for Lease wrapped in a separate div
            html.Label("Filter by Lease:"),
            dcc.RangeSlider(
                id='lease-filter',
                min=filtered_df['remaining_lease'].min(),
                max=filtered_df['remaining_lease'].max(),
                step=10,
                marks={i: str(i) for i in range(
                    filtered_df['remaining_lease'].min(),
                    filtered_df['remaining_lease'].max() + 1,
                    2
                )},
                value=[filtered_df['remaining_lease'].min(), filtered_df['remaining_lease'].max()],
                allowCross=False
            )
        ]),

        html.Div([  # RangeSlider for Sale Price wrapped in a separate div
            html.Label("Filter by Sale Price:"),
            dcc.RangeSlider(
                id='sale-price-filter',
                min=filtered_df['Sale_Price'].min(),
                max=filtered_df['Sale_Price'].max(),
                step=50000,
                marks={i: str(i) for i in range(
                    filtered_df['Sale_Price'].min(),
                    filtered_df['Sale_Price'].max() + 1,
                    50000
                )},
                value=[filtered_df['Sale_Price'].min(), filtered_df['Sale_Price'].max()],
                allowCross=False
            )
        ]),

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
            style_table={'width': '80%'},
        ),
    ])

    @app.callback(
        Output('table', 'data'),
        Input('location-type-filter', 'value'),
        Input('floor-area-filter', 'value'),
        Input('lease-filter', 'value'),
        Input('sale-price-filter', 'value')
    )
    def update_table(location_type_filter, floor_area_filter, lease_filter, sale_price_filter):
        if location_type_filter is None:
            # If no location type is selected, return an empty DataFrame
            filtered_data = pd.DataFrame()
        else:
            # Apply filters
            filtered_data = filtered_df[
                (filtered_df['Location_Type'].isin(location_type_filter))
                & (filtered_df['floor_area_sqm'] >= floor_area_filter[0])
                & (filtered_df['floor_area_sqm'] <= floor_area_filter[1])
                & (filtered_df['remaining_lease'] >= lease_filter[0])
                & (filtered_df['remaining_lease'] <= lease_filter[1])
                & (filtered_df['Sale_Price'] >= sale_price_filter[0])
                & (filtered_df['Sale_Price'] <= sale_price_filter[1])
                ]

        return filtered_data.to_dict('records')

    @server.route('/')
    def home():
        return render_template('index.html')

    return server


if __name__ == '__main__':
    print('running')
    app = create_filtered_housing_data_app()
    app.run('127.0.0.1', 5082, debug=True)




