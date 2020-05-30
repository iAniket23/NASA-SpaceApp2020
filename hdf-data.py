import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_hdf('./data/VNP46A1.A2020017.h00v08.001.2020053010251.h5')

app.layout = html.Div([
    df.head()
])

if __name__ == '__main__':
    app.run_server(debug=False)