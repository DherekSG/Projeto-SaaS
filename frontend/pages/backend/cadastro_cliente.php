<?php
require 'conexao.php';
date_default_timezone_set('America/Sao_Paulo');

$nome     = $_POST['nome'] ?? '';
$email    = $_POST['email'] ?? '';
$telefone = $_POST['telefone'] ?? '';
$cnpj     = $_POST['cnpj'] ?? '';
$senha    = $_POST['senha'] ?? '';
$csenha   = $_POST['csenha'] ?? '';
$data     = date('Y-m-d');

// Verifica se as senhas coincidem
if ($senha !== $csenha) {
    header("Location: /projeto-saas/frontend/pages/cadastro.php?erro=senha");
    exit;
}

// Criptografa a senha
$senha_hash = password_hash($senha, PASSWORD_DEFAULT);

try {
    $stmt = $conn->prepare("
        INSERT INTO clientes (nome, email, telefone, cnpj, senha, data_cadastro)
        VALUES (:nome, :email, :telefone, :cnpj, :senha, :data)
    ");

    $stmt->execute([
        ':nome' => $nome,
        ':email' => $email,
        ':telefone' => $telefone,
        ':cnpj' => $cnpj,
        ':senha' => $senha_hash,
        ':data' => $data
    ]);

    header("Location: ../pages/login.php");
    exit;
} catch (PDOException $e) {
    if (str_contains($e->getMessage(), 'cnpj')) {
        header("Location: ../pages/cadastro.php?erro=cnpj");
    } elseif (str_contains($e->getMessage(), 'email')) {
        header("Location: ../pages/cadastro.php?erro=email");
    } else {
        header("Location: ../pages/cadastro.php?erro=geral");
    }
    exit;
}
?>
