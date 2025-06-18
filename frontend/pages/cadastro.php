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
    <link rel="stylesheet" href="../styles/cadastro.css"/>
    <title>Cadastro</title>
</head>
<body>
    <div class="container">
        <form action="/projeto-saas/backend/cadastro_cliente.php" method="post">
            <h2>Cadastro de Cliente</h2>
            <div class="content">
                <div class="input-box">
                    <label for="nome">Nome Completo</label>
                    <input type="text" name="nome" required placeholder="Digite seu nome completo">
                </div>

                <div class="input-box">
                    <label for="cnpj">CNPJ</label>
                    <input type="text" name="cnpj" required placeholder="Digite seu CNPJ"
                        class="<?php echo in_array('cnpj', $erros) ? 'erro' : ''; ?>">
                    <?php if (in_array('cnpj', $erros)): ?>
                        <span class="mensagem-erro">Este CNPJ já está cadastrado.</span>
                    <?php endif; ?>
                </div>

                <div class="input-box">
                    <label for="email">Email</label>
                    <input type="email" name="email" required placeholder="Digite seu email"
                        class="<?php echo in_array('email', $erros) ? 'erro' : ''; ?>">
                    <?php if (in_array('email', $erros)): ?>
                        <span class="mensagem-erro">Este email já está em uso.</span>
                    <?php endif; ?>
                </div>

                <div class="input-box">
                    <label for="telefone">Telefone</label>
                    <input type="tel" name="telefone" required placeholder="Digite seu telefone"
                        class="<?php echo in_array('telefone', $erros) ? 'erro' : ''; ?>">
                    <?php if (in_array('telefone', $erros)): ?>
                        <span class="mensagem-erro">Este telefone já está em uso.</span>
                    <?php endif; ?>
                </div>

                <div class="input-box">
                    <label for="senha">Senha</label>
                    <input type="password" name="senha" required placeholder="Crie uma senha"
                        class="<?php echo in_array('senha', $erros) ? 'erro' : ''; ?>">
                    <?php if (in_array('senha', $erros)): ?>
                        <span class="mensagem-erro">As senhas não coincidem.</span>
                    <?php endif; ?>
                </div>

                <div class="input-box">
                    <label for="csenha">Confirmar Senha</label>
                    <input type="password" name="csenha" required placeholder="Confirme a senha"
                        class="<?php echo in_array('senha', $erros) ? 'erro' : ''; ?>">
                    <?php if (in_array('senha', $erros)): ?>
                        <span class="mensagem-erro">As senhas não coincidem.</span>
                    <?php endif; ?>
                </div>
            </div>

            <div class="alert">
                <p>Ao se cadastrar, você concorda com nossos 
                    <a href="#">Termos</a>, <a href="#">Política de Privacidade</a> e <a href="#">Política de Cookies</a>.
                </p>
            </div>

            <div class="button-container">
                <button type="submit">Cadastrar</button>
            </div>
        </form>
    </div>
</body>
</html>
