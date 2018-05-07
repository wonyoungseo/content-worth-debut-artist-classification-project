import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go

import pandas as pd

app = dash.Dash()
server = app.server

colors_default = {
    'background': '#111111',
    'text': '#229077  '
}



# Load Dataset
df = pd.read_csv('df_baseline-utf8.csv')
df_1 = df[df['label'] == 1].reset_index(drop=True)
df_0 = df[df['label'] == 0].reset_index(drop=True)




server = app.server

app.title = 'WACON DSS'

app.layout = html.Div(
    html.Div([


        # github logo on the upper right hand-side
        html.Div(
            html.A([
                html.Img(

                    # github icon
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
            html.A([
                html.Img(

                    # hiphople icon
                    src='http://real5781.cdn2.cafe24.com/hiphople_logo_2016.png', # parrot icon

                    # github icon
                    #src='https://cdn4.iconfinder.com/data/icons/iconsimple-logotypes/512/github-128.png', # github icon
                    style={
                        'height' : '4%',
                        'width' : '4%',
                        'float' : 'right',
                        'position' : 'relative',
                        'padding-top' : 1,
                        'padding-right' : 15
                    },
                )
            ], href='http://hiphople.com')
        ),

        html.Div(
            html.H1('Data Dashboard : WACON')
        ),

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
                placeholder="Select your option",

            ),
            style = {
                    'width' : '40%'
            }
        ),

        html.Div(
            html.Div(id='dropdown-output'),
        ),

        # html.Div(
        #     html.Div(id='dropdown-output-2'),
        # ),
        ],
    )
)

app.config['suppress_callback_exceptions']=True

@app.callback(Output('dropdown-output', 'children'),
                [Input('dropdown', 'value')])
def display_content(value):


    # Genre ratio
    if value == 1:
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
                'type': 'bar'
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
                'type': 'bar'
            }

            ]

        return html.Div([

                        html.Div(
                            dcc.Markdown('''
#### Markdown Test

Markdown testing
* * * *
                        ''')
                    ),

                # dcc.Graph(
                #     id='graph',
                #     figure={
                #         'data': data,
                #         'layout': {
                #             'margin': {
                #                 'l': 50,
                #                 'r': 50,
                #                 'b': 50,
                #                 't': 0
                #             },
                #             'legend': {'x': 0, 'y': 1}
                #         }
                #     }
                # )
                dcc.Graph(
                    id='heatmap',
                    figure={
                        'data': [{
                            'z': [
                                [1, 2, 3],
                                [4, 5, 6]
                            ],
                            'text': [
                                ['a', 'b', 'c'],
                                ['d', 'e', 'f']
                            ],
                            'customdata': [
                                ['c-a', 'c-b', 'c-c'],
                                ['c-d', 'c-e', 'c-f'],
                            ],
                            'type': 'heatmap'
                        }]
                    },
                    style={'height': '80vh'}
            ),
            ])

    elif value == 2:

        billboard_1 = df_1['freq_billboard'].mean()
        genius_1 = df_1['freq_genius'].mean()
        source_1 = df_1['freq_theSource'].mean()
        xxl_1 = df_1['freq_xxl'].mean()

        billboard_0 = df_0['freq_billboard'].mean()
        genius_0 = df_0['freq_genius'].mean()
        source_0 = df_0['freq_theSource'].mean()
        xxl_0 = df_0['freq_xxl'].mean()

        trace1 = go.Bar(
        x=['Published', 'Not Published'],
        y=[billboard_1, billboard_0],
        name='Billboard',
        marker=dict(
            color='#812492'
            )
        )

        trace2 = go.Bar(
        x=['Published', 'Not Published'],
        y=[genius_1, genius_0],
        name='Genius',
        marker=dict(
            color='#6DDA74'
            )
        )

        trace3 = go.Bar(
        x=['Published', 'Not Published'],
        y=[source_1, source_0],
        name='The Source',
        marker=dict(
            color='#2F8E3A'
            )
        )

        trace4 = go.Bar(
        x=['Published', 'Not Published'],
        y=[xxl_1, xxl_0],
        name='XXL Magazine',
        marker=dict(
            color='#84AFE0'
            )
        )

        data = [trace4, trace1, trace2, trace3]
        layout = go.Layout(
            barmode='stack'
        )

        return html.Div([

                        html.Div(
                            dcc.Markdown('''
#### Markdown Test

Markdown testing
* * * *
                        ''')
                    ),

                dcc.Graph(
                    id='buzz_bar_stack',
                    figure={
                        'data' : data,
                        'layout' : layout
                        },
                    style={'height': '78vh'}
                    ),
            ])


    # Avg. Ratings
    elif value == 3:

        ratings_1 = df_1['rating'].mean()
        ratings_0 = df_0['rating'].mean()

        data = [go.Bar(
            x=[ratings_0, ratings_1],
            y=['Not Published', 'Published'],
            orientation = 'h',
            marker=dict(
                color=['rgb(75, 188, 145)', 'rgb(247, 160, 46)']
                )
        )]

        return html.Div([

                        html.Div(
                            dcc.Markdown('''
#### Markdown Test

Markdown testing
* * * *
                        ''')
                    ),

                dcc.Graph(
                    id='graph',
                    figure={
                        'data': data,
                        'layout': {
                            'margin': {
                                'l': 200,
                                'r': 200,
                                'b': 50,
                                't': 100
                            },
                            'legend': {'x': 0, 'y': 1}
                        },

                    },
                    style={'height': '78vh'},
                )

            ])



    # Single Count
    elif value == 4:

        single_count_1 = df_1['single_count']
        single_count_0 = df_0['single_count']

        trace1 = go.Histogram(
            x=single_count_1,
            opacity=1,
            name='Published',
            marker=dict(
                color='rgb(247, 160, 46)'
                )
        )

        trace0 = go.Histogram(
            x=single_count_0,
            opacity=0.75,
            name='Not Published',
            marker=dict(
                color='rgb(75, 188, 145)'
                )
        )

        data = [trace0, trace1]
        layout = go.Layout(barmode='overlay')

        return html.Div([

                        html.Div(
                            dcc.Markdown('''
#### Markdown Test

Markdown testing
* * * *
                        ''')
                    ),

                dcc.Graph(
                    id='single_hist',
                    figure = {
                        'data':data,
                        'layout':layout,
                        'legend': {'x': 0, 'y': 1}
                        },
                    style={'height': '78vh'},

                )

            ])






    # SNS ratio
    elif value == 5:
        color_palette_1 = ['#6DDA74', '#BE2F76', '#84AFE0', '#CCB643', '#812492', '#B5642A']
        color_palette_2 = ['#FFFF00', '#BB3E94', '#2F8E3A']

        # By SNS Platform
        by_sns_platform_1 = []
        for platform in df_1[['twitter', 'instagram', 'facebook', 'youtube', 'soundcloud', 'spotify']]:
            sum_1 = df_1[platform].mean()
            by_sns_platform_1.append(sum_1)

        by_sns_platform_0 = []
        for platform in df_0[['twitter', 'instagram', 'facebook', 'youtube', 'soundcloud', 'spotify']]:
            sum_0 = df_0[platform].mean()
            by_sns_platform_0.append(sum_0)

        # By SNS Groups
        by_sns_groups_1 = []
        df_1['Private SNS'] = df_1['twitter'] + df_1['instagram']
        df_1['Fan Page'] = df_1['facebook'] + df_1['youtube']
        df_1['Music Account'] = df_1['soundcloud'] + df_1['spotify']
        for group in df_1[['Private SNS', 'Fan Page', 'Music Account']]:
            group_mean_1 = df_1[group].mean()
            by_sns_groups_1.append(group_mean_1)

        by_sns_groups_0 = []
        df_0['Private SNS'] = df_0['twitter'] + df_0['instagram']
        df_0['Fan Page'] = df_0['facebook'] + df_0['youtube']
        df_0['Music Account'] = df_0['soundcloud'] + df_0['spotify']
        for group in df_0[['Private SNS', 'Fan Page', 'Music Account']]:
            group_mean_0 = df_0[group].mean()
            by_sns_groups_0.append(group_mean_0)

        # By total count SNS
        twitter_1 = df_1['twitter'].sum()
        instagram_1 = df_1['instagram'].sum()
        facebook_1 = df_1['facebook'].sum()
        youtube_1 = df_1['youtube'].sum()
        soundcloud_1 = df_1['soundcloud'].sum()
        spotify_1 = df_1['spotify'].sum()

        twitter_0 = df_0['twitter'].sum()
        instagram_0 = df_0['instagram'].sum()
        facebook_0 = df_0['facebook'].sum()
        youtube_0 = df_0['youtube'].sum()
        soundcloud_0 = df_0['soundcloud'].sum()
        spotify_0 = df_0['spotify'].sum()

        data = [
            {
                'x': ['Twitter', 'Instagram', 'Facebook Page', 'Youtube Channel', 'SoundCloud', 'Spotify'],
                'y': [twitter_1, instagram_1, facebook_1, youtube_1, soundcloud_1, spotify_1],
                'name': 'Published',
                'marker': {
                    'color': 'rgb(247, 160, 46)'
                },
                'type': 'bar'
            },

            {
                'x': ['Twitter', 'Instagram', 'Facebook Page', 'Youtube Channel', 'SoundCloud', 'Spotify'],
                'y': [twitter_0, instagram_0, facebook_0, youtube_0, soundcloud_0, spotify_0],
                'name': 'Not Published',
                'marker': {
                    'color': 'rgb(75, 188, 145)'
                },
                'type': 'bar'
            }

            ]


        return html.Div([
            html.Div(
                dcc.Markdown('''
#### Markdown Test 2

Markdown tesing 2
* * * *
                        ''')
                    ),

            dcc.Graph(
                id='sns_pie_1',
                figure={
                  "data": [
                    {
                      "values": by_sns_platform_1,
                      "labels": ['A', 'B', 'C', 'D', 'E', 'F'],
                      "domain": {"x": [0, .48]},
                      "name": "Published",
                      "hoverinfo":"label+percent+name",
                      "hole": .3,
                      "type": "pie",
                      "marker" : {"colors":color_palette_1}
                    },
                    {
                      "values": by_sns_platform_0,
                      "labels": ['A', 'B', 'C', 'D', 'E', 'F'],
                      "textposition":"inside",
                      "domain": {"x": [.52, 1]},
                      "name": "Not Published",
                      "hoverinfo":"label+percent+name",
                      "hole": .5,
                      "type": "pie"
                    }],
                  "layout": {
                        "autosize" : True,
                        "height" : 600,
                        # "width" : 900,
                        "annotations": [

                            {
                                "font": {
                                    "size": 20
                                },
                                "showarrow": False,
                                "text": "Go",
                                "x": 0.2225,
                                "y": 0.5
                            },

                            {
                                "font": {
                                    "size": 20
                                },
                                "showarrow": False,
                                "text": "No Go",
                                "x": 0.7825,
                                "y": 0.5
                            }
                        ]
                    }
                }
                ),

            dcc.Graph(
                id='sns_pie_2',
                figure={
                  "data": [
                    {
                      "values": by_sns_groups_1,
                      "labels": df_1[['Private SNS', 'Fan Page', 'Music Account']].columns,
                      "domain": {"x": [0, .48]},
                      "name": "Published",
                      "hoverinfo":"label+percent+name",
                      "hole": .3,
                      "type": "pie",
                      "marker" : {"colors":color_palette_2}
                    },
                    {
                      "values": by_sns_groups_0,
                      "labels": df_0[['Private SNS', 'Fan Page', 'Music Account']].columns,
                      "textposition":"inside",
                      "domain": {"x": [.52, 1]},
                      "name": "Not Published",
                      "hoverinfo":"label+percent+name",
                      "hole": .5,
                      "type": "pie"
                    }],
                  "layout": {
                        "autosize" : True,
                        "height" : 600,
                        # "width" : 900,
                        "annotations": [

                            {
                                "font": {
                                    "size": 20
                                },
                                "showarrow": False,
                                "text": "Go",
                                "x": 0.2225,
                                "y": 0.5
                            },

                            {
                                "font": {
                                    "size": 20
                                },
                                "showarrow": False,
                                "text": "No Go",
                                "x": 0.7825,
                                "y": 0.5
                            }
                        ]
                    }
                }
                ),

            dcc.Graph(
                id='sns_bar',
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
