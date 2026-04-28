from src.database import listar
from src.ui import cabecalho, limpar_terminal
from src.utils import ler_opcao, formatar_livros


def listagem_completa() -> None:
    """
    Exibe no terminal a listagem completa dos livros cadastrados no banco de dados.
    """
    tamanho = cabecalho("listagem completa dos livros")

    livros = listar()
    formatar_livros(livros, tamanho)

    opcoes = ["🔙 Retornar ao menu inicial"]

    if ler_opcao(opcoes, tamanho) == 1:
        limpar_terminal()
        return
