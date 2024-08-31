import pandas as pd

def carregar_dados(caminho_arquivo):
    try:
        df = pd.read_csv(caminho_arquivo)
        if df.empty:
            raise ValueError('O arquivo CSV está vazio.')
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f'O arquivo {caminho_arquivo} não foi encontrado.')
    except pd.errors.EmptyDataError:
        raise ValueError('O arquivo CSV está vazio ou não contém dados válidos.')

def limpar_dados(df):
    df = df.dropna()
    return df

def preparar_dados(df):
    df['data'] = pd.to_datetime(df['data'])
    df.set_index('data', inplace=True)
    df_mensal = df.resample('ME').sum()
    return df_mensal
