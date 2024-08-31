# Script para Análise Exploratória de Dados]

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def gerar_graficos(df):
    plt.figure(figsize=(12, 6))
    
    plt.subplot(2, 2, 1)
    df['vendas'].plot(title='Tendência de Vendas', xlabel='Data', ylabel='Vendas')
    
    plt.subplot(2, 2, 2)
    df.groupby('produto')['vendas'].sum().plot(kind='bar', title='Vendas por Produto', xlabel='Produto', ylabel='Vendas')
    
    plt.subplot(2, 2, 3)
    df['vendas'].plot(kind='hist', bins=30, title='Distribuição de Vendas', xlabel='Vendas')
    
    plt.subplot(2, 2, 4)
    sns.boxplot(x='produto', y='vendas', data=df)
    plt.title('Outliers nas Vendas por Produto')
    
    plt.tight_layout()
    plt.savefig('outputs/analise_exploratoria.png')
    plt.show()
    
def estatisticas_descritivas(df):
    return df.describe()