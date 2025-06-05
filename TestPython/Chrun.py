import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = pd.read_csv('https://github.com/DherekSG/Projeto-SaaS/tree/master/TestPython/CSV/model_churn.csv')
df.drop(columns=['customerID'], inplace=True)   

#Pre-processamento
df.dropna(inpace=True)
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

#Separar os dados em variáveis independentes e dependentes

X = df.drop('Churn', axis=1)
y = df['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#Treinamento do modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

#Avaliação do modelo
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

#Exporta o modelo
joblib.dump(model, 'modelo_churn.pkl')
