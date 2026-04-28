from src.ui import linha


def ler_opcao(opcoes: list[str], tamanho: int, texto: str = "Escolha uma opção: ") -> int:
    """
    Exibe uma lista de opções e lê a escolha do usuário,
    garantindo que seja um número válido dentro do intervalo.

    Args:
        opcoes (list[str]): Lista de opções disponíveis.
        tamanho (int): Tamanho da linha separadora.
        texto (str, opcional): Mensagem exibida no input.
            Padrão: "Escolha uma opção: ".

    Returns:
        int: Índice da opção escolhida (baseado em 1).
    """
    for i, item in enumerate(opcoes, start=1):
        print(f"[{i}] {item}")

    linha(tamanho)

    while True:
        try:
            opcao = int(input(texto))
        except ValueError:
            print("❌ ERRO: Digite somente números inteiros.")
            linha(tamanho)
        else:
            if 0 < opcao <= len(opcoes):
                linha(tamanho)
                return opcao
            else:
                print("❌ ERRO: Opção inexistente.")
                linha(tamanho)


def ler_genero(tamanho: int) -> str:
    """
    Exibe os gêneros disponíveis e lê a opção escolhida pelo usuário.

    Args:
        tamanho (int): Tamanho da linha separadora.

    Returns:
        str: Gênero selecionado.
    """
    generos = [
        "aventura", "autoajuda", "biografia", "drama",
        "fantasia", "ficção", "ficção científica", "história",
        "mistério", "romance", "suspense", "terror"
    ]

    linha(tamanho)
    opcao = ler_opcao(generos, tamanho, "Escolha o gênero do livro: ")

    return generos[opcao - 1]
