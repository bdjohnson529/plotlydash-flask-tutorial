"""Instantiate a Dash app."""
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import numpy as np
import pandas as pd

from .data import create_dataframe, load_dataframe_from_csv
from .layout import html_layout


def init_app(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix="/dashboard3/",
        external_stylesheets=[
            "/static/dist/css/styles.css",
            "https://fonts.googleapis.com/css?family=Lato",
        ],
    )

    # Load DataFrame
    parameters_df = load_dataframe_from_csv("data/input_parameters.csv")

    # Custom HTML layout
    dash_app.index_string = html_layout

    # Create Layout
    dash_app.layout = html.Div(
        children=[
            create_data_table(parameters_df),
            html.Button(id='save-button', n_clicks=0, children='Submit')
        ],
        id="dash-container",
    )

    @dash_app.callback(
        Input("save-button", "n_clicks"),
        State("database-table","data")
        )
    def selected_data_to_csv(nclicks, table1):
        print("Callback**********************************************"*10)

    return dash_app.server




def create_data_table(df):
    """Create Dash datatable from Pandas DataFrame."""
    table = dash_table.DataTable(
        id="database-table",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        sort_action="native",
        sort_mode="native",
        style_cell_conditional=[
            {'if': {'column_id': 'Parameter'},
             'width': '40%'}
        ],
        editable=True
    )
    return table