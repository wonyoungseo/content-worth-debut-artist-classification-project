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



# Load Dataset : dataset
df = pd.read_csv('df_baseline-utf8.csv')
df_1 = df[df['label'] == 1].reset_index(drop=True)
df_0 = df[df['label'] == 0].reset_index(drop=True)

# Load Dataset : feature importance
fi = pd.read_csv('df-feature_importance.csv')




server = app.server

app.title = 'Dash, Plotly 기반 데이터 시각화 대쉬보드 프로젝트'

app.layout = html.Div(
    html.Div([


        # Upper right-hand side : HiphopLE, Github logos links to the website
        # Linkedin
        html.Div(
            html.A([
                html.Img(

                    # Linkedin icon
                    src='http://icons.iconarchive.com/icons/uiconstock/socialmedia/512/Linkedin-icon.png',
                    style={
                        'height' : '3%',
                        'width' : '3%',
                        'float' : 'right',
                        'position' : 'relative',
                        'padding-top' : 1,
                        'padding-right' : 15
                    },
                )
            ], href='https://www.linkedin.com/in/lucaseo/')
        ),

        # Slide
        html.Div(
            html.A([
                html.Img(

                    # Linkedin icon
                    src='https://i.pinimg.com/originals/6b/43/2d/6b432daf0add33cf63afe1e9756a8d58.png',
                    style={
                        'height' : '3%',
                        'width' : '3%',
                        'float' : 'right',
                        'position' : 'relative',
                        'padding-top' : 1,
                        'padding-right' : 15
                    },
                )
            ], href='https://www.slideshare.net/secret/1dxnLsgdtsSspj')
        ),

        # Github
        html.Div(
            html.A([
                html.Img(

                    # github icon
                    src='https://cdn4.iconfinder.com/data/icons/iconsimple-logotypes/512/github-128.png', # github icon
                    style={
                        'height' : '3%',
                        'width' : '3%',
                        'float' : 'right',
                        'position' : 'relative',
                        'padding-top' : 1,
                        'padding-right' : 15
                    },
                )
            ], href='https://github.com/lucaseo/content-worth-debut-artist-classification-project')
        ),

        # Hiphople.com
        html.Div(
            html.A([
                html.Img(

                    # hiphople icon
                    src='http://real5781.cdn2.cafe24.com/hiphople_logo_2016.png',
                    style={
                        'height' : '3%',
                        'width' : '3%',
                        'float' : 'right',
                        'position' : 'relative',
                        'padding-top' : 1,
                        'padding-right' : 15
                    },
                )
            ], href='http://hiphople.com')
        ),




        # Dashboard Header
        html.Div(
            html.H1('Debut Artist Classifier : Data Visualization Dashboard')
        ),


        #Dropdown Menu
        html.Div(
            dcc.Dropdown(
                    options=[
                        {'label': 'Genres Counts Comparison', 'value': 1},
                        {'label': 'Online Aticle Buzz Frequency', 'value': 2},
                        {'label': 'Average Ratings', 'value': 3},
                        {'label': 'Single Count Distribution', 'value': 4},
                        {'label': 'SNS Followers Comparison', 'value': 5},
                        {'label': 'Model Feature Importances', 'value': 6},
                    ],
                value=6,   # indicate fixed value if you want to view certain label at the beginning
                id = 'dropdown',
                placeholder="Select your option",

            ),
            style = {
                    'width' : '40%'
            }
        ),


        # Division to display output corresponding to each dropdown options
        html.Div(
            html.Div(id='dropdown-output'),
        ),
        ],
    )
)

app.config['suppress_callback_exceptions']=True

@app.callback(Output('dropdown-output', 'children'),
                [Input('dropdown', 'value')])
def display_content(value):


    # Genre ratio
    if value == 1:

        df_1_hiphop = len(df_1[df_1['genre'] == 'hiphop'])
        df_1_rnb = len(df_1[df_1['genre'] == 'rnb'])
        df_1_soul = len(df_1[df_1['genre'] == 'soul'])
        df_1_funk = len(df_1[df_1['genre'] == 'funk'])
        df_1_pop = len(df_1[df_1['genre'] == 'pop'])

        df_0_hiphop = len(df_0[df_0['genre'] == 'hiphop'])
        df_0_rnb = len(df_0[df_0['genre'] == 'rnb'])
        df_0_soul = len(df_0[df_0['genre'] == 'soul'])
        df_0_funk = len(df_0[df_0['genre'] == 'funk'])
        df_0_pop = len(df_0[df_0['genre'] == 'pop'])

        # color_palette_1 = ['#CF9322', '#E8851B', '#FF742A', '#E8340D', '#FF4645']
        # color_palette_0 = ['#1E4E4F', '#329677', '#317F4D', '#29962C', '#5F8C45']

        data_1 = [{
                'x': ['Hip-Hop', 'R&B', 'Soul', 'Funk', 'Pop'],
                'y': [df_1_hiphop, df_1_rnb, df_1_soul, df_1_funk, df_1_pop],
                'name': 'Published',
                'marker': {
                    'color': 'rgb(247, 160, 46)'
                },
                'type': 'bar'
        }]

        data_0 = [{
                'x': ['Hip-Hop', 'R&B', 'Soul', 'Funk', 'Pop'],
                'y': [df_0_hiphop, df_0_rnb, df_0_soul, df_0_funk, df_0_pop],
                'name': 'Not Published',
                'marker': {
                    'color': 'rgb(75, 188, 145)'
                },
                'type': 'bar'
            }]

        return html.Div([

            html.Div(
                dcc.Markdown('''
* * * *
                        ''')
                    ),
            html.Div( children=[
                html.Div(
                    dcc.Graph(
                        id='genre_bar_1',
                        figure={
                            'data': data_1,
                            'layout': {
                                'title' : 'Published',
                                'margin': {
                                    'l': 50,
                                    'r': 50,
                                    'b': 50,
                                    't': 100
                                },
                                'xaxis' : dict(
                                    title='Published',
                                    titlefront=dict(
                                    family = 'Courier New, monospace',
                                    size=20,
                                    color='#7f7f7f')),
                                'legend': {'x': 0, 'y': 1}
                            }
                        }, style={
                            'height': '70vh',
                            'width' : '80vh',
                                }
                ), style={'display' : 'inline-block'}
                ),

                html.Div(
                    dcc.Graph(
                        id='genre_bar__2',
                        figure={
                            'data': data_0,
                            'layout': {
                                'title' : 'Not Published',
                                'margin': {
                                    'l': 50,
                                    'r': 50,
                                    'b': 50,
                                    't': 100
                                },
                                'xaxis' : dict(
                                    title='Not Published',
                                    titlefront=dict(
                                    family = 'Courier New, monospace',
                                    size=20,
                                    color='#7f7f7f')),
                                'legend': {'x': 0, 'y': 1}
                            }
                        }, style={
                            'height': '70vh',
                            'width' : '80vh',
                                }
                    ), style={'display' : 'inline-block'})
            ], style={'width': '100%', 'display': 'inline-block'})

            ])


    # Avg Buzz count comparison
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
            color='#B06ECF'
            )
        )

        trace2 = go.Bar(
        x=['Published', 'Not Published'],
        y=[genius_1, genius_0],
        name='Genius',
        marker=dict(
            color='#C7C357'
            )
        )

        trace3 = go.Bar(
        x=['Published', 'Not Published'],
        y=[source_1, source_0],
        name='The Source',
        marker=dict(
            color='#245C6B'
            )
        )

        trace4 = go.Bar(
        x=['Published', 'Not Published'],
        y=[xxl_1, xxl_0],
        name='XXL Magazine',
        marker=dict(
            color='#AC3945'
            )
        )

        data = [trace4, trace1, trace2, trace3]
        layout = go.Layout(
            barmode='stack'
        )

        return html.Div([

                        html.Div(
                            dcc.Markdown('''
* * * *
                        ''')
                    ),

                dcc.Graph(
                    id='buzz_bar_stack',
                    figure={
                        'title' : 'Article Buzz Count',
                        'data' : data,
                        'layout' : layout
                        },
                    style={'height': '75vh'}
                    ),
            ])


    # Avg. Ratings Comparison
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
* * * *
                        ''')
                    ),

                dcc.Graph(
                    id='graph',
                    figure={
                        'data': data,
                        'layout': {
                            'title' : 'Average Rating Score',
                            'margin': {
                                'l': 200,
                                'r': 200,
                                'b': 50,
                                't': 100},
                        # 'xaxis' : dict(
                        #     title='Average Rating Score',
                        #     titlefront=dict(
                        #     family = 'Courier New, monospace',
                        #     size=20,
                        #     color='#7f7f7f')),
                        'legend': {'x': 0, 'y': 1}
                        },

                    },
                    style={'height': '75vh'},
                )

            ])



    # Single Count Comparison
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
        layout = {
            'title' : 'Count of pre-release singles',
            'barmode':'overlay',
            'xaxis' : dict(
                # title='Count of pre-release singles',
                titlefront=dict(
                family = 'Courier New, monospace',
                size=20,
                color='#7f7f7f'))
            }

        return html.Div([

                        html.Div(
                            dcc.Markdown('''
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
                    style={'height': '75vh'},

                )

            ])




    # SNS Ratio & Avg Count Comparison
    elif value == 5:
        color_palette_1 = ['#20ECF9', '#C13BD6', '#3B50D6', '#C70039', '#F98920', '#20F94B']

        # By SNS Platform
        by_sns_platform_1 = []
        for platform in df_1[['twitter', 'instagram', 'facebook', 'youtube', 'soundcloud', 'spotify']]:
            sum_1 = df_1[platform].mean()
            by_sns_platform_1.append(sum_1)

        by_sns_platform_0 = []
        for platform in df_0[['twitter', 'instagram', 'facebook', 'youtube', 'soundcloud', 'spotify']]:
            sum_0 = df_0[platform].mean()
            by_sns_platform_0.append(sum_0)

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
* * * *
                        ''')
                    ),

            dcc.Graph(
                id='sns_pie_1',
                figure={
                  "data": [
                    {
                      "values": by_sns_platform_1,
                      "labels": ['Twitter', 'Instagram', 'Facebook Page', 'Youtube Channel', 'SoundCloud', 'Spotify'],
                      "domain": {"x": [0, .48]},
                      "name": "Published",
                      "hoverinfo":"label+percent+name",
                      "Pull": .2,
                      "hole": .3,
                      "type": "pie",
                      "marker" : {"colors":color_palette_1}
                    },
                    {
                      "values": by_sns_platform_0,
                      "labels": ['Twitter', 'Instagram', 'Facebook Page', 'Youtube Channel', 'SoundCloud', 'Spotify'],
                      "textposition":"inside",
                      "domain": {"x": [.52, 1]},
                      "name": "Not Published",
                      "hoverinfo":"label+percent+name",
                      "hole": .5,
                      "type": "pie",
                      "marker" : {"colors":color_palette_1}
                    }],
                  "layout": {
                        "title" : "SNS Followers Comparison",
                        "autosize" : True,
                        "height" : 600,
                        # "width" : 900,
                        "annotations": [

                            {
                                "font": {
                                    "size": 20
                                },
                                "showarrow": False,
                                "text": "Published",
                                "x": 0.20,
                                "y": 0.5
                            },

                            {
                                "font": {
                                    "size": 20
                                },
                                "showarrow": False,
                                "text": "Not Published",
                                "x": 0.825,
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
                            't': 50
                        },
                        'legend': {'x': 0, 'y': 1}
                    }
                }
                )

        ])

    elif value == 6:

        fi.sort_values(by=['importance'], ascending=True, inplace=True)
        fi['importance'] = fi['importance'] * 100

        data = [go.Bar(
            x=fi['importance'],
            y=fi['feature'],
            orientation = 'h',
        )]



        return html.Div([
                    html.Div(
                        dcc.Markdown('''
* * * *
                        ''')
                    ),
                dcc.Graph(
                    id='graph',
                    figure={
                        'data': data,
                        'layout': {
                            'title' : 'Model Feature Importance (%)',
                            'margin': {
                                'l': 200,
                                'r': 200,
                                'b': 50,
                                't': 100},
                        # 'xaxis' : dict(
                        #     title='Average Rating Score',
                        #     titlefront=dict(
                        #     family = 'Courier New, monospace',
                        #     size=20,
                        #     color='#7f7f7f')),
                        # 'yaxis' : dict(
                        #     hoverformat = '.3f'),
                        'legend' : {'x': 0, 'y': 1}
                        },

                    },
                    style={'height': '75vh'},
                )

            ])






if __name__ == '__main__':
    app.run_server(debug=True)
