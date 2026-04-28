from src.database import cadastrar
from src.models import Livro
from src.ui import linha, cabecalho, limpar_terminal
from src.utils import ler_opcao, ler_genero, ler_lancamento, ler_nome


def cadastrar_livro() -> None:
    """
    Lê as informações do livro e cadastra um novo livro no banco de dados.
    """
    while True:
        tamanho = cabecalho("cadastro de livro")

        titulo = ler_nome("Título: ", tamanho)
        autor = ler_nome("Autor: ", tamanho)
        lancamento = ler_lancamento(tamanho)
        genero = ler_genero(tamanho)

        livro = Livro(titulo, autor, lancamento, genero)

        cadastrar(livro)

        print("✅ Livro cadastrado com sucesso!")
        linha(tamanho)

        opcoes = [
            "📋 Continuar cadastrando",
            "🔙 Retornar ao menu inicial"
        ]

        if ler_opcao(opcoes, tamanho) == 2:
            limpar_terminal()
            break

        limpar_terminal()
