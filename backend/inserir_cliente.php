<?php
require 'conexao.php';// Inclui a conexão

// Pegar os dados do formulário via POST
$nome = $_POST['nome'] ?? null;
$email = $_POST['email'] ?? null;
$telefone = $_POST['telefone'] ?? null;
$data_cadastro = $_POST['data_cadastro'] ?? null;
$canal = $_POST['canal'] ?? null;

// Validar os dados simples(ver se não está vazio)
if(!$nome || !$email)
{
    die('Nome e email são obrigatórios');
}

try {
    //Preparar o comando SQL para inserÇão com placeholders
    $sql = "INSERT INTO clientes (nome, email, telefone)
            VALUES (:nome, :email, :telefone)";
    $stmt = $pdo->prepare($sql);

    // Vincular os valores reais aos placeholders
    $stmt->bindParam(':nome', $nome);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':telefone', $telefone);
    $stmt->bindParam('data_cadastro', $data_cadastro);
    $stmt->bindParam('canal', $canal);
    
    //Executar a Query
    $stmt->execute();

    echo "Cliente cadastro com sucesso!";

} catch (PDOException $e) {
    echo "Erro ao inserir cliente" . $e->getMessage();
}
?>