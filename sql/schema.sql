
-- Criação do banco de dados
CREATE DATABASE projeto_saas;
\c projeto_saas;

-- Tabela de usuários (login do sistema)
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    senha_hash VARCHAR(255) NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de clientes
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20),
    data_cadastro DATE DEFAULT CURRENT_DATE
);

-- Tabela de atendimentos
CREATE TABLE atendimentos (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER REFERENCES clientes(id) ON DELETE CASCADE,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    descricao TEXT
);

-- Tabela de feedbacks
CREATE TABLE feedbacks (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER REFERENCES clientes(id) ON DELETE CASCADE,
    nota_nps INTEGER CHECK (nota_nps BETWEEN 0 AND 10),
    comentario TEXT,
    data DATE DEFAULT CURRENT_DATE
);

-- Tabela de previsão de churn
CREATE TABLE churn_predict (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER REFERENCES clientes(id) ON DELETE CASCADE,
    risco_churn DECIMAL(5,2) CHECK (risco_churn BETWEEN 0 AND 1),
    modelo_usado VARCHAR(100),
    data_prevista DATE DEFAULT CURRENT_DATE
);
