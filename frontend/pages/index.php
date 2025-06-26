<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://fonts.googleapis.com/css2?family=Urbanist:wght@400;600;700&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="../styles/index.css" />
    <title>Energy Ltda</title>
</head>

<body class="dark-mode">
    <header>
        <div class="logo-container">
            <img src="../images/leaf-logo.png" alt="leaf-logo" class="logo">
            <h1>Energy</h1>
        </div>
        <nav>
            <a href="#sobre">Sobre</a>
            <a href="#servicos">Soluções</a>
            <a href="#cases">Casos</a>
            <a href="#contato">Contato</a>
            <a href="../pages/login.php" target="_blank">Login Empresarial</a>

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
            <h2>Entenda como a <span class="destaque">Energy</span> economiza na <span class="destaque">entrega</span> de <span class="destaque">energia</span> para a sua <span class="destaque">residência</span>!"</h2>
            <p>Com <span class="destaque">inteligência artificial</span>, prevemos padrões de consumo, evitamos perdas e entregamos a sua <span class="destaque">energia</span> com mais <span class="destaque">eficiência</span>.</p>
            <button class="cta-button" onclick="window.location.href='#contato'">Agende uma demonstração</button>
        </div>
    </section>

    <section id="sobre" class="sobre">
        <h2>Quem Somos</h2>
        <div class="carrossel">
            <div class="texto">
            <p>Somos a Energy, uma empresa de energia limpa comprometida com a inovação. Unimos tecnologia, sustentabilidade e inteligência preditiva para garantir que cada cliente tenha uma experiência única, segura e eficiente no uso de energia elétrica.</p>
            <p>Utilizamos modelos avançados de machine learning e análise comportamental para antecipar necessidades, evitar perdas e otimizar o fornecimento de energia com base nos hábitos de consumo de cada região.</p>
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
        <h2>Soluções Inovadoras</h2>
        <div class="services">
            <div class="service">
                <h3>Smart Monitoring</h3>
                <p>Identificamos padrões de uso e prevemos falhas ou desperdícios antes que aconteçam.</p>
            </div>
            <div class="service">
                <h3>Consumption</h3>
                <p>Oferecemos estimativas precisas de consumo futuro para ajudar nossos clientes a economizar e planejar.</p>
            </div>
            <div class="service">
                <h3>Predictive Service</h3>
                <p>Nossos sistemas de IA antecipam solicitações e agilizam o suporte, garantindo mais agilidade e satisfação.</p>
            </div>
            <div class="service">
                <h3>Sustainable Energy</h3>
                <p>Incentivamos práticas sustentáveis e oferecemos sugestões automatizadas com base em perfis de consumo.</p>
            </div>
            <div class="service">
                <h3>Satisfaction Analysis</h3>
                <p>Coletamos e analisamos dados de interações, feedbacks e comportamento de uso em tempo real para medir a satisfação dos nossos clientes.</p>
            </div>
            <div class="service">
                <h3>Smart Management</h3>
                <p>Nosso sistema identifica horários de pico e prevê aumentos no consumo com base em padrões históricos e comportamento climático.</p>
            </div>
        </div>
    </section>

    <section id="cases" class="cases">
    <h2>Casos de Sucesso</h2>
    <div class="case-grid">
        
        <div class="case-item card">
            <img src="../images/help-desk.png" alt="IA em Atendimento" class="case-icon">
            <div class="case-content">
                <h3>Atendimento Preditivo</h3>
                <p>Redução de 35% no tempo de resposta com assistente virtual treinado em dados de consumo e históricos de atendimento.</p>
            </div>
        </div>

        <div class="case-item card">
            <img src="../images/cancel.png" alt="Evitar cancelamentos" class="case-icon">
            <div class="case-content">
                <h3>Prevenção de Cancelamentos</h3>
                <p>Identificamos 2.100 clientes em risco de desligamento e revertimos 78% com ações automatizadas e personalizadas.</p>
            </div>
        </div>

        <div class="case-item card">
            <img src="https://cdn-icons-png.flaticon.com/512/3050/3050525.png" alt="Painel Inteligente" class="case-icon">
            <div class="case-content">
                <h3>Dashboard do Cliente</h3>
                <p>Lançamos o painel de consumo personalizado que aumentou o engajamento em 52% e reduziu dúvidas recorrentes.</p>
            </div>
        </div>

        <div class="case-item card">
            <img src="../images/lightning.png" alt="Picos de Consumo" class="case-icon">
            <div class="case-content">
                <h3>Gestão de Picos</h3>
                <p>Reduzimos em 18% os custos operacionais ao prever e redistribuir demandas em horários de pico com machine learning.</p>
            </div>
        </div>

        <div class="case-item card">
            <img src="../images/satisfaction.png" alt="Satisfação do Cliente" class="case-icon">
            <div class="case-content">
                <h3>Satisfação em Tempo Real</h3>
                <p>Monitoramos a experiência dos clientes em tempo real, elevando nosso NPS de 62 para 84 em apenas 4 meses.</p>
            </div>
        </div>

        <div class="case-item card">
            <img src="../images/leaf.png" alt="Energia Rural" class="case-icon">
            <div class="case-content">
                <h3>Energia no Campo</h3>
                <p>Ampliamos o acesso à energia em regiões rurais com sensores IoT e automação inteligente, reduzindo falhas em 41%.</p>
            </div>
        </div>

        <div class="case-item card">
            <img src="../images/monitoring.png" alt="Manutenção Preditiva" class="case-icon">
            <div class="case-content">
                <h3>Manutenção Inteligente</h3>
                <p>Implementamos manutenção preditiva em transformadores, reduzindo em 63% as interrupções inesperadas.</p>
            </div>
        </div>

        <div class="case-item card">
            <img src="../images/energy-consumption.png" alt="Sustentabilidade" class="case-icon">
            <div class="case-content">
                <h3>Consumo Sustentável</h3>
                <p>Campanhas automatizadas incentivaram hábitos sustentáveis, reduzindo o desperdício de energia em 22 mil residências.</p>
            </div>
        </div>

        <div class="case-item card">
            <img src="../images/taxes.png" alt="Tarifa Inteligente" class="case-icon">
            <div class="case-content">
                <h3>Tarifa Inteligente</h3>
                <p>Desenvolvemos um modelo de tarifa dinâmica, reduzindo a inadimplência em 29% entre clientes de baixa renda.</p>
            </div>
        </div>
    </div>
</section>

    <section id="contato" class="contato">
        <h2>Fale com a Energy</h2>
        <p>Quer entender como usamos <span class="destaque">tecnologia</span> para levar <span class="destaque">energia</span> com mais <span class="destaque">inteligência</span> até você?</p>
        <p>Email: <a href="mailto:contato@energy.com.br">contato@energy.com.br</a></p>
    </section>

    <footer>
        <p>&copy; 2025 Energy. Todos os direitos reservados.</p>
    </footer>

    <script src="../scripts/script.js"></script>
    <script src="../scripts/carrossel.js"></script>
</body>

</html>
