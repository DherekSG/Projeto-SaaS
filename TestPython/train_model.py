# --- Importações Essenciais ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, classification_report
import joblib # Para exportar o modelo (alternativa ao pickle, mais eficiente para objetos numpy)
import os

print("Bibliotecas importadas com sucesso.")

# --- Configurações Globais (Opcional) ---
SEED = 42 # Para reprodutibilidade
np.random.seed(SEED)
plt.style.use('seaborn-v0_8-darkgrid') # Estilo dos gráficos

# --- Geração de Dataset de Exemplo (Substitua pelo seu dataset real) ---
def create_sample_dataset(filename="saas_churn_dataset.csv", num_samples=1000):
    """Cria um dataset de exemplo para churn em SaaS."""
    print(f"Gerando dataset de exemplo: {filename}...")
    data = {
        'CustomerID': [f'CUST_{i:04d}' for i in range(num_samples)],
        'TenureMonths': np.random.randint(1, 72, num_samples),
        'MonthlyCharge': np.random.uniform(20, 200, num_samples),
        'TotalCharges': lambda df: df['TenureMonths'] * df['MonthlyCharge'] * np.random.uniform(0.8, 1.2, num_samples), # Adiciona variabilidade
        'Contract': np.random.choice(['Month-to-Month', 'One Year', 'Two Year'], num_samples, p=[0.6, 0.25, 0.15]),
        'PaymentMethod': np.random.choice(['Bank Transfer', 'Credit Card', 'Electronic Check', 'Mailed Check'], num_samples),
        'PaperlessBilling': np.random.choice(['Yes', 'No'], num_samples),
        'OnlineSecurity': np.random.choice(['Yes', 'No', 'No internet service'], num_samples),
        'TechSupport': np.random.choice(['Yes', 'No', 'No internet service'], num_samples),
        'Dependents': np.random.choice(['Yes', 'No'], num_samples),
        'MultipleLines': np.random.choice(['Yes', 'No', 'No phone service'], num_samples),
        'Age': np.random.randint(18, 80, num_samples),
        'SupportTicketsLast6Months': np.random.poisson(1.5, num_samples), # Média de 1.5 tickets
        'UsageFrequency': np.random.choice(['Daily', 'Weekly', 'Monthly', 'Rarely'], num_samples, p=[0.5, 0.3, 0.15, 0.05]),
        'Churn': np.random.choice(['Yes', 'No'], num_samples, p=[0.26, 0.74]) # Taxa de churn de ~26%
    }
    df = pd.DataFrame(data)
    df['TotalCharges'] = df.apply(lambda row: row['TenureMonths'] * row['MonthlyCharge'] * np.random.uniform(0.8, 1.2) if row['TenureMonths'] > 0 else 0, axis=1)

    # Adicionar alguns NaNs para simular dados do mundo real
    for col in ['TechSupport', 'OnlineSecurity']:
        mask = np.random.choice([True, False], size=num_samples, p=[0.05, 0.95]) # 5% de NaNs
        df.loc[mask, col] = np.nan

    df.to_csv(filename, index=False)
    print(f"Dataset de exemplo '{filename}' criado com {num_samples} amostras.")
    return df

# Verifica se o dataset de exemplo existe, senão cria
dataset_filename = "saas_churn_dataset.csv"
if not os.path.exists(dataset_filename):
    df_churn = create_sample_dataset(dataset_filename)
else:
    print(f"Dataset '{dataset_filename}' já existe. Carregando...")

# 1. Carregamento e Inspeção do Dataset
print("\n--- 1. Carregamento e Inspeção do Dataset ---")
try:
    df_churn = pd.read_csv(dataset_filename)
    print(f"Dataset '{dataset_filename}' carregado com sucesso.")
except FileNotFoundError:
    print(f"ERRO: Arquivo '{dataset_filename}' não encontrado. Execute a criação do dataset de exemplo ou forneça o caminho correto.")
    exit()

print("\nPrimeiras 5 linhas do dataset:")
print(df_churn.head())

print("\nInformações gerais do dataset:")
df_churn.info()

print("\nEstatísticas descritivas do dataset:")
print(df_churn.describe(include='all'))

print("\nVerificação de valores nulos:")
print(df_churn.isnull().sum())

print("\nContagem de valores únicos por coluna:")
for col in df_churn.columns:
    print(f"{col}: {df_churn[col].nunique()} valores únicos")

# Identificar a coluna alvo
TARGET_COL = 'Churn'

# 2. Limpeza e Pré-processamento dos Dados
print("\n--- 2. Limpeza e Pré-processamento dos Dados ---")

# Remover colunas irrelevantes (ex: CustomerID)
if 'CustomerID' in df_churn.columns:
    df_churn = df_churn.drop('CustomerID', axis=1)
    print("Coluna 'CustomerID' removida.")

# Converter 'TotalCharges' para numérico, tratando erros
if 'TotalCharges' in df_churn.columns:
    df_churn['TotalCharges'] = pd.to_numeric(df_churn['TotalCharges'], errors='coerce')
    # Se houver NaNs após a conversão (ex: espaços em branco), podemos imputá-los.
    # Para este exemplo, vamos imputar com a mediana se houver NaNs em TotalCharges.
    if df_churn['TotalCharges'].isnull().any():
        print(f"Valores nulos encontrados em 'TotalCharges' após conversão: {df_churn['TotalCharges'].isnull().sum()}")
        median_total_charges = df_churn['TotalCharges'].median()
        df_churn['TotalCharges'].fillna(median_total_charges, inplace=True)
        print(f"'TotalCharges' nulos preenchidos com a mediana ({median_total_charges:.2f}).")

# Converter a coluna alvo para formato numérico (0 e 1)
if df_churn[TARGET_COL].dtype == 'object':
    le = LabelEncoder()
    df_churn[TARGET_COL] = le.fit_transform(df_churn[TARGET_COL])
    print(f"Coluna alvo '{TARGET_COL}' convertida para numérico: {dict(zip(le.classes_, le.transform(le.classes_)))}")
    # Guardar as classes para referência futura, se necessário
    target_classes = le.classes_

# Identificar colunas numéricas e categóricas
numerical_cols = df_churn.select_dtypes(include=np.number).columns.tolist()
numerical_cols.remove(TARGET_COL) # Remover a coluna alvo da lista de features numéricas

categorical_cols = df_churn.select_dtypes(include='object').columns.tolist()

print(f"\nColunas numéricas identificadas: {numerical_cols}")
print(f"Colunas categóricas identificadas: {categorical_cols}")

# Divisão dos dados em features (X) e alvo (y)
X = df_churn.drop(TARGET_COL, axis=1)
y = df_churn[TARGET_COL]

# Divisão em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=SEED, stratify=y)
print(f"\nDados divididos em treino ({X_train.shape[0]} amostras) e teste ({X_test.shape[0]} amostras).")
print(f"Distribuição do Churn no treino: \n{y_train.value_counts(normalize=True)}")
print(f"Distribuição do Churn no teste: \n{y_test.value_counts(normalize=True)}")

# 3. Análise Exploratória (EDA) - Focada no conjunto de treino para evitar data leakage
print("\n--- 3. Análise Exploratória (EDA) ---")
df_train_eda = X_train.copy()
df_train_eda[TARGET_COL] = y_train

# Distribuição da variável alvo
plt.figure(figsize=(6, 4))
sns.countplot(x=TARGET_COL, data=df_train_eda)
plt.title('Distribuição de Churn (Conjunto de Treino)')
plt.savefig('eda_churn_distribution.png')
plt.show()
print("Gráfico da distribuição de churn salvo como 'eda_churn_distribution.png'")

# Análise de features numéricas vs Churn
for col in numerical_cols:
    if col in df_train_eda.columns: # Checar se a coluna existe após remoções
        plt.figure(figsize=(10, 4))
        plt.subplot(1, 2, 1)
        sns.histplot(df_train_eda[col], kde=True, bins=30)
        plt.title(f'Distribuição de {col}')
        plt.subplot(1, 2, 2)
        sns.boxplot(x=TARGET_COL, y=col, data=df_train_eda)
        plt.title(f'{col} vs Churn')
        plt.tight_layout()
        plt.savefig(f'eda_{col}_vs_churn.png')
        plt.show()
        print(f"Gráfico de '{col} vs Churn' salvo como 'eda_{col}_vs_churn.png'")

# Análise de features categóricas vs Churn
for col in categorical_cols:
     if col in df_train_eda.columns: # Checar se a coluna existe
        plt.figure(figsize=(10, 5))
        sns.countplot(x=col, hue=TARGET_COL, data=df_train_eda, order=df_train_eda[col].value_counts().index)
        plt.title(f'{col} vs Churn')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(f'eda_{col}_vs_churn.png')
        plt.show()
        print(f"Gráfico de '{col} vs Churn' salvo como 'eda_{col}_vs_churn.png'")

# Matriz de correlação (apenas para features numéricas após pré-processamento, se necessário)
# Neste ponto, as features categóricas ainda não foram transformadas.
# Poderíamos fazer uma cópia e aplicar one-hot encoding apenas para a correlação,
# mas é mais comum fazer isso após o pipeline de pré-processamento.
# Por ora, vamos correlacionar as numéricas originais com o target.
if numerical_cols: # Verifica se há colunas numéricas
    corr_matrix = df_train_eda[numerical_cols + [TARGET_COL]].corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Matriz de Correlação (Features Numéricas e Churn)')
    plt.savefig('eda_correlation_matrix.png')
    plt.show()
    print("Matriz de correlação salva como 'eda_correlation_matrix.png'")


# 4. Engenharia de Atributos (Feature Engineering)
print("\n--- 4. Engenharia de Atributos (Feature Engineering) ---")
# Esta etapa é altamente dependente do domínio e dos insights da EDA.
# Exemplos (podem ser adicionados ao pipeline de pré-processamento):
# - Criação de novas features: ex: 'TenureToAgeRatio' = TenureMonths / Age
# - Binning de features numéricas: ex: transformar 'Age' em grupos etários
# - Interações entre features: ex: 'MonthlyCharge_x_ContractType'

# Por enquanto, vamos manter simples e focar no pipeline de pré-processamento básico.
# Adicionaremos as transformações diretamente no ColumnTransformer.
# Exemplo simples:
# X_train['TenureInYears'] = X_train['TenureMonths'] / 12
# X_test['TenureInYears'] = X_test['TenureMonths'] / 12
# numerical_cols.append('TenureInYears') # Adicionar à lista se criar novas features
# print("Feature 'TenureInYears' criada.")

# No nosso caso, vamos definir os transformadores para uso posterior.
# Pré-processador para features numéricas: imputação + scaling
numerical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')), # Imputar NaNs com a mediana
    ('scaler', StandardScaler()) # Padronizar features
])

# Pré-processador para features categóricas: imputação + one-hot encoding
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')), # Imputar NaNs com o valor mais frequente
    ('onehot', OneHotEncoder(handle_unknown='ignore', drop='first')) # 'drop=first' para evitar multicolinearidade
])

# Criar o ColumnTransformer para aplicar transformações diferentes em colunas diferentes
# É importante garantir que as listas de colunas estejam corretas e correspondam às colunas em X_train/X_test
# Re-identificar colunas caso tenham sido modificadas ou removidas.
current_numerical_cols = [col for col in numerical_cols if col in X_train.columns]
current_categorical_cols = [col for col in categorical_cols if col in X_train.columns]

print(f"Colunas numéricas para transformador: {current_numerical_cols}")
print(f"Colunas categóricas para transformador: {current_categorical_cols}")

# Checar se há colunas a serem processadas
if not current_numerical_cols and not current_categorical_cols:
    print("ERRO: Nenhuma coluna numérica ou categórica identificada para o pré-processamento. Verifique os passos anteriores.")
    # Poderia adicionar um fallback ou parar, dependendo da lógica desejada.
    # Para este script, se não houver colunas, o ColumnTransformer pode falhar ou não fazer nada.

transformers_list = []
if current_numerical_cols:
    transformers_list.append(('num', numerical_transformer, current_numerical_cols))
if current_categorical_cols:
    transformers_list.append(('cat', categorical_transformer, current_categorical_cols))

if not transformers_list:
    print("Nenhum transformador foi adicionado. Verifique as listas de colunas.")
    # Decide como proceder: pode ser um erro ou um caso onde não há colunas para transformar
    # (embora improvável para um dataset de churn típico).
    # Para este exemplo, prosseguiremos, mas na prática, isso indicaria um problema.
    preprocessor = None # Ou uma estrutura vazia, dependendo do que os modelos esperam
else:
    preprocessor = ColumnTransformer(transformers=transformers_list)

print("Pré-processador (ColumnTransformer) definido.")

# 5. Modelagem e Comparação de Algoritmos
print("\n--- 5. Modelagem e Comparação de Algoritmos ---")

models = {
    "Logistic Regression": LogisticRegression(random_state=SEED, solver='liblinear', class_weight='balanced'),
    "Random Forest": RandomForestClassifier(random_state=SEED, class_weight='balanced'),
    "Gradient Boosting": GradientBoostingClassifier(random_state=SEED),
    # "SVC": SVC(random_state=SEED, probability=True, class_weight='balanced'), # Pode ser lento sem GridSearchCV
    # "KNN": KNeighborsClassifier() # Geralmente precisa de features escaladas, o que nosso pipeline faz
}

results = {}
best_model_name = None
best_model_pipeline = None
best_f1_score = 0

# Validação Cruzada Estratificada
cv_strategy = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEED)

for name, model in models.items():
    print(f"\nTreinando e avaliando: {name}")

    # Criar pipeline completo: pré-processador + modelo
    if preprocessor: # Se houver passos de pré-processamento
        pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                   ('classifier', model)])
    else: # Se não houver pré-processamento (improvável, mas para cobrir o caso)
        pipeline = Pipeline(steps=[('classifier', model)])

    # Treinamento
    pipeline.fit(X_train, y_train)

    # Previsões
    y_pred_train = pipeline.predict(X_train)
    y_pred_test = pipeline.predict(X_test)
    y_proba_test = pipeline.predict_proba(X_test)[:, 1] if hasattr(model, "predict_proba") else None

    # Métricas
    accuracy_train = accuracy_score(y_train, y_pred_train)
    accuracy_test = accuracy_score(y_test, y_pred_test)
    precision_test = precision_score(y_test, y_pred_test, zero_division=0)
    recall_test = recall_score(y_test, y_pred_test, zero_division=0)
    f1_test = f1_score(y_test, y_pred_test, zero_division=0)
    roc_auc_test = roc_auc_score(y_test, y_proba_test) if y_proba_test is not None else 'N/A'

    results[name] = {
        "Accuracy Train": accuracy_train,
        "Accuracy Test": accuracy_test,
        "Precision Test": precision_test,
        "Recall Test": recall_test,
        "F1 Test": f1_test,
        "ROC AUC Test": roc_auc_test,
        "Confusion Matrix": confusion_matrix(y_test, y_pred_test)
    }

    print(f"  F1-score (Teste) para {name}: {f1_test:.4f}")

    # Guardar o melhor modelo com base no F1-score no conjunto de teste
    if f1_test > best_f1_score:
        best_f1_score = f1_test
        best_model_name = name
        best_model_pipeline = pipeline # Salvar o pipeline inteiro

    # Validação Cruzada (exemplo com F1-score)
    # Nota: A validação cruzada deve ser feita nos dados de treino para evitar data leakage do teste final.
    # O pipeline já inclui o pré-processamento, então ele será aplicado corretamente em cada fold.
    if preprocessor:
        cv_pipeline = Pipeline(steps=[('preprocessor', preprocessor), ('classifier', model)])
    else:
        cv_pipeline = Pipeline(steps=[('classifier', model)])

    try:
        cv_scores = cross_val_score(cv_pipeline, X_train, y_train, cv=cv_strategy, scoring='f1_weighted', n_jobs=-1)
        results[name]["CV F1 Weighted (mean)"] = cv_scores.mean()
        results[name]["CV F1 Weighted (std)"] = cv_scores.std()
        print(f"  Cross-Validation F1 Weighted (mean) para {name}: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
    except Exception as e:
        print(f"  Erro na validação cruzada para {name}: {e}")
        results[name]["CV F1 Weighted (mean)"] = "N/A"
        results[name]["CV F1 Weighted (std)"] = "N/A"


print("\n--- 6. Avaliação de Métricas ---")
results_df = pd.DataFrame(results).T.sort_values(by="F1 Test", ascending=False)
print("\nResultados Comparativos dos Modelos:")
print(results_df[['Accuracy Test', 'Precision Test', 'Recall Test', 'F1 Test', 'ROC AUC Test', 'CV F1 Weighted (mean)']])

if best_model_name:
    print(f"\nMelhor modelo selecionado: {best_model_name} com F1-score de {best_f1_score:.4f}")
    print(f"\nRelatório de Classificação para {best_model_name} (no conjunto de teste):")
    y_pred_best = best_model_pipeline.predict(X_test)
    print(classification_report(y_test, y_pred_best, target_names=[str(cls) for cls in target_classes] if 'target_classes' in locals() else ['0', '1']))

    print(f"\nMatriz de Confusão para {best_model_name} (no conjunto de teste):")
    cm = confusion_matrix(y_test, y_pred_best)
    plt.figure(figsize=(6,4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=target_classes if 'target_classes' in locals() else ['Não Churn', 'Churn'],
                yticklabels=target_classes if 'target_classes' in locals() else ['Não Churn', 'Churn'])
    plt.xlabel('Previsto')
    plt.ylabel('Verdadeiro')
    plt.title(f'Matriz de Confusão - {best_model_name}')
    plt.savefig(f'confusion_matrix_{best_model_name.replace(" ", "_")}.png')
    plt.show()
    print(f"Matriz de confusão para '{best_model_name}' salva.")

    # Opcional: Otimização de Hiperparâmetros para o melhor modelo (ex: com GridSearchCV)
    # Exemplo para RandomForest (pode ser demorado):
    if best_model_name == "Random Forest" and isinstance(best_model_pipeline.named_steps['classifier'], RandomForestClassifier):
        print(f"\nIniciando otimização de hiperparâmetros para {best_model_name} (pode demorar)...")
        # Definir pipeline apenas com o pré-processador para GridSearchCV
        # pois o GridSearchCV irá adicionar o estimador
        pipeline_for_grid = Pipeline(steps=[('preprocessor', preprocessor)])
        
        # Parâmetros para RandomForest
        param_grid = {
            'classifier__n_estimators': [100, 200], # Adicionar mais se tiver tempo: 300
            'classifier__max_depth': [None, 10, 20], # Adicionar mais: 30
            'classifier__min_samples_split': [2, 5], # Adicionar mais: 10
            'classifier__min_samples_leaf': [1, 2]   # Adicionar mais: 4
        }
        
        # Modelo base para GridSearchCV
        rf_model_for_grid = RandomForestClassifier(random_state=SEED, class_weight='balanced')
        
        # Pipeline completo para GridSearchCV
        full_pipeline_for_grid = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', rf_model_for_grid)
        ])

        grid_search = GridSearchCV(full_pipeline_for_grid, param_grid, cv=cv_strategy, scoring='f1_weighted', n_jobs=-1, verbose=1)
        
        try:
            grid_search.fit(X_train, y_train)
            print(f"Melhores hiperparâmetros encontrados para {best_model_name}: {grid_search.best_params_}")
            best_model_pipeline_tuned = grid_search.best_estimator_ # Pipeline já otimizado
            
            # Reavaliar o modelo otimizado
            y_pred_tuned = best_model_pipeline_tuned.predict(X_test)
            f1_tuned = f1_score(y_test, y_pred_tuned)
            print(f"F1-score do modelo otimizado ({best_model_name}) no teste: {f1_tuned:.4f}")
            
            if f1_tuned > best_f1_score:
                print("Modelo otimizado superou o modelo anterior. Atualizando melhor modelo.")
                best_f1_score = f1_tuned
                best_model_pipeline = best_model_pipeline_tuned
                # (Re)imprimir relatório de classificação e matriz de confusão para o modelo otimizado
                print(f"\nRelatório de Classificação para {best_model_name} (Otimizado):")
                print(classification_report(y_test, y_pred_tuned, target_names=[str(cls) for cls in target_classes] if 'target_classes' in locals() else ['0', '1']))
                cm_tuned = confusion_matrix(y_test, y_pred_tuned)
                plt.figure(figsize=(6,4))
                sns.heatmap(cm_tuned, annot=True, fmt='d', cmap='Blues',
                            xticklabels=target_classes if 'target_classes' in locals() else ['Não Churn', 'Churn'],
                            yticklabels=target_classes if 'target_classes' in locals() else ['Não Churn', 'Churn'])
                plt.xlabel('Previsto')
                plt.ylabel('Verdadeiro')
                plt.title(f'Matriz de Confusão - {best_model_name} (Otimizado)')
                plt.savefig(f'confusion_matrix_{best_model_name.replace(" ", "_")}_tuned.png')
                plt.show()

        except Exception as e:
            print(f"Erro durante GridSearchCV para {best_model_name}: {e}")
else:
    print("Nenhum modelo foi treinado com sucesso ou avaliado.")


# 7. Exportação do Modelo (.pkl ou .joblib)
print("\n--- 7. Exportação do Modelo ---")
if best_model_pipeline:
    model_filename = f"melhor_modelo_churn_{best_model_name.replace(' ', '_').lower()}.joblib"
    try:
        joblib.dump(best_model_pipeline, model_filename)
        print(f"Melhor modelo ('{best_model_name}') salvo como '{model_filename}'")

        # Exemplo de como carregar o modelo (para teste)
        loaded_model = joblib.load(model_filename)
        print(f"Modelo '{model_filename}' carregado com sucesso para verificação.")
        # Testar se o modelo carregado funciona
        # y_pred_loaded = loaded_model.predict(X_test)
        # print(f"F1-score do modelo carregado no teste: {f1_score(y_test, y_pred_loaded):.4f}")

    except Exception as e:
        print(f"Erro ao salvar o modelo: {e}")
else:
    print("Nenhum modelo foi selecionado como o melhor, portanto, nenhum modelo foi exportado.")

#>>>>>>> 79b128c05c6cab56f64ce9c184e651785d9d448a
print("\n--- Script de Treinamento Concluído ---")