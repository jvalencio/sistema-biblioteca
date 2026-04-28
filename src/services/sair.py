from time import sleep

from src.ui import linha


def sair(tamanho: int) -> None:
    """
    Exibe uma mensagem de encerramento no terminal com efeito de digitação

    Args:
        tamanho (int): Tamanho da linha separadora.
    """
    texto = f" ENCERRANDO O PROGRAMA ".center(tamanho, "-")

    for caracter in texto:
        print(caracter, end="", flush=True)
        sleep(0.03)

    print()
    linha(tamanho)
