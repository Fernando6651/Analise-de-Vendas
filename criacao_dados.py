import pandas as pd
import numpy as np
import random

# Configurações
np.random.seed(42)
random.seed(42)

# Definindo o período das vendas
datas = pd.date_range(start='2023-01-01', end='2023-12-31')

# Lista de produtos fictícios
produtos = ['Produto A', 'Produto B', 'Produto C', 'Produto D']

# Gerando os dados
dados = {
    'data': np.random.choice(datas, size=1000),  # 1000 registros
    'produto': np.random.choice(produtos, size=1000),
    'vendas': np.random.poisson(lam=100, size=1000)  # Distribuição de Poisson para simular vendas
}

# Criando o DataFrame
dados_vendas = pd.DataFrame(dados)

# Adicionando uma coluna de preço para cada produto
precos = {
    'Produto A': 10.99,
    'Produto B': 15.49,
    'Produto C': 7.99,
    'Produto D': 12.99
}

dados_vendas['preco'] = dados_vendas['produto'].map(precos)

# Calculando a receita total por venda (preço * quantidade vendida)
dados_vendas['receita'] = dados_vendas['vendas'] * dados_vendas['preco']

# Exibindo as primeiras linhas do dataframe
print(dados_vendas.head())

# Exibindo as primeiras linhas do dataframe
print(dados_vendas.head())

# Exibindo informações gerais do dataframe
print(dados_vendas.info())

# Exibindo uma descrição estatística dos dados
print(dados_vendas.describe())

# Estatísticas descritivas por produto
estatisticas_produto = dados_vendas.groupby('produto').agg({
    'vendas': ['sum', 'mean', 'std', 'min', 'max'],
    'receita': ['sum', 'mean', 'std', 'min', 'max']
}).reset_index()

estatisticas_produto.columns = ['Produto', 'Total Vendas', 'Média Vendas', 'Desvio Padrão Vendas', 'Min Vendas', 'Max Vendas',
                                'Total Receita', 'Média Receita', 'Desvio Padrão Receita', 'Min Receita', 'Max Receita']

print(estatisticas_produto)
