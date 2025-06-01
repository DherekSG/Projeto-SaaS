  // Seleciona o botão
  const toggleBtn = document.getElementById('toggle-theme-btn');

  // Função para alternar o modo
  function toggleTheme() {
    const body = document.body;
    if(body.classList.contains('dark-mode')) {
      body.classList.remove('dark-mode');
      localStorage.setItem('theme', 'light');
    } else {
      body.classList.add('dark-mode');
      localStorage.setItem('theme', 'dark');
    }
  }

  // Ao clicar no botão alterna o tema
  toggleBtn.addEventListener('click', toggleTheme);

  // Mantém a preferência salva no localStorage
  window.addEventListener('load', () => {
    const savedTheme = localStorage.getItem('theme');
    if(savedTheme === 'dark') {
      document.body.classList.add('dark-mode');
    } else {
      document.body.classList.remove('dark-mode');
    }
  });