# imports
import dash
import plotly.express as px
import pandas as pd

# Core Dash Functionality -> higher-level components that are 
# interactive and are generated with JavaScript, HTML, and 
# CSS through the React.js library
import dash_core_components as dcc
# HTML Functionality -> Visual Components
import dash_html_components as html

# external style sheets url 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Instantiate App Instance
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Define Color Dictionary
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# ---- Define App Data ----
# assume you have "long-form" data frame
# defining data-frame -> Nothing special to see here.
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Define Plot
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Specify Plot Colors
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

# --- 2 Parts to Every Dash App ---
# --- Layout ---
# --- Interactivity ---
# -> For now, we are just seeing layout...?

# Looks like each html component is a html method
# Each html method is responsible for generating the necessar html to 
# make the page work as intended

# style= is always passed a dictionary with pre-defined keys
            # Top Div
app.layout = html.Div(style={'backgroundColor': colors['background']}, 
children=[
# children is inherently always the first argument of html objects
                                # AKA the first attribute or property

    # Header 1 -> Within Div -> Child of Div?
    html.H1(
        children="Hello Taylor's Dash",
        style={
            'textAlign': 'center',
            'color': colors['text'] 
        }
    ),
     
    # This is a Div Within Div
    html.Div(children='''
    Dash: A web application framework for Python
    ''',
    style={
        'textAlign': 'center',
        'color': colors['text']
    }
    ),

    # This is dcc as opposed to html because it is core to dash functionality
    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )

])

if __name__ == '__main__':
    # Run the Server
    app.run_server(debug=True)