from src.database import buscar_titulo
from src.ui import linha, cabecalho, limpar_terminal
from src.utils import ler_opcao, ler_nome, formatar_livros


def buscar_livro() -> None:
    """
    Lê o título do livro e exibe os livros encontrados.
    """
    while True:
        tamanho = cabecalho("busca por título")

        titulo = ler_nome("Título do livro: ", tamanho)

        resultado = buscar_titulo(titulo)

        linha(tamanho)

        formatar_livros(resultado, tamanho)

        opcoes = [
            "🔍 Continuar buscando",
            "🔙 Retornar ao menu inicial"
        ]

        if ler_opcao(opcoes, tamanho) == 2:
            limpar_terminal()
            break

        limpar_terminal()
