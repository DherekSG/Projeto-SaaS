<?php
require 'conexao.php';
session_start();

// Define timezone
date_default_timezone_set('America/Sao_Paulo');

// Coleta os dados do formulário
$cnpj = $_POST['cnpj'] ?? '';
$senha = $_POST['senha'] ?? '';

// Verifica se os campos foram preenchidos
if (empty($cnpj) || empty($senha)) {
    echo "Preencha todos os campos.";
    exit();
}

try {
    // Busca o cliente no banco de dados (PostgreSQL usa aspas duplas para nomes de colunas/tabelas)
    $sql = "SELECT * FROM clientes WHERE cnpj = :cnpj";
    $stmt = $conn->prepare($sql);
    $stmt->bindParam(':cnpj', $cnpj);
    $stmt->execute();

    $cliente = $stmt->fetch(PDO::FETCH_ASSOC);

    if ($cliente && password_verify($senha, $cliente['senha'])) {
        // Login bem-sucedido

        // Inicia sessão
        $_SESSION['usuario_id'] = $cliente['id'];
        $_SESSION['nome'] = $cliente['nome'];
        $_SESSION['cnpj'] = $cliente['cnpj'];

        // Cria pasta personalizada (opcional)
        $dir = "../clientes/" . preg_replace("/[^a-zA-Z0-9]/", "_", $cliente['cnpj']);
        if (!is_dir($dir)) {
            mkdir($dir, 0755, true);
        }

        // Redireciona para a área exclusiva
        header("Location: ../pages/area_exclusiva.php");
        exit();
    } else {
        echo "CNPJ ou senha incorretos.";
    }

} catch (PDOException $e) {
    echo "Erro no login: " . $e->getMessage();
}
?>
