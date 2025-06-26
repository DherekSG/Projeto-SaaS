<?php
session_start();

if (!isset($_SESSION['usuario_id'])) {
    header("Location: ../pages/login.php");
    exit();
}

$usuario = $_SESSION['usuario'];
?>

<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Painel do Cliente</title>
    <link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@400;600;700&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="../styles/area_exclusiva.css" />
    <!-- Você pode adicionar links para fontes ou ícones aqui -->
</head>
<body>
    <div class="container">
        <aside class="sidebar">
            <div class="sidebar-header">
                <h2>Área Exclusiva</h2>
            </div>
            <nav class="menu">
                <ul>
                    <li><a href="#" class="active">Dashboard</a></li>
                    <li><a href="#">Retenção</a></li>
                    <li><a href="#">Perdas</a></li>
                    <li><a href="#">Relatórios</a></li>
                    <li><a href="#">Cadastro</a></li>
                    <li><a href="#">Configurações</a></li>
                </ul>
            </nav>
        </aside>

        <main class="main-content">
            <header class="topbar">
                <div class="welcome">
                    Bem-vindo, <span class="usuario-info">Usuário: <?php echo htmlspecialchars($usuario); ?></span>
                </div>
                <a href="../pages/index.php" class="logout-btn" title="Sair da conta">Sair</a>
            </header>

            <section class="dashboard">
                <h1>Dashboard</h1>
                <p>Aqui você terá acesso aos gráficos e análises preditivas baseadas em Machine Learning.</p>

                <!-- Exemplo embed Power BI (substitua pelo real) -->
                <div class="powerbi-frame">
                    <iframe 
                        title="Dashboard Power BI"
                        width="100%" height="600" 
                        src="https://app.powerbi.com/view?r=EXEMPLO" 
                        frameborder="0" allowFullScreen="true"></iframe>
                </div>
            </section>
        </main>
    </div>
</body>
</html>
