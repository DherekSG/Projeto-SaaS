# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import f1_score, classification_report, confusion_matrix
import shap
import joblib
import os

SEED = 42
np.random.seed(SEED)
plt.style.use('seaborn-v0_8-darkgrid')

# --- Dataset de exemplo (igual ao seu) ---
def create_sample_dataset(filename="saas_churn_dataset.csv", num_samples=1000):
    data = {
        'CustomerID': [f'CUST_{i:04d}' for i in range(num_samples)],
        'TenureMonths': np.random.randint(1, 72, num_samples),
        'MonthlyCharge': np.random.uniform(20, 200, num_samples),
        'Contract': np.random.choice(['Month-to-Month', 'One Year', 'Two Year'], num_samples, p=[0.6, 0.25, 0.15]),
        'PaymentMethod': np.random.choice(['Bank Transfer', 'Credit Card', 'Electronic Check', 'Mailed Check'], num_samples),
        'PaperlessBilling': np.random.choice(['Yes', 'No'], num_samples),
        'OnlineSecurity': np.random.choice(['Yes', 'No', 'No internet service'], num_samples),
        'TechSupport': np.random.choice(['Yes', 'No', 'No internet service'], num_samples),
        'Dependents': np.random.choice(['Yes', 'No'], num_samples),
        'MultipleLines': np.random.choice(['Yes', 'No', 'No phone service'], num_samples),
        'Age': np.random.randint(18, 80, num_samples),
        'SupportTicketsLast6Months': np.random.poisson(1.5, num_samples),
        'UsageFrequency': np.random.choice(['Daily', 'Weekly', 'Monthly', 'Rarely'], num_samples, p=[0.5, 0.3, 0.15, 0.05]),
        'Churn': np.random.choice(['Yes', 'No'], num_samples, p=[0.26, 0.74])
    }
    df = pd.DataFrame(data)
    df['TotalCharges'] = df.apply(lambda row: row['TenureMonths'] * row['MonthlyCharge'] * np.random.uniform(0.8, 1.2) if row['TenureMonths'] > 0 else 0, axis=1)
    for col in ['TechSupport', 'OnlineSecurity']:
        mask = np.random.choice([True, False], size=num_samples, p=[0.05, 0.95])
        df.loc[mask, col] = np.nan
    df.to_csv(filename, index=False)
    return df

dataset_filename = "saas_churn_dataset.csv"
if not os.path.exists(dataset_filename):
    df_churn = create_sample_dataset(dataset_filename)
else:
    df_churn = pd.read_csv(dataset_filename)

df_churn['TotalCharges'] = pd.to_numeric(df_churn['TotalCharges'], errors='coerce')
df_churn['TotalCharges'].fillna(df_churn['TotalCharges'].median(), inplace=True)
le = LabelEncoder()
df_churn['Churn'] = le.fit_transform(df_churn['Churn'])
target_classes = le.classes_

if 'CustomerID' in df_churn.columns:
    df_churn = df_churn.drop('CustomerID', axis=1)

TARGET_COL = 'Churn'
numerical_cols = df_churn.select_dtypes(include=np.number).columns.tolist()
numerical_cols.remove(TARGET_COL)
categorical_cols = df_churn.select_dtypes(include='object').columns.tolist()

X = df_churn.drop(TARGET_COL, axis=1)
y = df_churn[TARGET_COL]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED, stratify=y)

# --- Pré-processamento ---
numerical_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])
categorical_transformer = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', drop='first'))
])
preprocessor = ColumnTransformer([
    ('num', numerical_transformer, numerical_cols),
    ('cat', categorical_transformer, categorical_cols)
])

# --- Modelos ---
models = {
    "Random Forest": RandomForestClassifier(random_state=SEED, class_weight='balanced'),
    "XGBoost": XGBClassifier(random_state=SEED, use_label_encoder=False, eval_metric='logloss')
}

for name, model in models.items():
    print(f"\nTreinando: {name}")
    pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('classifier', model)
    ])
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    print(f"F1-score (teste): {f1_score(y_test, y_pred):.4f}")
    print(classification_report(y_test, y_pred, target_names=target_classes))
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=target_classes, yticklabels=target_classes)
    plt.title(f'Matriz de Confusão - {name}')
    plt.xlabel('Previsto')
    plt.ylabel('Verdadeiro')
    plt.tight_layout()
    plt.savefig(f'confusion_matrix_{name.replace(" ", "_")}.png')
    plt.show()

    # --- SHAP ---
    print(f"Calculando SHAP para {name}...")
    # Pega os dados já pré-processados
    X_train_proc = preprocessor.fit_transform(X_train)
    X_test_proc = preprocessor.transform(X_test)
    feature_names = (
        numerical_cols +
        list(preprocessor.named_transformers_['cat']['onehot'].get_feature_names_out(categorical_cols))
    )

    if name == "Random Forest":
        explainer = shap.TreeExplainer(model)
    else:  # XGBoost
        explainer = shap.Explainer(model, X_train_proc, feature_names=feature_names)

    shap_values = explainer(X_test_proc)

    # Summary plot
    shap.summary_plot(shap_values, X_test_proc, feature_names=feature_names, show=False)
    plt.tight_layout()
    plt.savefig(f'shap_summary_{name.replace(" ", "_")}.png')
    plt.close()

    # Bar plot
    shap.plots.bar(shap_values, show=False)
    plt.tight_layout()
    plt.savefig(f'shap_bar_{name.replace(" ", "_")}.png')
    plt.close()

    # Waterfall plot (primeira amostra)
    shap.plots.waterfall(shap_values[0], show=False)
    plt.tight_layout()
    plt.savefig(f'shap_waterfall_{name.replace(" ", "_")}.png')
    plt.close()

    # Force plot (primeira amostra)
    force_plot = shap.plots.force(shap_values[0], matplotlib=True, show=False)
    plt.tight_layout()
    plt.savefig(f'shap_force_{name.replace(" ", "_")}.png')
    plt.close()

    print(f"Gráficos SHAP salvos para {name}.")

    # Salvar modelo
    joblib.dump(pipeline, f"modelo_{name.replace(' ', '_').lower()}.joblib")
    print(f"Modelo '{name}' salvo.")

print("\n--- Script concluído ---")