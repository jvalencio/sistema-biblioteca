from src.ui import linha


def ler_nome(texto: str, tamanho: int) -> str:
    """
    Lê um nome digitado, garantindo que não seja vazio e
    que não ultrapasse o tamanho máximo de 40 caractéres.

    Args:
        texto (str): Mensagem exibida no input.
        tamanho (int): Tamanho da linha separadora.

    Returns:
        str: Nome digitado pelo usuário.
    """
    while True:
        nome = input(texto).strip().lower()

        if not nome:
            print("❌ Erro: Entrada vazia.")
            linha(tamanho)
            continue

        if len(nome) > 60:
            print("❌ Erro: Limite de tamanho ultrapassado.")
            linha(tamanho)
            continue
    
        return nome
