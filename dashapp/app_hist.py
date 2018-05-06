import dash
import plotly.figure_factory as ff
import dash_html_components as html
import dash_core_components as dcc

import numpy as np

app = dash.Dash()

x = np.random.randn(1000)
hist_data = [x]
group_labels = ['distplot']

fig = ff.create_distplot(hist_data, group_labels)

app.layout = html.Div([
     dcc.Graph(id='my-id', figure=fig)
])


if __name__ == '__main__':
    app.run_server(debug=True)
