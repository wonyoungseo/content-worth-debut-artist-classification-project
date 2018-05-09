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
            html.A([
                html.Img(
                    # src='https://i.imgur.com/zNUvykh.png', # parrot icon
                    src='https://cdn4.iconfinder.com/data/icons/iconsimple-logotypes/512/github-128.png', # github icon
                    style={
                        'height' : '4%',
                        'width' : '4%',
                        'float' : 'right',
                        'position' : 'relative',
                        'padding-top' : 1,
                        'padding-right' : 15
                    },
                )
            ], href='https://github.com/lucaseo/debut-artist-go-or-no-go')
        ),

        html.Div(
            html.H1('Dash App Layout')
        ),

        # html.Div(
        #     dcc.Tabs(
        #         tabs=[
        #             {'label': 'Genres', 'value': 1},
        #             {'label': 'Online Buzz', 'value': 2},
        #             {'label': 'Average Ratings', 'value': 3},
        #             {'label': 'SNS Followers', 'value': 4},
        #         ],
        #         value=1,
        #         id='tabs',
        #         vertical=True,
        #         style={
        #             'height': '100vh',
        #             'borderRight': 'thin lightgrey solid',
        #             'textAlign': 'left'
        #         }
        #     ),style={'width': '20%', 'float': 'left'}
        # ),
        html.Div(
            dcc.Dropdown(
                    options=[
                        {'label': 'Genres Ratio', 'value': 1},
                        {'label': 'Online Buzz', 'value': 2},
                        {'label': 'Average Ratings', 'value': 3},
                        {'label': 'Single Count Comparison', 'value': 4},
                        {'label': 'SNS Followers Ratio', 'value': 5},
                    ],
                # value=3,
                id = 'dropdown',
                placeholder="옵션을 선택하세요",

            ),
            style = {
                    'width' : '40%'
            }
        ),

        html.Div(
            html.Div(id='dropdown-output'),
            # style={'width': '80%', 'float': 'right'}
        ),
        ],
    )
)


@app.callback(Output('dropdown-output', 'children'), [Input('dropdown', 'value')])
def display_content(value):

    data = [
        {
            'x': [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                  2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
            'y': [219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                  350, 430, 474, 526, 488, 537, 500, 439],
            'name': 'test 1',
            'marker': {
                'color': 'rgb(247, 160, 46)'
            },
            'type': [ 'box','scatter', 'box', 'bar', 'scatter'][int(value) % 5]
        },

        {
            'x': [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                  2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
            'y': [16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                  299, 340, 403, 549, 499],
            'name': 'test 2',
            'marker': {
                'color': 'rgb(75, 188, 145)'
            },
            'type': [ 'box', 'scatter', 'box', 'bar', 'scatter'][int(value) % 5]
        }

    ]

    return html.Div([

                html.Div(
                    dcc.Markdown('''
#### Markdown Test

한글 테스트.

Markdown is a simple way to write and format text.
It includes a syntax for things like **bold text** and *italics*,
[links](http://commonmark.org/help), inline `code` snippets, lists,
quotes, and more.
* * * *
                    ''')
                ),

        dcc.Graph(
            id='graph',
            figure={
                'data': data,
                'layout': {
                    'margin': {
                        'l': 50,
                        'r': 50,
                        'b': 50,
                        't': 0
                    },
                    'legend': {'x': 0, 'y': 1}
                }
            }
        )

    ])


if __name__ == '__main__':
    app.run_server(debug=True)
