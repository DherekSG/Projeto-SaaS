<?php
$erro = $_GET['erro'] ?? '';
$erros = explode(',', $erro);
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../styles/login.css"/>
    <title>Login</title>
</head>
<body>
    <div class="container">
        <form action="/projeto-saas/backend/login_cliente.php" method="post">
            <h2>Área de Login</h2>
            <div class="content">
                <div class="input-box-lg">
                    <label for="usuario">Usuário</label>
                    <input type="text" name="usuario" 
                        class="<?php echo in_array('usuario', $erros) ? 'erro' : ''; ?>">
                    <?php if (in_array('usuario', $erros)): ?>
                        <span class="mensagem-erro">Usuário não encontrado.</span>
                    <?php endif; ?>
                </div>
                <div class="input-box">
                    <label for="senha">Senha</label>
                    <input type="password" name="senha" 
                        class="<?php echo in_array('senha', $erros) ? 'erro' : ''; ?>">
                    <?php if (in_array('senha', $erros)): ?>
                        <span class="mensagem-erro">Senha incorreta.</span>
                    <?php endif; ?>
                </div>
            </div>
            <?php if (in_array('erro_servidor', $erros)): ?>
                <div class="alert alert-error">Erro no servidor. Tente novamente mais tarde.</div>
            <?php endif; ?>
            <div class="alert">
                <p>Não possui uma conta? Cadastre-se diretamente com o administrador do sistema.</p>
            </div>
            <div class="button-container">
                <button type="submit">Entrar</button>
            </div>
        </form>
    </div>
</body>
</html>
