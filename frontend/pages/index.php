<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@400;600;700&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="../styles/index.css" />
    <title>Projeto-SaaS</title>
</head>

<body class="dark-mode">
    <header>
        <h1>Projeto SaaS </h1>
        <nav>
            <a href="#sobre">Sobre</a>
            <a href="#servicos">Soluções</a>
            <a href="#cases">Casos</a>
            <a href="#contato">Contato</a>
            <a href="../pages/login.html" target="_blank">Login</a>

            <button id="toggle-theme-btn" aria-label="Alternar tema" title="Alternar tema" type="button">
                <span class="hamburger-line"></span>
                <span class="hamburger-line"></span>
                <span class="hamburger-line"></span>
            </button>
        </nav>
    </header>

    <section class="hero">
        <div class="hero-content">
            <h2>Entenda por que sua empresa está perdendo clientes</h2>
            <p>Reduza o churn com machine learning, análise preditiva e dashboards com Power BI.</p>
            <button class="cta-button" onclick="window.location.href='#contato'">Agende uma demonstração</button>
        </div>
    </section>

    <section id="sobre" class="sobre">
        <h2>Quem Somos</h2>
        <div class="carrossel">
            <div class="texto">
                <p>Somos uma consultoria especializada em Inteligência Artificial aplicada à retenção de clientes. Atuamos com análise preditiva, modelos de churn, personalização de atendimento e visualização de dados com Power BI.</p>
                <p>Nosso foco é ajudar empresas a compreender o comportamento de seus clientes e antecipar perdas com tecnologia e precisão.</p>
            </div>
            <img src="https://placehold.co/600x300?text=600x300" alt="Imagem institucional">
        </div>
    </section>

    <section id="servicos" class="servicos">
        <h2>Soluções Inteligentes</h2>
        <div class="services">
            <div class="service">
                <h3>Análise de Churn</h3>
                <p>Modelos preditivos que identificam clientes propensos a sair, com base em comportamento e padrões históricos.</p>
            </div>
            <div class="service">
                <h3>Power BI Personalizado</h3>
                <p>Dashboards intuitivos e estratégicos com KPIs de retenção, engajamento e performance.</p>
            </div>
            <div class="service">
                <h3>Plataforma SaaS Exclusiva</h3>
                <p>Solução web completa com login empresarial, dados centralizados e segurança para toda a equipe.</p>
            </div>
        </div>
    </section>

    <section id="cases" class="cases">
        <h2>Casos de Sucesso</h2>
        <div class="case-list">
            <div class="case-item">
                <p>Empresa do setor bancário reduziu em 45% a evasão de clientes em apenas 3 meses.</p>
            </div>
            <div class="case-item">
                <p>Rede de academias aumentou a fidelização com campanhas personalizadas via insights de churn.</p>
            </div>
            <img src="https://placehold.co/600x300?text=600x300" alt="Imagem institucional">
        </div>
    </section>

    <section id="contato" class="contato">
        <h2>Fale Conosco</h2>
        <p>Quer agendar uma demonstração, entender nosso modelo SaaS ou conversar sobre churn? Fale com a gente!</p>
        <p>Email: <a href="mailto:contato@nomedaempresa.com.br">contato@nomedaempresa.com.br</a></p>
    </section>

    <footer>
        <p>&copy; 2025 Projeto SaaS Inteligente. Todos os direitos reservados.</p>
    </footer>

    <script src="../scripts/script.js"></script>
</body>

</html>