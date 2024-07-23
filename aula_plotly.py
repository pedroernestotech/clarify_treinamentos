import dash
from dash import dcc, html
from dash.dependencies import Input, Output

import plotly.graph_objects as go 


# Dados
dados_conceitos = dict(
    java =       {'variáveis': 3, 'condicionais': 6, 'loops': 2, 'poo':1, 'funções': 1},
    python =     {'variáveis': 9, 'condicionais': 8, 'loops': 5, 'poo':7, 'funções': 4},
    sql =        {'variáveis': 4, 'condicionais': 2, 'loops': 5, 'poo':4, 'funções': 6},
    golang =     {'variáveis': 6, 'condicionais': 8, 'loops': 9, 'poo':8, 'funções': 3},
    javascript = {'variáveis': 8, 'condicionais': 5, 'loops': 2, 'poo':9, 'funções': 4}
)

color_map = dict(
    java = 'red',
    python = 'blue',
    sql = 'lightblue',
    golang = 'orange',
    javascript = 'yellow'
)

app = dash.Dash(__name__)

# ____________________Layout_____________________

app.layout = html.Div([
    html.H2(
        'Leonardo Alves', style={'textAlign':'center'}
        ),
    html.Div(
        dcc.Dropdown(
            id='dropdown_linguagens',
            options=[
                {'label': 'Java', 'value': 'java'},
                {'label': 'Python', 'value': 'python'},
                {'label': 'SQL', 'value': 'sql'},
                {'label': 'GoLang', 'value': 'golang'},
                {'label': 'JavaScript', 'value': 'javascript'}
            ],
            value=['java'],
            multi=True,
            style={'width': '70%', 'margin': '0 auto'}
        )  
    ),
    dcc.Graph(
        id='scatter_plot'
    )
])                        


# ___________________Callbacks___________________

@app.callback(
    Output('scatter_plot', 'figure'),
    [Input('dropdown_linguagens', 'value')]
)
def atualizar_scatter(linguagens_selecionadas):
    
    scatter_trace = []
    
    for linguagem in linguagens_selecionadas:
        dados_linguagem = dados_conceitos[linguagem]
        for conceito, conhecimento in dados_linguagem.items():
            scatter_trace.append(
                go.Scatter(
                    x=[conceito],
                    y=[conhecimento],
                    mode='markers',
                    name=linguagem.upper(),
                    marker=dict(size=50, color=color_map[linguagem]),
                    showlegend=False
                )
            )
    
    scatter_layout = go.Layout(
        title='Minhas linguagens',
        xaxis=dict(title='Conceitos', showgrid=False),
        yaxis=dict(title='Nível de conhecimento', showgrid=False)
    )
    
    return {'data': scatter_trace, 'layout': scatter_layout}

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
    
    
    
