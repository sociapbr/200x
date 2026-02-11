---
name: resumo-sugestao-livros
description: Criar resumos curtos de livros de finanças e sugerir próximas leituras com base em tema, nível e objetivo do usuário. Usar quando o pedido envolver recomendar livros, resumir livros, montar listas de leitura, ou transformar o catálogo atual do site 200x em conteúdo de biblioteca/páginas de livro.
---

# Resumo e Sugestão de Livros

## Visão geral

Padronizar a resposta para pedidos de resumo e recomendação de livros de finanças pessoais usando o catálogo atual do projeto 200x.
Priorizar respostas práticas: resumo em linguagem simples, motivo da indicação e próximo passo de leitura.

## Fluxo rápido

1. Identificar o objetivo do usuário (iniciar estudos, sair de dívidas, investir, mentalidade, planejamento).
2. Ler `references/fonte-200x.md` para entender o catálogo e os metadados disponíveis.
3. Se precisar de saída estruturada, executar `scripts/gerar_resumo_livros.py` para gerar base em Markdown.
4. Entregar recomendação final com:
   - livro principal;
   - resumo em 3 a 5 frases;
   - 2 a 4 sugestões complementares com justificativa curta.

## Formato recomendado de resposta

Usar a estrutura abaixo sempre que possível:

- **Livro principal**: título + autor.
- **Resumo**: foco no que o leitor aprende e em qual etapa financeira ajuda.
- **Por que ler agora**: benefício prático em 1 frase.
- **Próximas leituras**: lista curta com progressão (básico → intermediário).

## Regras de qualidade

- Adaptar a recomendação ao nível do usuário (iniciante, intermediário, avançado).
- Evitar jargões técnicos sem explicação.
- Não inventar dados bibliográficos; usar apenas informações do catálogo disponível.
- Se faltar informação no catálogo, sinalizar claramente a limitação.
