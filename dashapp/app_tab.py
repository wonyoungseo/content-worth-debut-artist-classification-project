import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from loremipsum import get_sentences

import plotly.graph_objs as go

app = dash.Dash()

colors = {
    'background': '#111111',
    'text': '#229077  '
}

server = app.server

app.title = 'WACON'

app.layout = html.Div(
    html.Div([

        html.Div(
            html.Img(
                src='https://i.imgur.com/zNUvykh.png',
                style={
                    'height' : '4%',
                    'width' : '4%',
                    'float' : 'right',
                    'position' : 'relative',
                    'padding-top' : 0,
                    'padding-right' : 0

                },
            )
        ),

        html.Div(
            html.H1('Dash App Layout')
        ),

        html.Div(
            dcc.Tabs(
                tabs=[
                    {'label': 'Genres', 'value': 1},
                    {'label': 'Online Buzz', 'value': 2},
                    {'label': 'Average Ratings', 'value': 3},
                    {'label': 'SNS Followers', 'value': 4},
                ],
                value=1,
                id='tabs',
                vertical=True,
                style={
                    'height': '100vh',
                    'borderRight': 'thin lightgrey solid',
                    'textAlign': 'left'
                }
            ),style={'width': '20%', 'float': 'left'}
        ),
        # html.Div(
        #     dcc.Dropdown(
        #             options=[
        #                 {'label': 'Genres', 'value': 1},
        #                 {'label': 'Online Buzz', 'value': 2},
        #                 {'label': 'Average Ratings', 'value': 3},
        #                 {'label': 'SNS Followers', 'value': 4},
        #             ],
        #         # value=3,
        #         id = 'dropdown',
        #         placeholder="옵션을 선택하세요",
        #
        #     ),
        #     style = {
        #             'width' : '40%'
        #     }
        # ),
        #
        html.Div(
            html.Div(id='tab-output'),
            style={'width': '80%', 'float': 'right'}
        ),
        ],
    )
)


@app.callback(Output('tab-output', 'children'), [Input('tabs', 'value')])
def display_content(value):

    data = [
        {
            'x': [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                  2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
            'y': [219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                  350, 430, 474, 526, 488, 537, 500, 439],
            'name': 'Rest of world',
            'marker': {
                'color': 'rgb(55, 83, 109)'
            },
            'type': [ 'line','scatter', 'box', 'bar'][int(value) % 4]
        },

        {
            'x': [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                  2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
            'y': [16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                  299, 340, 403, 549, 499],
            'name': 'China',
            'marker': {
                'color': 'rgb(26, 118, 255)'
            },
            'type': [ 'line', 'scatter', 'box', 'bar'][int(value) % 4]
        }

    ]

    return html.Div([



        dcc.Graph(
            id='graph',
            figure={
                'data': data,
                'layout': {
                    'margin': {
                        'l': 30,
                        'r': 0,
                        'b': 30,
                        't': 0
                    },
                    'legend': {'x': 0, 'y': 1}
                }
            }
        ),

        html.Div(
            dcc.Markdown('''
* * * *
#### Markdown Test

한글 테스트.

Markdown is a simple way to write and format text.
It includes a syntax for things like **bold text** and *italics*,
[links](http://commonmark.org/help), inline `code` snippets, lists,
quotes, and more.
            ''')
        ), style

    ])


if __name__ == '__main__':
    app.run_server(debug=True)
