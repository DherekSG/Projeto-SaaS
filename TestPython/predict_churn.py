import pandas as pd
from joblib import load

# Aqui agt carrega
model = load('model.joblib')

# Aqui os dados que vem do csv
novos = pd.read_csv("novos_clientes.csv")  # deve conter as colunas esperadas
risco = model.predict_proba(novos[['atendimentos', 'nota_nps']])[:, 1]

# Aqui salva
novos['risco_churn'] = risco
novos.to_csv("previsoes.csv", index=False)
