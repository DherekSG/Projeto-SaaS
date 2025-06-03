  const toggleBtn = document.getElementById('toggle-theme-btn');

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

  toggleBtn.addEventListener('click', toggleTheme);

  window.addEventListener('load', () => {
    const savedTheme = localStorage.getItem('theme');
    if(savedTheme === 'dark') {
      document.body.classList.add('dark-mode');
    } else {
      document.body.classList.remove('dark-mode');
    }
  });
  