import flask
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as gobs
import plotly.express as px
import datetime

external_stylesheets = ['https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css']


external_scripts = ['https://code.jquery.com/jquery-3.2.1.slim.min.js',
                    'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js',
                    'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js']

# Server definition

server = flask.Flask(__name__)
app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                external_scripts=external_scripts,
                server=server)

# HEADER
# ======

header = dbc.NavbarSimple(
    children=[
    ],
    brand="Internet Connection Dashboard",
    brand_href="#",
    color="primary",
    dark=True
)


# COMPONENTS
# ==========

# Your components go here.
def dateparse (time_in_secs):    
    return datetime.datetime.fromtimestamp(float(time_in_secs))

def create_plot():
    connection_log_url = "https://github.com/tim-fan/internet_connection_datalogging/raw/main/logs/dryden.csv"

    df = pd.read_csv(
        connection_log_url,
        converters={"timestamp":dateparse, "ping_successful":bool })
    # give user friendly col names
    df = df.rename(columns=dict(
        timestamp="Timestamp",
        ssid="Network",
        device_connected="Can connect to network",
        ping_successful="Internet connected",
    ))
    fig = px.line(df, x="Timestamp", y="Internet connected", color="Network")
    fig.data[0].update(mode='markers+lines')
    return fig

graph = dcc.Graph(
    id='connectivity-graph',
    figure=create_plot()
)

interval_component = dcc.Interval(
    id='interval-component',
    interval=60*1000, # in milliseconds
)

# INTERACTION
# ===========

# Your interaction goes here.


# APP LAYOUT
# ==========

app.layout = html.Div([
    header,
    graph,
    interval_component,
])

# callbacks
@app.callback(Output('connectivity-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def plot_interval_callback(n):
    return create_plot()

if __name__ == '__main__':
    app.run_server(debug=True)