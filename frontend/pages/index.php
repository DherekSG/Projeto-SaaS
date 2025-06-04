<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@400;600;700&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="../styles/index.css" />
    <title>Projeto-SaaS</title>
</head>

<body class="dark-mode">
    <header>
    <h1>Projeto SaaS</h1>
        <nav>
            <a href="#sobre">Sobre</a>
            <a href="#servicos">Soluções</a>
            <a href="#cases">Casos</a>
            <a href="#contato">Contato</a>
            <a href="../pages/login.php" target="_blank">Login</a>

            <button id="toggle-theme-btn" aria-label="Abrir menu" title="Abrir menu" type="button">
                <span class="hamburger-line"></span>
                <span class="hamburger-line"></span>
                <span class="hamburger-line"></span>
            </button>

            <!-- Menu dropdown -->
            <div class="dropdown-menu" id="dropdown-menu">
            <ul>
                <label class="switch">
                    <input type="checkbox" id="theme-switch">
                    <span class="slider round"></span>
                    <span class="switch-label" id="theme-label">Modo Claro</span>
                </label>
            </ul>
            </div>
        </nav>
    </header>

    <section class="hero">
        <div class="hero-content">
            <h2>Entenda <span class="destaque">por que</span> a sua <span class="destaque">empresa</span> está perdendo <span class="destaque">clientes</span></h2>
            <p>Reduza sua <span class="destaque2">perda</span> com <span class="destaque2">machine learning</span>, análise preditiva e dashboards utilizando o <span class="destaque2">Power BI</span>.</p>
            <button class="cta-button" onclick="window.location.href='#contato'">Agende uma demonstração</button>
        </div>
    </section>

    <section id="sobre" class="sobre">
        <h2>Quem Somos</h2>
        <div class="carrossel">
            <div class="texto">
                <p>Somos uma consultoria especializada em Inteligência Artificial voltada para a retenção de clientes. Combinamos análise preditiva, modelos de churn, personalização de atendimento e visualização de dados com Power BI para transformar dados em decisões estratégicas.</p>
                <p>Nosso propósito é ajudar empresas a entender profundamente o comportamento de seus clientes, antecipando riscos de perda e potencializando a fidelização com o uso de tecnologia, precisão e inteligência de ponta.</p>
            </div>
            <div class="carrossel-imagens">
                <img src="https://images.unsplash.com/photo-1629904853716-f0bc54eea481" alt="Equipe criativa">
                <img src="https://images.unsplash.com/photo-1551434678-e076c223a692" alt="Ambiente tecnológico">
                <img src="https://images.unsplash.com/photo-1551836022-d5d88e9218df" alt="img1">
                <img src="https://images.unsplash.com/photo-1557804506-669a67965ba0" alt="img2">
                <img src="https://images.unsplash.com/photo-1603791440384-56cd371ee9a7" alt="img3">

            </div>
        </div>
    </section>

    <section id="servicos" class="servicos">
        <h2>Soluções Inteligentes</h2>
        <div class="services">
            <div class="service">
                <h3>Advanced Churn</h3>
                <p>Detecte padrões comportamentais e antecipe a saída de clientes com modelos de machine learning sob medida.</p>
            </div>
            <div class="service">
                <h3>Power BI</h3>
                <p>Visualize seus dados com clareza por meio de painéis interativos que destacam métricas de retenção, engajamento e performance.</p>
            </div>
            <div class="service">
                <h3>Software as a Service</h3>
                <p>Tenha uma solução web completa e segura, com login empresarial, dados integrados e usabilidade otimizada para equipes de qualquer porte.</p>
            </div>
            <div class="service">
                <h3>Customer Experience</h3>
                <p>Integre dados de NPS, feedbacks e jornadas para identificar pontos críticos e melhorar continuamente a experiência do usuário.</p>
            </div>
            <div class="service">
                <h3>Insights Automation</h3>
                <p>Gere alertas e recomendações automáticas baseadas em comportamento anômalo, riscos de churn e tendências de uso.</p>
            </div>
            <div class="service">
                <h3>Exclusive Area</h3>
                <p>Tenha acesso a um ambiente seguro, inteligente e totalmente personalizado para sua empresa.</p>
            </div>
        </div>
    </section>

    <section id="cases" class="cases">
        <h2>Casos de Sucesso</h2>
            <div class="case-grid">
                <div class="case-item card">
                    <img src="https://cdn-icons-png.flaticon.com/512/3135/3135706.png" alt="Banco" class="case-icon">
                <div class="case-content">
                    <h3>Setores Bancários</h3>
                    <p>reduziram em 45% a evasão de clientes em apenas 3 meses com análises preditivas.</p>
                </div>
            </div>
            <div class="case-item card">
                    <img src="https://cdn-icons-png.flaticon.com/512/3004/3004582.png" alt="Academia" class="case-icon">
                <div class="case-content">
                    <h3>Redes de Academias</h3>
                    <p>Aumentaram as fidelizações com campanhas personalizadas via insights de churn.</p>
                </div>
            </div>
            <div class="case-item card">
                    <img src="https://cdn-icons-png.flaticon.com/512/3135/3135768.png" alt="Educação" class="case-icon">
                <div class="case-content">
                    <h3>Grupos Educacionais</h3>
                    <p>Reverteram 1.200 cancelamentos com ações baseadas em dados comportamentais.</p>
                </div>
            </div>
            <div class="case-item card">
                    <img src="https://cdn-icons-png.flaticon.com/512/891/891462.png" alt="E-commerce" class="case-icon">
                <div class="case-content">
                    <h3>E-commerce</h3>
                    <p>Recuperaram mais de R$ 500 mil em receitas anuais com segmentações avançadas e dashboards Power BI.</p>
                </div>
            </div>
            <div class="case-item card">
                    <img src="https://cdn-icons-png.flaticon.com/512/702/702797.png" alt="Energia" class="case-icon">
                <div class="case-content">
                    <h3>Empresas de Energia</h3>
                    <p>Aumentaram as satisfações dos clientes em 27% com atendimentos proativos guiado por IA.</p>
                </div>
            </div>
            <div class="case-item card">
                    <img src="https://cdn-icons-png.flaticon.com/512/2965/2965567.png" alt="Clínicas de Saúde" class="case-icon">
                <div class="case-content">
                    <h3>Clínicas de Saúde</h3>
                    <p>Reduções de 35% nos cancelamentos de planos com notificações automáticas de riscos.</p>
                </div>
            </div>
            <div class="case-item card">
                    <img src="https://cdn-icons-png.flaticon.com/512/1046/1046784.png" alt="Franquia de Alimentação" class="case-icon">
                <div class="case-content">
                    <h3>Franquias de Alimentação</h3>
                    <p>Triplicou as conversões em campanhas de reengajamento com clientes inativos.</p>
                </div>
            </div>
            <div class="case-item card">
                    <img src="https://cdn-icons-png.flaticon.com/512/3063/3063827.png" alt="Empresa de Seguros" class="case-icon">
                <div class="case-content">
                    <h3>Empresas de Seguros</h3>
                    <p>Melhorias de 21 pontos no NPS com estratégias de retenção baseadas em insights preditivos.</p>
                </div>
            </div>
            <div class="case-item card">
                    <img src="https://cdn-icons-png.flaticon.com/512/1055/1055646.png" alt="Games" class="case-icon">
                <div class="case-content">
                    <h3>Plataformas de Games</h3>
                    <p>Melhorias de 29 pontos no NPS com sugestões de conteúdo personalizadas e retenções baseadas em usos.</p>
                </div>
            </div>
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
    <script src="../scripts/carrossel.js"></script>
</body>

</html>
