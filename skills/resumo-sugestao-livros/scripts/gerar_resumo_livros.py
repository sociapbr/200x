#!/usr/bin/env python3
"""Gera um resumo em Markdown do catálogo de livros do 200x."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def carregar_livros(caminho: Path) -> list[dict]:
    conteudo = caminho.read_text(encoding="utf-8")
    dados = json.loads(conteudo)
    if not isinstance(dados, list):
        raise ValueError("O JSON deve conter uma lista de livros.")
    return dados


def resumo_livro(livro: dict) -> str:
    titulo = livro.get("titulo", "Sem título")
    autor = livro.get("autor", "Autor não informado")
    categoria = livro.get("categoria", "Sem categoria")
    resumo = livro.get("conteudo") or livro.get("descricao") or "Resumo não disponível no catálogo."
    link = livro.get("link", "")

    linhas = [
        f"### {titulo}",
        f"- Autor: {autor}",
        f"- Categoria: {categoria}",
        f"- Resumo: {resumo}",
    ]

    if link:
        linhas.append(f"- Compra: {link}")

    return "\n".join(linhas)


def gerar_markdown(livros: list[dict], limite: int) -> str:
    selecionados = livros[:limite] if limite > 0 else livros
    partes = ["# Resumo de livros (200x)", ""]
    for livro in selecionados:
        partes.append(resumo_livro(livro))
        partes.append("")
    return "\n".join(partes).rstrip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Gerar resumo em Markdown dos livros do 200x")
    parser.add_argument(
        "--input",
        default="data/livros-referencia.json",
        help="Caminho para o arquivo JSON de livros",
    )
    parser.add_argument(
        "--output",
        default="",
        help="Arquivo de saída Markdown. Se vazio, imprime no stdout.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=5,
        help="Quantidade máxima de livros no resumo. Use 0 para todos.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    livros = carregar_livros(Path(args.input))
    markdown = gerar_markdown(livros, args.limit)

    if args.output:
        Path(args.output).write_text(markdown, encoding="utf-8")
        print(f"Resumo salvo em: {args.output}")
    else:
        print(markdown)


if __name__ == "__main__":
    main()
