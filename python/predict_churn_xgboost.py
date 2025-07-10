import joblib
import numpy as np
from sklearn.metrics import accuracy_score, f1_score, recall_score

def carregar_modelo_e_prever(X_novo, model_path="xgboost_churn_model.pkl", threshold_path="xgboost_churn_threshold.pkl"):
    """
    Aplica predição de churn usando modelo XGBoost treinado.

    Parâmetros:
    - X_novo: DataFrame já pré-processado (sem a coluna 'churn')
    - model_path: caminho do modelo .pkl
    - threshold_path: caminho do threshold .pkl

    Retorna:
    - y_pred: array de predições (0 ou 1)
    - y_proba: probabilidades da classe 1 (churn)
    """
    modelo = joblib.load(model_path)
    threshold = joblib.load(threshold_path)

    y_proba = modelo.predict_proba(X_novo)[:, 1]
    y_pred = (y_proba >= threshold).astype(int)

    return y_pred, y_proba

# Exemplo de uso:
if __name__ == "__main__":
    import pandas as pd

    # Carregue seu dataset de teste já pré-processado
    df_test = pd.read_csv("dataset_preprocessado_com_churn.csv")
    X_test = df_test.drop("churn", axis=1)
    y_true = df_test["churn"].values

    y_pred, y_proba = carregar_modelo_e_prever(X_test)

    acc = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)

    print(f"Accuracy: {acc:.4f}")
    print(f"F1-score: {f1:.4f}")
    print(f"Recall: {recall:.4f}")
