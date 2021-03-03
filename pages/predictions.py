# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
# from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            Your instructions: How to use your app to get new predictions.

            """
        ),
    ],
    md=4,
)

import dash  # (version 1.11.0)
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import datetime
import plotly.express as px

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://raw.githubusercontent.com/yestrella14/datasets/master/spotify_data_Reduced.csv')

#Create a dictionary with song name and Ids
# song_dictionary = df.set_index('id')['name'].to_dict()
song_dictionary = (df[['id', 'name']]).to_dict(orient='records')

# song_name = df['name'].unique()

column2 = dbc.Col(
    [

        dcc.Dropdown(
            id='input_song',
            options=[{'label': i['name'], 'value': i['id']} for i in song_dictionary],
            value='Sunflower'
            ),

    ]
)

layout = dbc.Row([column1, column2])

