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
                        class="<?php echo (isset($_GET['erro']) && $_GET['erro'] === 'cnpj') ? 'erro' : ''; ?>">
                    <?php if (isset($_GET['erro']) && $_GET['erro'] === 'cnpj'): ?>
                        <span class="mensagem-erro">Este CNPJ já está cadastrado.</span>
                    <?php endif; ?>
                </div>

                <div class="input-box">
                    <label for="email">Email</label>
                    <input type="email" name="email" required placeholder="Digite seu email"
                        class="<?php echo (isset($_GET['erro']) && $_GET['erro'] === 'email') ? 'erro' : ''; ?>">
                    <?php if (isset($_GET['erro']) && $_GET['erro'] === 'email'): ?>
                        <span class="mensagem-erro">Este email já está em uso.</span>
                    <?php endif; ?>
                </div>

                <div class="input-box">
                    <label for="telefone">Telefone</label>
                    <input type="tel" name="telefone" required placeholder="Digite seu telefone">
                </div>

                <div class="input-box">
                    <label for="senha">Senha</label>
                    <input type="password" name="senha" required placeholder="Crie uma senha">
                </div>

                <div class="input-box">
                    <label for="csenha">Confirmar Senha</label>
                    <input type="password" name="csenha" required placeholder="Confirme a senha">
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
