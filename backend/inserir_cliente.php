<?php
require 'conexao.php';

$nome = $_POST['nome'];
$email = $_POST['email'];
$telefone = $_POST['telefone'];

$sql = "INSERT INTO clientes (nome, email, telefone) VALUES (:nome, :email, :telefone)";
$stmt = $conn->prepare($sql);
$stmt->execute([
    ':nome' => $nome,
    ':email' => $email,
    ':telefone' => $telefone
]);

echo "Cliente cadastrado com sucesso!";
?>
