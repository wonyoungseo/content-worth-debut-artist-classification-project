import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly import graph_objs as go


# app.layout = html.Div(children=[
#     html.H1(children="Who's Hot, Who's Not?"),
#
#     html.Div(children='''
#         Visual Analysis on Debut Artists (2011 - Current).
#     '''),
#
#     dcc.Dropdown(
#         options=[
#         {'label' : 'Pitchfork Rating', 'value': 'Pitchfork'},
#         {'label' : 'Single Pre-releases', 'value': 'Singles'}
#         ],
#         value='Select'
#     ),
#
#
#
#     dcc.Markdown('''
#
# #### Testing Markdown for Dash Markdown
#
# '''),


all_options = {
    'All' : ['New York City', 'San Francisco', 'Cincinnati', u'Montréal', 'Toronto', 'Ottawa'],
    'US' : ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada' : [u'Montréal', 'Toronto', 'Ottawa'],
}

city_data = {
    'San Francisco' : {'x' : [1, 2, 3],  'y': [4, 1, 2]},
    u'Montréal' : {'x' : [1, 2, 3],  'y': [7, 12, 3]},
    'New York City' : {'x' : [1, 2, 3],  'y': [2, 9, 4]},
    'Cincinnati' : {'x' : [1, 2, 3],  'y': [1, 7, 9]},
    'Toronto' : {'x' : [1, 2, 3],  'y': [15, 3, 12]},
    'Ottawa' : {'x' : [1, 2, 3],  'y': [4, 7, 13]},
}

# 앱 시작
app = dash.Dash()
server = app.server

app.title = 'WACON'

colors = {
    'background': '#111111',
    'text': '#229077  '
}


app.css.append_css({'external_url': 'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css'})  # noqa: E501
# cdn 링크를 클릭해서 직접 내부적으로 조정할 수 있는 요소들을 확인하면 좋다
# 현재 cdn에서는 기본적으로 너비를 12columns로 설정 (단위 columns, % 여러가지가 있다)


# 레이아웃을 선언
app.layout = html.Div(
    html.Div([               # html.Div를 통해 구역을 따로따로 나누고, 스타일을 부여할 수 있음

        html.Div(
            [
                html.H1(children = 'Worth a Content or Not ?',
                        className = 'nine column',
                        style={
                        'textAlign': 'left',
                        'color': colors['text']
                        }),

                html.Img(
                    src='https://i.imgur.com/zNUvykh.png',
                    className='three columns',
                    style={
                        'height' : '7%',
                        'width' : '7%',
                        'float' : 'right',
                        'position' : 'relative',
                        'padding-top' : 0,
                        'padding-right' : 0

                    },
                ),
                # html.Div(
                # children = '''
                #     Dash : A web application framework for Python.
                # ''',
                #         className = 'nine columns'
                # ),
                dcc.Markdown('''
                ###  Dash and Markdown

                Dash supports [Markdown](http://commonmark.org/help).

                Markdown is a simple way to write and format text.
                It includes a syntax for things like **bold text** and *italics*,
                [links](http://commonmark.org/help), inline `code` snippets, lists,
                quotes, and more.
                ''',
                        className = 'nine columns'
                ),
            ], className='row'
        ),                              #className : header부분을 하나의 row로 지정

        html.Div(
            [
                html.Div(
                    [
                        html.P('Choose City:'),
                        dcc.Checklist(     # Dash core components 중 체크박스 (callback이 필요하다)
                                id = 'Cities',
                                # options=[
                                #     {'label': 'San Francisco', 'value': 'Sab Francisco'},
                                #     {'label': u'Montréal', 'value': u'Montréal'}
                                # ],
                                values=['San Francisco', u'Montréal'],
                                labelStyle={'display': 'inline-block'}
                        ),

                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                ),
                html.Div(
                    [
                        html.P('Choose Country:'),
                        dcc.RadioItems(     # 무조건 하나만, 둘 중 하나만 선택하게 하는 component
                            id = 'Country',
                            options=[{'label': k, 'value': k} for k in all_options.keys()],
                            value='All',
                            labelStyle={'display': 'inline-block'}
                        ),
                    ],
                    className='six columns',
                    style={'margin-top': '10'}
                )
            ], className="row"   # 체크박스 요소를 또 하나의 row에 지정
        ),

        html.Div([
            html.Div([    # nested div를 하나 더 추가해서 그래프를 각각 따로 관리
                dcc.Graph(
                    # graph 1
                    id='example-graph-1',

                )], className='six columns'  # 12 컬럼 중 5컬럼을 지정
                ),                           # 이렇게 하면 세로로 분할할 수 있다.
                                             # total 12 :)

            # graph 2 ( 두번 째 그래프 선언 )
            html.Div([
                dcc.Graph(
                    id='example-graph-2',
                )
            ], className='six columns'),  # 12 - 5 = 7

            ], className='row'
        ) # 그래프 부분은 또 하나의 row에 배정한다.

    ],
    className='ten columns offset-by-one',
    ), #style={'backgroundColor': colors['background']},                          # 글로벌적으로 좌우에 1columns씩 마진을 기본으로 부여 (offset)
)


@app.callback(
    dash.dependencies.Output('Cities', 'options'),
    [dash.dependencies.Input('Country', 'value')])
def set_cities_options(selected_countries):
    return [{'label': i, 'value': i} for i in all_options[selected_countries]]

# 참고용 archive [첫번 째 콜백 함수]
# # 첫번 째 그래프와, 체크박스에 관한 콜백 요소
# @app.callback(
#     dash.dependencies.Output('example-graph-1', 'figure'), #영향을 받는 id와 영향
#     [dash.dependencies.Input('Cities', 'values')]) #영향을 트리거 하는 id
# def update_image_src(selector):
#
#     #체크박스가 빈칸일 때, 무엇이 선택되냐에 따라 보여지는 그래프 요소를 구별해놓았다.
#     data = []
#     if 'San Francisco' in selector:
#         data.append({'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'San Francisco'})
#     if u'Montréal' in selector:
#         data.append({'x': [1, 2, 3], 'y': [7, 12, 3], 'type':'bar', 'name': u'Montréal'})
#
#     figure = {
#         'data': data,
#         'layout': {
#             'title': 'Bar Chart',
#             'xaxis': dict(
#                 title = 'x axis',
#                 titlefront = dict(
#                 family = 'Courier New, monospace',
#                 size = 25,
#                 color = '#7f7f7f'
#             )),
#             'yaxis': dict(
#                 title = 'y axis',
#                 titlefront = dict(
#                 family = 'Arial, monospace',
#                 size = 25,
#                 color = '#7f7f7f'
#             )),
#         }
#     }
#     return figure
#
# @app.callback(
#     dash.dependencies.Output('example-graph-2', 'figure'), #영향을 받는 id와 영향
#     [dash.dependencies.Input('Cities', 'values')]) #영향을 트리거 하는 id
# def update_image_src(selector):
#
#     #체크박스가 빈칸일 때, 무엇이 선택되냐에 따라 보여지는 그래프 요소를 구별해놓았다.
#     data = []
#     if 'San Francisco' in selector:
#         data.append({'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'San Francisco'})
#     if u'Montréal' in selector:
#         data.append({'x': [1, 2, 3], 'y': [7, 12, 3], 'type':'line', 'name': u'Montréal'})
#
#     figure = {
#         'data': data,
#         'layout': {
#             'title': 'Chart',
#             'xaxis': dict(
#                 title = 'x axis',
#                 titlefront = dict(
#                 family = 'Courier New, monospace',
#                 size = 25,
#                 color = '#7f7f7f'
#             )),
#             'yaxis': dict(
#                 title = 'y axis',
#                 titlefront = dict(
#                 family = 'Arial, monospace',
#                 size = 25,
#                 color = '#7f7f7f'
#             )),
#         }
#     }
#     return figure    # 복사 후, 위의 그래프 요소를 다 지우면, 둘 다 체크박스의 영향을 받음


# callback 함수 수정 (for문으로 데이터를 쉽게 추가하기 위해)
@app.callback(
    dash.dependencies.Output('example-graph-1', 'figure'),
    [dash.dependencies.Input('Cities', 'values')])
def update_image_src(selector):

    #체크박스가 빈칸일 때, 무엇이 선택되냐에 따라 보여지는 그래프 요소를 구별해놓았다.
    data = []
    for city in selector:
        data.append({ 'x' : city_data[city]['x'], 'y' : city_data[city]['y'],
                    'type': 'bar', 'name': city})

    figure = {
        'data': data,
        'layout': {
            'title': 'Chart',
            # 'plot_bgcolor': colors['background'],
            # 'paper_bgcolor': colors['background'],
            # 'font': {
            #     'color': colors['text']},
            'xaxis': dict(
                title = 'x axis',
                titlefront = dict(
                family = 'Courier New, monospace',
                size = 25,
                color = '#7FDBFF'
            )),
            'yaxis': dict(
                title = 'y axis',
                titlefront = dict(
                family = 'Arial, monospace',
                size = 25,
                color =  '#7FDBFF'
            )),
        }
    }
    return figure    # 복사 후, 위의 그래프 요소를 다 지우면, 둘 다 체크박스의 영향을 받음

@app.callback(
    dash.dependencies.Output('example-graph-2', 'figure'),
    [dash.dependencies.Input('Cities', 'values')])
def update_image_src(selector):

    #체크박스가 빈칸일 때, 무엇이 선택되냐에 따라 보여지는 그래프 요소를 구별해놓았다.
    data = []
    for city in selector:
        data.append({ 'x' : city_data[city]['x'], 'y' : city_data[city]['y'],
                    'type': 'line', 'name': city})

    figure = {
        'data': data,
        'layout': {
            'title': 'Chart',
            'xaxis': dict(
                title = 'x axis',
                titlefront = dict(
                family = 'Courier New, monospace',
                size = 25,
                color = '#7f7f7f'
            )),
            'yaxis': dict(
                title = 'y axis',
                titlefront = dict(
                family = 'Arial, monospace',
                size = 25,
                color = '#7f7f7f'
            )),
        }
    }
    return figure    # 복사 후, 위의 그래프 요소를 다 지우면, 둘 다 체크박스의 영향을 받음


if __name__ == '__main__':
    app.run_server(debug=True)



# Callback is ...
# function that comes at the end of your code
# it accepts input and output
# input : something that changes
# output : id of the thing that we want to changes
# we need to return the result





## Multiple chart layout
# app.layout = html.Div(children=[
#     html.Div(
#         dcc.Graph(
#             figure= dsf.customChart1(Data=Data, attribution=['Gender','JobType'], title='Gender Distribution'),
#             style={'width': '800'}
#         ), style={'display': 'inline-block'}),
#     html.Div(
#         dcc.Graph(
#             figure=dsf.customChart2(Data=Data, xd='Age',yd='Salary', attribution=['Gender','JobType'],
#                      title='Some Title' , color_att=['Gender']),
#             style={'width': '800'}
#         ), style={'display': 'inline-block'})
# ], style={'width': '100%', 'display': 'inline-block'})
