from src.database import listar, buscar_id, deletar
from src.ui import linha, cabecalho, limpar_terminal
from src.utils import ler_opcao, ler_id, formatar_livros


def deletar_livro() -> None:
    """
    Lê o ID do livro cadastrado no banco de dados e exclui caso o ID exista.
    """
    while True:
        tamanho = cabecalho("deletar livro")

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
                "🚮 Confirmar exclusão",
                "📚 Escolher outro livro",
                "🔙 Retornar ao menu inicial"
            ]

            opcao = ler_opcao(opcoes, tamanho)

            if opcao == 1:
                deletar(id_livro)

                print("✅ Livro deletado com sucesso!")
                linha(tamanho)

                opcoes = [
                    "🚮 Continuar deletando",
                    "🔙 Retornar ao menu inicial"
                ]

                opcao = ler_opcao(opcoes, tamanho)

                if opcao == 2:
                    limpar_terminal()
                    break

            elif opcao == 3:
                limpar_terminal()
                break
            
        limpar_terminal()
