<?php
session_start();

if (!isset($_SESSION['usuario_id'])) {
    header("Location: ../pages/login.php");
    exit();
}

$nome = $_SESSION['nome'];
$cnpj = $_SESSION['cnpj'];
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Painel do Cliente</title>
</head>
<body>
    <h1>Bem-vindo, <?php echo htmlspecialchars($nome); ?>!</h1>
    <p>Seu CNPJ: <?php echo htmlspecialchars($cnpj); ?></p>

    <p><a href="../backend/logout.php">Sair da conta</a></p>
</body>
</html>