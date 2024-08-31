from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
import pandas as pd

def treinar_modelo(df):
    X = df[['vendas']]  # Variáveis independentes
    y = df['receita']  # Variável dependente
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    modelo = RandomForestRegressor()
    modelo.fit(X_train, y_train)
    
    y_pred = modelo.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    
    return modelo, mse, mae
