# imports
import dash
import plotly.express as px
import pandas as pd
# Core Dash Functionality
import dash_core_components as dcc
# Visual Components
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have "long-form" data frame
# defining data-frame -> Nothing special to see here.
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# define plot
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# 2 Parts to Every Dash App
# - Layout 
# - Interactivity

# Looks like each html component is a html method
app.layout = html.Div(children=[

    # Header 1 -> Within Div -> Child of Div?
    html.H1(children='Hello Dash'),
     
    # This is a Div Within Div
    html.Div(children='''
    Dash: A web application framework for Python
    '''),

    # This is dcc as opposed to html because it is core to dash functionality
    dcc.Graph(
        id='example-graph',
        figure=fig
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)