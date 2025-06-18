<?php
require 'conexao.php';
date_default_timezone_set('America/Sao_Paulo');

// Limpa espaços e padroniza os campos importantes
$nome     = trim($_POST['nome'] ?? '');
$email    = strtolower(trim($_POST['email'] ?? ''));
// Remove qualquer caractere que não seja número, para telefone e cnpj
$telefone = preg_replace('/\D/', '', $_POST['telefone'] ?? '');
$cnpj     = preg_replace('/\D/', '', $_POST['cnpj'] ?? '');
$senha    = $_POST['senha'] ?? '';
$csenha   = $_POST['csenha'] ?? '';

$senha_hash = password_hash($senha, PASSWORD_DEFAULT);
$erros = [];

if ($senha !== $csenha) {
    $erros[] = 'senha';
}

// Verifica se já existe CNPJ cadastrado (sem pontuação)
$stmtCnpj = $conn->prepare("SELECT 1 FROM empresas WHERE cnpj = :cnpj");
$stmtCnpj->execute([':cnpj' => $cnpj]);
if ($stmtCnpj->fetch()) {
    $erros[] = 'cnpj';
}

// Verifica se já existe email cadastrado
$stmtEmail = $conn->prepare("SELECT 1 FROM empresas WHERE email = :email");
$stmtEmail->execute([':email' => $email]);
if ($stmtEmail->fetch()) {
    $erros[] = 'email';
}

// Verifica se já existe telefone cadastrado (também sem pontuação)
$stmtTel = $conn->prepare("SELECT 1 FROM empresas WHERE telefone = :telefone");
$stmtTel->execute([':telefone' => $telefone]);
if ($stmtTel->fetch()) {
    $erros[] = 'telefone';
}

if (!empty($erros)) {
    $erroStr = implode(',', $erros);
    header("Location: ../frontend/pages/cadastro.php?erro=$erroStr");
    exit;
}

$stmt = $conn->prepare("
    INSERT INTO empresas (nome, email, telefone, cnpj, senha_hash, criado_em)
    VALUES (:nome, :email, :telefone, :cnpj, :senha_hash, CURRENT_TIMESTAMP)
");

$stmt->execute([
    ':nome'       => $nome,
    ':email'      => $email,
    ':telefone'   => $telefone,
    ':cnpj'       => $cnpj,
    ':senha_hash' => $senha_hash
]);

header("Location: ../frontend/pages/login.php");
exit;
