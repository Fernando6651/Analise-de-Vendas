import plotly.express as px
import pandas as pd


def plotar_previsao_vs_real(y_test, y_pred):
    df_comparacao = pd.DataFrame({'Real': y_test, 'Previsão': y_pred}, index=y_test.index)
    fig = px.line(df_comparacao, title='Previsão vs Real')
    fig.update_layout(xaxis_title='Tempo', yaxis_title='Receita')
    fig.write_image('outputs/previsao_vs_real.png')
    return fig

def plotar_sazonalidade(df):
    fig = px.line(df, x=df.index, y='vendas', title='Sazonalidade das Vendas')
    fig.update_layout(xaxis_title='Data', yaxis_title='Vendas')
    fig.write_image('outputs/sazonalidade.png')
    return fig

def plotar_vendas_produtos(df):
    fig = px.bar(df.groupby('produto').sum().reset_index(), x='produto', y='vendas', title='Vendas Totais por Produto')
    fig.update_layout(xaxis_title='Produto', yaxis_title='Vendas')
    fig.write_image('outputs/vendas_produtos.png')
    return fig

def plotar_vendas_totais(df):
    fig = px.line(df, x=df.index, y='vendas', title='Vendas Totais ao Longo do Tempo')
    fig.update_layout(xaxis_title='Data', yaxis_title='Vendas Totais')
    fig.write_image('outputs/vendas_totais.png')
    return fig
