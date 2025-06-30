# 📊 Projeto SaaS - Análise de Clientes e Previsão de Churn

## 🧠 Visão Geral

Este projeto tem como objetivo o desenvolvimento de uma aplicação SaaS voltada para pequenas empresas ou profissionais autônomos. A plataforma permitirá o cadastro de clientes, atendimentos e feedbacks, além da geração de relatórios visuais e previsão de churn (abandono de clientes) com técnicas de Machine Learning.

## 🚀 Funcionalidades

- Cadastro de clientes, atendimentos e feedbacks via interface web
- Previsão de churn com script Python e algoritmos de ML
- Visualização de métricas como NPS, churn e satisfação média com Power BI
- Modo demo com dados simulados

## 🧱 Tecnologias Utilizadas

### 💻 Backend:
- PHP (com PDO para PostgreSQL)
- PostgreSQL (estrutura relacional com tabelas normalizadas)

### 🌐 Frontend:
- HTML5 + CSS3 (com Bootstrap)
- Formulários integrados ao backend

### 🧠 Machine Learning:
- Python (pandas, scikit-learn, joblib)
- Modelo de regressão treinado com dados reais simulados
- Exportação de previsões para CSV e/ou banco de dados

### 📊 Visualização:
- Power BI (dashboards de churn, NPS, base ativa, etc.)

---
## 📁 Estrutura de Pastas

```
Projeto-SaaS/
├── backend/               # Scripts PHP
│   ├── conexao.php
│   ├── inserir_cliente.php
│   ├── inserir_feedback.php
│   └── listar_clientes.php
├── frontend/              # Formulários HTML
│   ├── cadastro_cliente.html
│   ├── cadastro_feedback.html
│   └── login.html
├── python/                # Scripts de ML
│   ├── churn_model.py
│   ├── predict_churn.py
│   └── dataset.csv
├── sql/                   # Scripts SQL
│   ├── schema.sql
│   └── dados_teste.sql
├── docs/                  # Documentação e diagramas
│   ├── diagrama.dbml
│   └── arquitetura.md
└── README.md
```

---

## 🧪 Como Executar Localmente

### 1. Banco de Dados
- Instale PostgreSQL e crie o banco `projeto_saas`
- Execute `sql/schema.sql` para criar as tabelas
- Execute `sql/dados_teste.sql` para inserir dados fictícios

### 2. Backend
- Configure `conexao.php` com seu usuário e senha local
- Acesse os formulários via navegador (ex: `cadastro_cliente.html`)

### 3. Python (ML)
- Execute `churn_model.py` para treinar o modelo
- Execute `predict_churn.py` para gerar previsões (salvas em CSV ou banco)

### Requisitos
- PHP + XAMPP
- PostgreSQL
- Python 3.x
- Power BI Desktop

---


## 👥 Equipe

| Nome    | Função |
|---------|--------|
| **[Dherek](https://github.com/DherekSG)** | Líder técnico geral, integração de módulos, Python |
| **[Tego](https://github.com/TiagoRochaDSantos)**   | Backend em PHP e integração com Python |
| **[Hey](https://github.com/Gucostaa)**    | Backend em PHP e integração a Banco de dados |
| **[Gaby](https://github.com/TheNamelessAngel)**   | Banco de Dados |
| **[Livai](https://github.com/Livai1)**  | Backend, Banco de Dados|
| **[Pony](https://github.com/juanmh10)**   | Banco de dados, Python, Power BI e documentação |


## 📄 Licença
Este projeto é livre para fins educacionais e de portfólio.
