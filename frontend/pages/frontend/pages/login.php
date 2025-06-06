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
        <form action="../backend/inserir_cliente.php" method="post">
            <h2>Área de Login</h2>
            <div class="content">
                <div class="input-box-lg">
                    <label for="nome">CNPJ</label>
                    <input type="text" name="nome">
                </div>
                <div class="input-box">
                    <label for="senha">Senha</label>
                    <input type="password" name="senha">
                </div>
            </div>
            <div class="alert">
                <p>Não possui uma conta? <a href="../pages/cadastro.php">Cadastre-se!</a></p>
            </div>
            <div class="button-container">
                <button type="submit">Entrar</button>
            </div>
        </form>
    </div>
</body>
</html>
