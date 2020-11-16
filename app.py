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
    'background': '#E75480',
    'text': '#7FDBFF'
}

# ---- Add Bar Chart ----
# assume you have "long-form" data frame
# defining data-frame -> Nothing special to see here.
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Define Plot
fig_bar = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Specify Plot Colors
fig_bar.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

# ---- Add Table ----

df_table = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

# ---- Add Bubble Chart ----

# Load Data
df_bubble = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')

fig_bubble = px.scatter(df_bubble, x="gdp per capita", y="life expectancy",
                size="population", color="continent", hover_name="country",
                log_x=True, size_max=60)

# ---- Add Text Using Markdown ----
markdown_text = """
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
"""


# --- 2 Parts to Every Dash App ---
# --- Layout ---
# --- Interactivity ---
# -> For now, we are just seeing layout...?

# Looks like each html component is a html method
# Each html method is responsible for generating the necessar html to 
# make the page work as intended

# style= is always passed a dictionary with pre-defined keys
            # Top Div
app.layout = html.Div(style={'backgroundColor': colors['background'], 
                             'columnCount': '1'}, 
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
        figure=fig_bar
    ),

    html.Div(children=[
        html.H2(children='US Agriculture Exports (2011)'),
        generate_table(df_table)
    ]),

    html.Div(children=[
        html.H3("Life Expenctancy vs GDP"),
        dcc.Graph(
            id='example-graph-3',
            figure=fig_bubble
        )
    ]),

    html.Div(children=[
        # Pass Markdown the markdown text through children
        dcc.Markdown(children=markdown_text)
    ]),

    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    # Add Label -> Like a visual header
    html.Label('Multi-Select Dropdown'),
    # Instantiate Component
    dcc.Dropdown(
        # Define Options 
        # -> Outward Label, Than Internal Variable Name
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'} 
        ],
        # Define Defaults
        value=['MTL', 'SF'],
        # Define Other Details
        multi=True
    ),

    # Standardized Test Bubble
    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='MTL'
    ),

    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montreal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value=['MTL', 'SF']
    ),

    html.Label('Text Input'),
    dcc.Input(value='MTL', type='text'),

    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=5
    ),

    html.H4("Change the value in the text box to see callbacks in action!"),

    # In Dash, the *inputs and outputs* of our application are simply the 
    # properties of a particular component.

    # -> Input Component <- 
    html.Div(["Input: ", # MATCH
              dcc.Input(id='my-input', 
                        value='default_value', # Input Property
                        type='text')
    ]),
    # ?
    html.Br(),

    # -> Output Component <-
                # MATCH 2
    html.Div(id='my-output') # Output Property
    # We do not set a value here because it is automatically connected to
    # the input property... and any value supplied in the output component
    # would just be overwritten by the value at the input component.

    # It's sort of like programming with Microsoft Excel: whenever an input 
    # cell changes, all of the cells that depend on that cell will get 
    # updated automatically. This is called "Reactive Programming".

])

#  -- Decorator -- 
# Whenever an input property changes, the function that the callback decorator
# wraps will get called automatically.
# Dash provides the function with the new value of the input property as
# an input argument and Dash updates the property of the output component with
# the ID "my-output".
@app.callback( 
             # MATCH 2
    # The component_id and component_property arguments are optional
    Output(component_id='my-output', component_property='children'),
                        # MATCH
    [Input(component_id='my-input', component_property='value')]
    # ?- So? Output(), [Input()] -?
)
def update_output_div(input_value):
    return 'Output: {}'.format(input_value)

if __name__ == '__main__':
    # Run the Server
    app.run_server(debug=True)