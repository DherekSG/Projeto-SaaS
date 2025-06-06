INSERT INTO clientes (nome, email, telefone) VALUES
('Maria Silva', 'maria@email.com', '(11) 99999-1111'),
('Carlos Souza', 'carlos@email.com', '(11) 98888-2222');

INSERT INTO atendimentos (cliente_id, descricao) VALUES
(1, 'Solicitação de troca de plano'),
(2, 'Dúvida sobre fatura');

INSERT INTO feedbacks (cliente_id, nota_nps, comentario) VALUES
(1, 9, 'Atendimento rápido e eficiente.'),
(2, 6, 'Demorou para resolver.');

INSERT INTO churn_predict (cliente_id, risco_churn, modelo_usado) VALUES
(1, 0.15, 'RandomForest'),
(2, 0.72, 'RandomForest');
