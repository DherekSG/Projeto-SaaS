const imagens = document.querySelectorAll('.carrossel-imagens img');
  let indiceAtual = 0;

  function trocarImagem() {
    imagens.forEach((img, index) => {
      img.classList.toggle('active', index === indiceAtual);
    });
    indiceAtual = (indiceAtual + 1) % imagens.length;
  }

  trocarImagem();
  setInterval(trocarImagem, 4000); 