<?php
require 'conexao.php';
session_start();

date_default_timezone_set('America/Sao_Paulo');

$usuario = trim($_POST['usuario'] ?? '');
$senha = $_POST['senha'] ?? '';

$erros = [];

try {
    // Buscando pelo campo "usuario"
    $sql = 'SELECT * FROM administradores WHERE usuario = :usuario';
    $stmt = $conn->prepare($sql);
    $stmt->bindParam(':usuario', $usuario);
    $stmt->execute();

    $admin = $stmt->fetch(PDO::FETCH_ASSOC);

    if (!$admin) {
        $erros[] = 'usuario'; // Usuário não encontrado
    } else {
        // Comparação direta da senha, sem hash
        if ($senha !== $admin['senha']) {
            $erros[] = 'senha'; // Senha incorreta
        }
    }

    if (!empty($erros)) {
        $erroStr = implode(',', $erros);
        header("Location: ../frontend/pages/login.php?erro=$erroStr");
        exit;
    }

    // Login válido
    $_SESSION['usuario_id'] = $admin['id'];
    $_SESSION['nome'] = $admin['nome'];
    $_SESSION['usuario'] = $admin['usuario'];

    $dir = "../clientes/" . preg_replace("/[^a-zA-Z0-9]/", "_", $admin['usuario']);
    if (!is_dir($dir)) {
        mkdir($dir, 0755, true);
    }

    header("Location: ../frontend/pages/area_exclusiva.php");
    exit();

} catch (PDOException $e) {
    header("Location: ../frontend/pages/login.php?erro=erro_servidor");
    exit;
}
