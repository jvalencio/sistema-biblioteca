from typing import TypeAlias

from src.ui import linha

LivroTuple: TypeAlias = tuple[int, str, str, int, str]

def formatar_livros(livros: list[LivroTuple], tamanho: int) -> None:
    """
    Exibe uma lista de livros formatada no terminal.

    Args:
        livros (list[LivroTuple]): Lista de livros a serem exibidos.
        tamanho (int): Tamanho da linha separadora.
    """
    if not livros:
        print("❌ Nenhum livro encontrado.")
    else:
        encontrados = len(livros)

        if encontrados == 1:
            print("✅ 1 livro encontrado.\n")
        else:
            print(f"✅ {encontrados} livros encontrados.\n")

        for id, titulo, autor, lancamento, genero in livros:
            print(f"ID: {id} - {titulo} | {autor} | {lancamento} | {genero}")

    linha(tamanho)
