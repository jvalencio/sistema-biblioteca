import os
import sys
import subprocess
from time import sleep


def linha(tamanho: int) -> None:
    """
    Imprime uma linha de '=' com o tamanho informado.
    """
    print("=" * tamanho)


def cabecalho(titulo: str) -> int:
    """
    Imprime um cabeçalho formatado no terminal.

    Args:
        titulo (str): Texto do título.

    Returns:
        int: Tamanho total do cabeçalho gerado.
    """
    tamanho = len(titulo) + 50
    titulo_formatado = f" {titulo.upper()} "

    linha(tamanho)
    print(titulo_formatado.center(tamanho, "-")) 
    linha(tamanho)

    return tamanho


def limpar_terminal() -> None:
    """
    Limpa o terminal e exibe uma simulação de carregamento.
    """
    sleep(0.5)

    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)

    for c in range(101):
        sys.stdout.write(f"\r⌛ Processando: {c}%")
        sys.stdout.flush()
        sleep(0.01)
    
    sleep(0.3)
    subprocess.run(comando, shell=True)
