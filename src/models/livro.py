class Livro:
    """
    Representa um livro com informações básicas como
    título, autor, ano de lançamento e gênero.
    """
    def __init__(self, titulo: str, autor: str, lancamento: int, genero: str) -> None:
        """Inicializa um novo livro.

        Args:
            titulo (str): Nome do livro.
            autor (str): Autor do livro.
            lancamento (int): Ano de lançamento.
            genero (str): Gênero do livro.
        """
        self.titulo = titulo
        self.autor = autor
        self.lancamento = lancamento
        self.genero = genero
