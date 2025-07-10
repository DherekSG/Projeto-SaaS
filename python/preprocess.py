import pandas as pd
from sklearn.preprocessing import StandardScaler

# Carregar o dataset (atenção à barra invertida duplicada)
df = pd.read_csv("C:\\Users\\juanm\\Desktop\\Dataset_Energia\\Dataset_Bruto.csv")

# Remover colunas irrelevantes
remover_colunas = ['id', 'date_activ', 'date_end', 'date_modif_prod', 'date_renewal']
df_clean = df.drop(columns=remover_colunas)

# Padronizar strings (strip e upper)
for col in df_clean.select_dtypes(include='object').columns:
    df_clean[col] = df_clean[col].astype(str).str.strip().str.upper()

# Corrigir digitação: get_dummies
df_clean = pd.get_dummies(df_clean, drop_first=True)

# Separar features e alvo
X = df_clean.drop("churn", axis=1)
y = df_clean["churn"]

# Normalizar os dados
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Recriar DataFrame normalizado
X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)


df_final = X_scaled_df.copy()
df_final["churn"] = y.values

df_final.to_csv("dataset_preprocessado_com_churn.csv", index=False)

print("Pré-processamento concluído e arquivo salvo com sucesso!")