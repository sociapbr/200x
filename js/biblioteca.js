(function () {
  const listElement = document.getElementById('books-list');
  const errorElement = document.getElementById('books-error');

  function createBookCard(book) {
    const col = document.createElement('div');
    col.className = 'col-md-6 col-lg-4 mil-services-grid-item p-0';

    const card = document.createElement('article');
    card.className = 'mil-service-card-sm mil-book-card';

    const image = document.createElement('img');
    image.className = 'mil-book-cover mil-mb-20';
    image.src = book.imagem;
    image.alt = `Capa do livro ${book.titulo}`;
    image.loading = 'lazy';

    const category = document.createElement('p');
    category.className = 'mil-light mil-mb-15';
    category.textContent = book.categoria;

    const title = document.createElement('h5');
    title.className = 'mil-muted mil-mb-15';
    title.textContent = book.titulo;

    const author = document.createElement('p');
    author.className = 'mil-light mil-mb-15';
    author.textContent = `Autor: ${book.autor}`;

    const description = document.createElement('p');
    description.className = 'mil-light mil-mb-15';
    description.textContent = book.descricao;

    const contentDescription = document.createElement('p');
    contentDescription.className = 'mil-light mil-mb-30';
    contentDescription.textContent = `Conteúdo: ${book.conteudo}`;

    const link = document.createElement('a');
    link.className = 'mil-link mil-light mil-arrow-place';
    link.href = book.link;
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
    link.textContent = 'Ver livro';

    card.appendChild(image);
    card.appendChild(category);
    card.appendChild(title);
    card.appendChild(author);
    card.appendChild(description);
    card.appendChild(contentDescription);
    card.appendChild(link);

    col.appendChild(card);
    return col;
  }

  async function loadBooks() {
    try {
      const response = await fetch('/data/livros-referencia.json', { cache: 'no-store' });

      if (!response.ok) {
        throw new Error(`Erro ao carregar JSON: ${response.status}`);
      }

      const books = await response.json();
      const fragment = document.createDocumentFragment();

      books.forEach((book) => {
        fragment.appendChild(createBookCard(book));
      });

      listElement.innerHTML = '';
      listElement.appendChild(fragment);
    } catch (error) {
      console.error(error);
      errorElement.style.display = 'block';
    }
  }

  loadBooks();
})();
