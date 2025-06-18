<?php
require 'conexao.php';
session_start();

date_default_timezone_set('America/Sao_Paulo');

$cnpj = $_POST['cnpj'] ?? '';
$senha = $_POST['senha'] ?? '';

// Limpa o CNPJ (apenas números)
$cnpj = preg_replace('/\D/', '', $cnpj);

$erros = [];

try {
    $sql = 'SELECT * FROM empresas WHERE cnpj = :cnpj';                 
    $stmt = $conn->prepare($sql);
    $stmt->bindParam(':cnpj', $cnpj);
    $stmt->execute();

    $empresa = $stmt->fetch(PDO::FETCH_ASSOC);

    if (!$empresa) {
        $erros[] = 'cnpj'; // CNPJ não encontrado
    } else {
        if (!password_verify($senha, $empresa['senha_hash'])) {
            $erros[] = 'senha'; // Senha incorreta
        }
    }

    if (!empty($erros)) {
        $erroStr = implode(',', $erros);
        header("Location: ../frontend/pages/login.php?erro=$erroStr");
        exit;
    }

    // Login válido, cria sessão
    $_SESSION['usuario_id'] = $empresa['id'];
    $_SESSION['nome'] = $empresa['nome'];
    $_SESSION['cnpj'] = $empresa['cnpj'];

    $dir = "../clientes/" . preg_replace("/[^a-zA-Z0-9]/", "_", $empresa['cnpj']);
    if (!is_dir($dir)) {
        mkdir($dir, 0755, true);
    }

    header("Location: ../frontend/pages/area_exclusiva.php");
    exit();

} catch (PDOException $e) {
    // Pode criar uma mensagem de erro genérica ou logar
    header("Location: ../frontend/pages/login.php?erro=erro_servidor");
    exit;
}
?>
