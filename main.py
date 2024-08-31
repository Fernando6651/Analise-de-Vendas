from dash import dcc, html
import plotly.express as px
import pandas as pd
import dash

# Funções de carregamento e preparação de dados
from src.data_processing import carregar_dados, limpar_dados, preparar_dados

# Carregar e preparar dados
df = carregar_dados('data/vendas_historicas.csv')
df = limpar_dados(df)
df_mensal = preparar_dados(df)

# Atualizar o gráfico de acordo com as colunas disponíveis
fig_vendas_produtos = px.bar(df, x='produto', y='vendas', color='produto', title='Vendas Totais por Produto')

# Verificar se o índice é do tipo datetime
if not pd.api.types.is_datetime64_any_dtype(df.index):
    df.index = pd.to_datetime(df.index)

fig_vendas_diarias = px.line(df, x=df.index, y='vendas', title='Vendas Diárias')

if not pd.api.types.is_datetime64_any_dtype(df_mensal.index):
    df_mensal.index = pd.to_datetime(df_mensal.index)

fig_sazonalidade = px.line(df_mensal, x=df_mensal.index, y='vendas', title='Sazonalidade das Vendas')
fig_vendas_totais = px.line(df_mensal, x=df_mensal.index, y='vendas', title='Vendas Totais ao Longo do Tempo')

# Configurar a aplicação Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Vendas por Produto', children=[
            html.Div([dcc.Graph(figure=fig_vendas_produtos)])
        ]),
        dcc.Tab(label='Vendas Diárias', children=[
            html.Div([dcc.Graph(figure=fig_vendas_diarias)])
        ]),
        dcc.Tab(label='Sazonalidade das Vendas', children=[
            html.Div([dcc.Graph(figure=fig_sazonalidade)])
        ]),
        dcc.Tab(label='Vendas Totais ao Longo do Tempo', children=[
            html.Div([dcc.Graph(figure=fig_vendas_totais)])
        ]),
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
