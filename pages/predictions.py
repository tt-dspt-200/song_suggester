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
from dash.exceptions import PreventUpdate
# import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# df = pd.read_csv('https://raw.githubusercontent.com/yestrella14/datasets/master/spotify_data_Reduced.csv')

#Create a dictionary with song name and Ids
# song_dictionary = df.set_index('id')['name'].to_dict()
# song_dictionary = (df[['id', 'name']]).to_dict(orient='records')
song_dictionary= [{'id': '0cS0A1fUEUd1EW3FcF8AEI', 'name': 'Keep A Song In Your Soul'}, {'id': '0hbkKFIJm7Z05H8Zl9w30f', 'name': 'I Put A Spell On You'}, {'id': '11m7laMUgmOKqI3oYzuhne', 'name': 'Golfing Papa'}, {'id': '19Lc5SfJJ5O1oaxY0fpwfh','name': 'True House Music - Xavier Santos & Carlos Gomix Remix'}]
# song_dictionary2 = (df[['name', 'id']]).to_dict(orient='records')
# song_name_data = df['name'].unique()

# options=[{'label': song_dictionary['name'], 'value': song_dictionary['id']}]

column2 = dbc.Col(
    [
        html.Div([
            html.Label('Look up your favorite song'),
            dcc.Dropdown(
            id='input_song',
            options=[{'label': i['name'], 'value': i['id']} for i in song_dictionary],
            value='Sunflower',
            placeholder = "Search for a song"
            ),

        html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'})
        
    
        # html.Div([
        #     html.Label('Look up your favorite song'),
        #     dcc.Dropdown(
        #     id='input_song',
        #     multi=True),

        # html.Div(
        #     id='textarea-example-output', style={'whiteSpace': 'pre-line'})


        ])

    ]
)
# layout = dbc.Row([column1, column2])
app.layout= dbc.Row([column1, column2])


# @app.callback(
#     dash.dependencies.Output("input_song", "options"),
#     [dash.dependencies.Input("input_song", "search_value")],
# )
# def update_options(search_value):
#     if not search_value:
#         raise PreventUpdate
#     return [o for o in song_dictionary2 if search_value in o["name"]]


if __name__ == "__main__":
    # print(song_dictionary[:4])
    app.run_server(debug=True)

# @app.callback(
# Output('textarea-example-output', 'children'),
# Input('input_song', 'value'))
        
# def update_output(value):
#     # my_value = value.values()
#     # return 'You have entered: \n{}'.format(my_value.values())
#     #get the key from the dictionary
#     # res = list(value.keys())[0] 
#     return 'You have entered: \n{}'.format(value)


