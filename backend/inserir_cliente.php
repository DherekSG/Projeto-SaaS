<?php
require 'conexao.php';
date_default_timezone_set('America/Sao_Paulo');

$nome = $_POST['nome'];
$email = $_POST['email'];
$telefone = $_POST['telefone'];
$senha = $_POST['senha'];
$csenha = $_POST['csenha'];
$genero = $_POST['genero'];
$data = date('Y-m-d');

if ($senha !== $csenha) {
    echo "As senhas não coincidem.";
    exit;
}

$senha_hash = password_hash($senha, PASSWORD_DEFAULT);

$sql = "INSERT INTO clientes (nome, email, telefone, senha, genero, data_inclusao) 
        VALUES (:nome, :email, :telefone, :senha, :genero, :data)";
$stmt = $conn->prepare($sql);

$stmt->execute([
    ':nome' => $nome,
    ':email' => $email,
    ':telefone' => $telefone,
    ':senha' => $senha_hash,
    ':genero' => $genero,
    ':data' => $data
]);

echo "Cliente cadastrado com sucesso!";
?>
