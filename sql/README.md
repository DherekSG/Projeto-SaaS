Documentação Banco de Dados

Este documento apresenta a estrutura completa do banco de dados do projeto SaaS, descrevendo detalhadamente suas tabelas, relacionamentos e alterações realizadas durante o desenvolvimento.

Estrutura Geral do Banco

O projeto utiliza PostgreSQL e está organizado em entidades relacionadas, permitindo um gerenciamento eficaz das informações necessárias para o funcionamento da aplicação.

--Tabelas

usuarios: Registro dos usuários que possuem acesso ao sistema.

clientes: Armazena informações detalhadas dos clientes cadastrados.

atendimentos: Registros dos atendimentos realizados aos clientes.

feedbacks: Armazena avaliações e comentários feitos pelos clientes.

churn_predict: Informações sobre previsões de churn geradas por modelos de Machine Learning.

eventos: Registros de eventos dos usuários, utilizados para alimentação de algoritmos de Machine Learning.

--Relacionamentos

Clientes têm relação com: Atendimentos, Feedbacks, Churn Predict e Eventos (1 cliente para N registros relacionados).

--Descrição das Tabelas

usuarios
id (PK): Identificador único do usuário.

nome: Nome completo do usuário.
email: E-mail único do usuário, utilizado para login.
senha_hash: Senha criptografada (bcrypt, argon2, scrypt).
criado_em: Data e hora da criação do registro.

clientes
id (PK): Identificador único do cliente.

nome: Nome do cliente.
email: E-mail do cliente.
telefone: Número de telefone no formato E.164.
canal: Canal preferencial de contato (email, telefone, whatsapp, app).
data_cadastro: Data de cadastro do cliente.
criado_em: Data e hora da criação do registro.

atendimentos

id (PK): Identificador único do atendimento.
cliente_id (FK → clientes.id): Cliente relacionado.
data_atendimento: Data e hora do atendimento realizado.
descricao: Descrição detalhada do atendimento.
criado_em: Data e hora da criação do registro.

feedbacks

id (PK): Identificador único do feedback.
cliente_id (FK → clientes.id): Cliente relacionado.
nota_nps: Nota NPS dada pelo cliente (0-10).
comentario: Comentário adicional do cliente.
data_feedback: Data que o feedback foi realizado.
criado_em: Data e hora da criação do registro.

churn_predict

id (PK): Identificador único da previsão de churn.
cliente_id (FK → clientes.id): Cliente relacionado.
risco_churn: Probabilidade estimada de churn (0-1).
modelo_usado: Modelo de Machine Learning utilizado.
data_prevista: Data prevista para possível churn.
criado_em: Data e hora da criação do registro.

eventos

id (PK): Identificador único do evento.
cliente_id (FK → clientes.id): Cliente relacionado.
tipo_evento: Tipo do evento registrado (login, logout, acesso_relatorio, cancelamento, novo_feedback).
data_evento: Data e hora em que o evento ocorreu.

--Documentos e Imagens Complementares

ERD_txt.txt: Arquivo contendo o ERD textual detalhado.

ERD_VISUAL.png: Imagem visual do ERD para melhor entendimento da estrutura.

##Histórico de Alterações-----

##Comentários foram adicionados em tabelas específicas para melhor entendimento.
##Coluna criado_em adicionada em tabelas para datação das inserções.
##Nova tabela eventos criada para coleta de dados destinados à alimentação de algoritmos de Machine Learning.
##ERD_txt.txt
##ERD_VISUAL.png

