from src.database import (
    listar,
    buscar_id,
    editar_titulo,
    editar_autor,
    editar_lancamento,
    editar_genero
)
from src.ui import linha, cabecalho, limpar_terminal
from src.utils import (
    ler_opcao,
    ler_nome,
    ler_lancamento,
    ler_genero,
    ler_id,
    formatar_livros
)


def editar_livro() -> None:
    """
    Lê o ID do livro cadastrado no banco de dados e atualiza a
    informação escolhida caso o ID exista.
    """
    while True:
        tamanho = cabecalho("editar informações do livro")

        livros = listar()
        formatar_livros(livros, tamanho)

        id_livro = ler_id(tamanho)
        resultado = buscar_id(id_livro)

        formatar_livros(resultado, tamanho)

        if not resultado:
            opcoes = [
                "📚 Escolher outro livro",
                "🔙 Retornar ao menu inicial"
            ]

            opcao = ler_opcao(opcoes, tamanho)

            if opcao == 2:
                limpar_terminal()
                break

        else:
            opcoes = [
                "📖 Editar título",
                "✍  Editar autor",
                "📅 Editar ano de lançamento",
                "🎭 Editar gênero",
                "📚 Escolher outro livro",
                "🔙 Retornar ao menu inicial"
            ]

            opcao = ler_opcao(opcoes, tamanho)

            match opcao:
                case 1:
                    novo_titulo = ler_nome("Novo título: ", tamanho)
                    editar_titulo(id_livro, novo_titulo)
                case 2:
                    novo_autor = ler_nome("Novo autor: ", tamanho)
                    editar_autor(id_livro, novo_autor)
                case 3:
                    novo_lancamento = ler_lancamento(tamanho)
                    editar_lancamento(id_livro, novo_lancamento)
                case 4:
                    novo_genero = ler_genero(tamanho)
                    editar_genero(id_livro, novo_genero)
                case 6:
                    limpar_terminal()
                    break

            if opcao in [1, 2, 3, 4]:
                linha(tamanho)
                print("✅ Informação do livro atualizada com sucesso!")
                linha(tamanho)

                opcoes = [
                    "📝 Continuar editando",
                    "🔙 Retornar ao menu inicial"
                ]

                opcao = ler_opcao(opcoes, tamanho)

                if opcao == 2:
                    limpar_terminal()
                    break

        limpar_terminal()
