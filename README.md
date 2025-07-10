# 📊 Projeto SaaS – Plataforma de Análise de Clientes e Previsão de Churn

## 🧠 Visão Geral

Este projeto propõe o desenvolvimento de uma plataforma SaaS voltada para pequenas empresas e profissionais autônomos. O sistema possibilita o cadastro e gerenciamento de clientes, atendimentos e feedbacks, além de oferecer **análises visuais** e **previsão de churn (evasão de clientes)** com suporte de algoritmos de Machine Learning.

---

## 🚀 Funcionalidades

- 📋 Cadastro e gestão de clientes, atendimentos e feedbacks
- 🤖 Previsão de churn com algoritmos de Machine Learning (XGBoost)
- 📈 Dashboards com métricas como NPS, satisfação e churn no Power BI
- 🧪 Modo demo com dados simulados para demonstração e testes

---

## 🧱 Stack Tecnológica

| Camada                | Tecnologias Utilizadas                                |
|-----------------------|-------------------------------------------------------|
| **Frontend**          | HTML5, CSS3, JavaScript, Bootstrap                    |
| **Backend Web**       | PHP 7+, integração com PostgreSQL                     |
| **Persistência**      | PostgreSQL hospedado em instância EC2 (AWS)          |
| **Machine Learning**  | Python (Pandas, Scikit-learn, XGBoost), Jupyter Notebook |
| **Visualização**      | Power BI Desktop                                      |
| **Versionamento**     | Git + GitHub                                          |
| **Deploy (opcional)** | XAMPP, Replit, EC2 Free Tier (AWS)                   |

---

## 📂 Estrutura do Repositório

```bash
projeto_saas/
├── backend/        # Código PHP: APIs, autenticação, rotas
├── docs/           # Documentação técnica e capturas de tela (prints)
├── datasets/       # Arquivos de dados para testes e treinamento (CSV)
├── frontend/       # Interface web: HTML, CSS, JS, Bootstrap
├── Modelos/        # Contém os modelos .plk do Machine Learning
├── powerbi/        # Dashboards Power BI (.pbix e imagens exportadas)
├── python/         # Scripts de ML: inserção no banco, treino e teste de modelos
├── sql/            # Scripts SQL, backups, CSVs de inserção e diagrama ER visual
├── .gitignore      # Arquivos ignorados no versionamento
└── README.md       # Documentação principal do projeto
```

---

## 👥 Equipe Técnica

| Nome | Responsabilidades |
|------|-------------------|
| 🔧 **[Dherek Schaberle](https://github.com/DherekSG)** | Líder técnico geral, integração de módulos, suporte e validação |
| 🧩 **[Tiago Rocha](https://github.com/TiagoRochaDSantos)** | Backend em PHP e integração com Python |
| 🎨 **[Gustavo Costa](https://github.com/Gucostaa)** | Backend em PHP, design da interface, frontend, embedding e integração com banco de dados |
| 🧱 **[Gabriel Antonio](https://github.com/TheNamelessAngel)** | Banco de dados, inserções, testes e manutenção |
| 🧪 **[Erick Levi](https://github.com/Livai1)** | Banco de dados, inserções, testes e manutenção |
| 📊 **[Juan Henrique](https://github.com/juanmh10)** | Administrador do banco de dados, Power BI, documentação, treinamento e testes de Machine Learning em Python, integração em cloud |

---

## ✅ Requisitos

Para executar o projeto em sua totalidade, é necessário ter os seguintes componentes instalados:

- **PHP 7+** com servidor local, como **XAMPP** ou ambiente online como **Replit**
- **PostgreSQL 16+** (banco hospedado localmente ou via EC2)
- **Python 3.x** (utilizamos a versão **3.10**)
- **Power BI Desktop** (visualização de dashboards .pbix)
- **Jupyter Notebook** (para execução dos scripts de Machine Learning)

---

## ⚙️ Como Executar o Projeto

Após clonar o repositório, certifique-se de que os **caminhos de diretório (paths)** e o acesso ao **banco de dados PostgreSQL** estejam corretamente configurados para o seu ambiente.

### ▶️ Passos para execução da etapa de Machine Learning (Jupyter Notebook)

1. **Abra o Jupyter Notebook ou a extensão no VS Code.**  
   Selecione a pasta `python/` e certifique-se de apontar corretamente para o dataset bruto localizado em `/datasets`.

2. **Execute o script de pré-processamento do dataset.**  
   Inclui limpeza, normalização e codificação das variáveis.

3. **Execute o script que carrega o modelo treinado (.pkl)** e aplica ao dataset processado.

4. **Valide as métricas geradas**, garantindo que incluam:
   - `F1-Score`
   - `Accuracy`
   - `Recall`

5. **Gere os gráficos com Matplotlib** para representar os resultados visualmente.

---

### 📌 Ao final deste processo, você deverá obter:

- ✔️ Dataset pré-processado  
- ✔️ Dataset com predição do modelo  
- ✔️ Métricas de desempenho do modelo  
- ✔️ Três gráficos representando os resultados do teste  

---

## 📄 Licença

Este projeto é acadêmico e está licenciado sob os termos da [MIT License](LICENSE).

---

## 📬 Contato

Dúvidas, sugestões ou contribuições? Entre em contato com qualquer membro da equipe via GitHub ou abra uma *issue* neste repositório.










--------------------------------------------
Adicionando
.env 
Arquivo de variável de ambiente de exemplo sem credênciais.