// Seleciona os elementos necessários
const toggleBtn = document.getElementById('toggle-theme-btn');
const themeSwitch = document.getElementById('theme-switch');
const dropdownMenu = document.getElementById('dropdown-menu');
const themeLabel = document.getElementById('theme-label'); // Texto ao lado da bolinha

// Função para alternar tema claro/escuro
function toggleTheme() {
  const body = document.body;
  const isDark = body.classList.toggle('dark-mode');
  const currentTheme = isDark ? 'dark' : 'light';
  localStorage.setItem('theme', currentTheme);

  // Atualiza o estado do switch
  if (themeSwitch) {
    themeSwitch.checked = isDark;
  }

  // Atualiza o texto ao lado do switch
  if (themeLabel) {
    themeLabel.textContent = isDark ? 'Modo Escuro' : 'Modo Claro';
  }
}

// Aplica o tema salvo do localStorage ao carregar a página
function applySavedTheme() {
  const savedTheme = localStorage.getItem('theme');
  const isDark = savedTheme === 'dark';

  document.body.classList.toggle('dark-mode', isDark);

  if (themeSwitch) {
    themeSwitch.checked = isDark;
  }

  if (themeLabel) {
    themeLabel.textContent = isDark ? 'Modo Escuro' : 'Modo Claro';
  }
}

// Alterna a visibilidade do menu dropdown
function toggleDropdownMenu() {
  const isVisible = dropdownMenu.style.display === 'flex';
  dropdownMenu.style.display = isVisible ? 'none' : 'flex';
}

// Fecha o menu ao clicar em um link ou botão dentro dele
function closeDropdownOnLinkClick() {
  dropdownMenu.querySelectorAll('a, button').forEach(el => {
    el.addEventListener('click', () => {
      dropdownMenu.style.display = 'none';
    });
  });
}

// Inicializa os eventos
function initializeMenuDropdown() {
  applySavedTheme();

  toggleBtn.addEventListener('click', toggleDropdownMenu);
  themeSwitch.addEventListener('click', toggleTheme);
  closeDropdownOnLinkClick();
}

// Aguarda o carregamento do DOM
window.addEventListener('DOMContentLoaded', initializeMenuDropdown);
