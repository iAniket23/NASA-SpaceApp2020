import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash(__name__)

#df = pd.read_hdf('./data/dataset.h5')
hdf = pd.HDFStore('./data/dataset.h5')
hdf.keys()
#df1 = hdf.get('/DF1')

app.layout = html.Div([
    #df1.head()
])

if __name__ == '__main__':
    app.run_server(debug=False)