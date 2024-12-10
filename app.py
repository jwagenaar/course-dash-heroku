import logging

from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import pennsieve2 as ps

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash()

server = app.server

ps = ps.Pennsieve(connect=True)

session = ps.connect()
logging.info(session)

user = session.get_user()
logging.info(user)
# ds = ps.get('https://api.pennsieve.io/discover/datasets', params={'limit':20})
# df_list = pd.DataFrame(ds['datasets'])


app.layout = [
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    # dcc.Dropdown(df_list.name.unique(), '' , id='dropdown-selection' ),
    dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run(debug=True)
