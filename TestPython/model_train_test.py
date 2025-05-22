import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#caminho
caminho = "model_churn"
#read
df = pd.read_csv(caminho)
df.head()
print("Dimensoes:" df.shape)

df.info()
df.isnull().sum()

#limpando valores invalidos
df.drop(columns=['customerID'], inplace=True)
print("Valores nao numericos TotalCharges:", df[pd.to_numeric(df['TotalCharges'], errors='coerce').isna()].shape[0])

#Convertendo para float
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

#verificar valores nulos apos conversao
print(df.isnull().sum())

#removendo linhas com valores null
df.dropna(inplace=True)

#convertendo valores yes/no em binario
df['Churn'] = df['Churn'].map({'Yes':1, 'No':0})

#identificador de colunas categoricas
cat_cols = df.select_dtypes(include=['object']).columns.tolist()

#aplicar one-hot encoding
df_encoded = pd.get_dummies(df, columns=cat_cols, drop_first=True)





#plotagem do alvo
sns.countplot(x='Churn', data=df)
plt.title('Distribuicao da variavel alvo (Churn)')
plt.xlabel('Churn (0 = Nao, 1 = Sim)')
plt.ylabel('Quantidade')
plt.show()

#Proporcoes
print(df['Churn'].value_counts(normalize=True))

#distribuicoes de variaveis
num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
for col in num_cols:
    plt.figure(figsize=(6, 4))
    sns.histplot(data=df, x=col, hue='Churn', kde=True, bins=30)
    plt.title(f'Distribuicao de {col} por Churn')
    plt.xlabel(col)
    plt.ylabel('Contagem')
    plt.show()

#comparar churn por variaveis categoricas
cat_cols_plot = ['Contract', 'InternetService', 'PaymentMethod', 'OnlineSecurity', 'TechSupport']
for col in cat_cols_plot:
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x=col, hue='Churn')
    plt.title(f'Churn for {col}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

#matriz de correlacao entre variaveis numericas e churn
plt.figure(figsize=(10, 6))
corr = df_encoded.corr()
sns.heatmap(corr[['Churn']].sort_values(by='Churn', ascending=False), annot=True, cmap='coolwarm')
plt.title('Correlacao das variaveis com o Churn')
plt.show()
    



