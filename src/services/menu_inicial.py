from src.ui import cabecalho
from src.utils import ler_opcao


def menu_inicial() -> tuple[int, int]:
    """
    Exibe o menu incial e retorna a escolha do usuário e o tamanho da tela.

    Returns:
        tuple[int, int]: Uma tupla contendo:
            - A opção escolhida pelo usuário.
            - O tamanho calculado da interface.
    """
    tamanho = cabecalho("biblioteca de marília")
    
    opcoes = [
        "📋 Cadastrar livro",
        "🔍 Buscar livro",
        "📖 Listagem completa",
        "📝 Editar livro",
        "🚮 Deletar livro",
        "🔚 Sair"
    ]

    escolha = ler_opcao(opcoes, tamanho)

    return escolha, tamanho
