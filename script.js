async function carregarCatalogo() {
  const resposta = await fetch("catalogo.json");
  const catalogo = await resposta.json();
  const container = document.getElementById("catalogo");

  function exibir(lista) {
    container.innerHTML = "";
    lista.forEach(item => {
      const card = document.createElement("div");
      card.className = "card";
      card.innerHTML = `
        <img src="${item.imagem}" alt="${item.nome}">
        <h3>${item.nome}</h3>
        <p>${item.preco}</p>
        <button onclick="comprar('${item.nome}')">COMPRAR</button>
      `;
      container.appendChild(card);
    });
  }

  // Exibe tudo inicialmente
  exibir(catalogo);

  // Barra de pesquisa
  document.getElementById("pesquisa").addEventListener("input", e => {
    const termo = e.target.value.toLowerCase();
    const filtrados = catalogo.filter(item =>
      item.nome.toLowerCase().includes(termo)
    );
    exibir(filtrados);
  });
}

function comprar(nome) {
  const usuarioTelegram = "SEU_USER"; // coloque seu @ do Telegram
  const link = `https://t.me/Nathyelerosa?text=Oi,%20quero%20comprar%20a%20série%20${encodeURIComponent(nome)}`;
  window.open(link, "_blank");
}

carregarCatalogo();
