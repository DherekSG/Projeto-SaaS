
-- Criacao do banco de dados
CREATE DATABASE projeto_saas;
\c projeto_saas;

<<<<<<< HEAD
-- Tabela de usuarios (login do sistema)
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
=======
-- Tabela de empresas (login do sistema) cnpj + senha
CREATE TABLE empresas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone varchar(20),
    cnpj varchar(14) unique check (cnpj ~ '^[0-9]{14}$'),   --REGEX CNPJ apenas numeros.
>>>>>>> 0739ea749af15caec55ff8a5c89f8064c5c267f7
    senha_hash VARCHAR(255) NOT NULL, --bcrypt,argon2,scrypt ???
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de clientes
CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20) CHECK (telefone ~ '^\+?\d{10,15}$'), --E.164?
    canal VARCHAR(50) CHECK (canal in('email', 'telefone', 'whatsapp', 'app')),
    data_cadastro DATE DEFAULT CURRENT_DATE,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    --atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	);

-- Tabela de atendimentos
CREATE TABLE atendimentos (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER REFERENCES clientes(id) ON DELETE CASCADE,
    data_atendimento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    --atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  	descricao TEXT
);

-- Tabela de feedbacks
CREATE TABLE feedbacks (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER REFERENCES clientes(id) ON DELETE CASCADE,
    nota_nps INTEGER CHECK (nota_nps BETWEEN 0 AND 10),
    comentario TEXT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    --atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_feedback DATE DEFAULT CURRENT_DATE
);

-- Tabela de previsao de churn
CREATE TABLE churn_predict (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER REFERENCES clientes(id) ON DELETE CASCADE,
    risco_churn DECIMAL(5,2) CHECK (risco_churn BETWEEN 0 AND 1),
    modelo_usado VARCHAR(100) not null, 
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    --atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_prevista DATE DEFAULT CURRENT_DATE
);


-- Tabela de eventos de uso | usados na alimentacao do MACHINE LEARNING
CREATE TABLE eventos(
    id SERIAL PRIMARY KEY,
    cliente_id integer references clientes(id) ON DELETE CASCADE,
    tipo_evento VARCHAR(50) CHECK (tipo_evento in ('login', 'logout', 'acesso_relatorio', 'cancelamento', 'novo_feedback')), --login, acesso_relatorio, cancelamento, etc...
    data_evento TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);