# Fonte de dados do projeto 200x

## Arquivos de referência

- `data/livros-referencia.json`: catálogo principal de livros da biblioteca.
- `livros/psicologia-financeira.html`: exemplo de página de livro já implementada com título, capa, autor, resumo e CTA de compra.

## Campos encontrados no catálogo

Cada item pode conter:

- `titulo`
- `autor`
- `categoria`
- `descricao` (opcional)
- `conteudo` (opcional)
- `link`
- `imagem`

## Observações de uso

- Alguns títulos podem aparecer duplicados com pequenas variações de nome.
- Priorizar os campos `conteudo` e `descricao` para montar resumos.
- Se `conteudo` não existir, resumir com base em `descricao` e `categoria`.
