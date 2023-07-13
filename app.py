from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import os
import plotly.express as px

# Load Data
data_path = 'https://raw.githubusercontent.com/nwidyant9/Project00/main/dummy.csv'
df = pd.read_csv(data_path)

# Preprocessing Data
df = df.dropna(subset=['Mesin'])
df[['Load_time', 'Freq', 'Menit']] = df[['Load_time', 'Freq', 'Menit']].fillna(0)
df['BD_percent'] = round((df['Menit'] / df['Load_time']) * 100, 2)
df['BD_percent'] = df['BD_percent'].fillna(0)
df['Target_percent'] = round(df['Target'] * 100, 2)

# Dash App
app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='MME 1', style={'textAlign':'center'}),
    dcc.Dropdown(df.Mesin.unique(), '', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)

def update_graph(value):
  dff = df[df.Mesin==value]
  fig = px.line(dff, x='Bulan', y='BD_percent', markers=True)
  fig1 = px.line(dff, x='Bulan', y='BD_percent')
  return fig

if __name__ == '__main__':
    app.run(debug=True)