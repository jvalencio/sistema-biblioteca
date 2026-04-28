from datetime import datetime

from src.ui import linha


def ler_lancamento(tamanho: int) -> int:
    """
    Lê o ano de lançamento do livro, garantindo que seja um
    número inteiro e que não seja maior que o ano atual.

    Args:
        tamanho (int): Tamanho da linha separadora.

    Returns:
        int: Ano de lançamento válido.
    """
    ano_atual = datetime.now().year

    while True:
        try:
            ano_lancamento = int(input("Ano de lançamento: "))
        except ValueError:
            print("❌ Erro: Tipo da entrada inválido.")
            linha(tamanho)
        else:
            if ano_lancamento > ano_atual:
                print("❌ Erro: Ano de lançamento inválido.")
                linha(tamanho)
            else:
                return ano_lancamento


def ler_id(tamanho: int) -> int:
    """
    Lê o ID do livro, garantindo que seja um número inteiro maior que zero.

    Args:
        tamanho (int): Tamanho da linha separadora.

    Returns:
        int: ID em formato válido.
    """
    while True:
        try:
            id = int(input("Informe o ID: "))
        except ValueError:
            print("❌ Erro: Tipo da entrada inválido.")
            linha(tamanho)
        else:
            if id <= 0:
                print("❌ Erro: Formato de ID inválido.")
                linha(tamanho)
            else:
                linha(tamanho)
                return id
