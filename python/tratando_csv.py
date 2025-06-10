import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import sklearn as sk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Leitura dos dados
df = pd.read_csv(r"C:\Projetos\SaaS_churn\Projeto-SaaS\datasets\CSV_Bruto.csv")   ##ALTERAR DE ACORDO COM O COLABORADOR

# Análise inicial dos dados
df.head()
df.isnull().sum()
df.dtypes

# Conversão da coluna 'Churn' para numérica
df['Churn'] = df['Churn'].map({'No': 0, 'Yes': 1})

# Identificação de colunas categóricas e numéricas
cat_cols = df.select_dtypes(include='object').columns.tolist()
num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
df.columns.tolist()

# Limpeza dos nomes das colunas
df.columns = df.columns.str.strip()
df.columns.tolist()

# Tratamento de valores nulos em 'TotalCharges'
df['TotalCharges'].isnull().sum()
df.dropna(subset=['TotalCharges'], inplace=True)
df.isnull().sum().sum()

# Separação de variáveis independentes e alvo
X = df.drop('Churn', axis=1)
y = df['Churn']

# Codificação de variáveis categóricas
X = pd.get_dummies(X, drop_first=True)

# Divisão dos dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinamento do modelo
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Avaliação do modelo
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)

# Salvando o DataFrame processado
df.to_csv(r"C:\Projetos\SaaS_churn\Projeto-SaaS\datasets\CSV_Processado.csv", index=False)  ##ALTERAR DE ACORDO COM O COLABORADOR