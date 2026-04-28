from src.database import criar_tabela
from src.ui import limpar_terminal
from src.services import (
    listagem_completa,
    menu_inicial,
    cadastrar_livro,
    buscar_livro,
    editar_livro,
    deletar_livro,
    sair
)


def main() -> None:
    """
    Inicializa o sistema e gerencia o menu principal,
    executando as ações conforme a escolha do usuário.
    """
    criar_tabela()

    while True:
        opcao, tamanho = menu_inicial()

        if opcao == 6:
            sair(tamanho)
            break

        limpar_terminal()

        match opcao:
            case 1:
                cadastrar_livro()
            case 2:
                buscar_livro()
            case 3:
                listagem_completa()
            case 4:
                editar_livro()
            case 5:
                deletar_livro()


if __name__ == "__main__":
    main()
