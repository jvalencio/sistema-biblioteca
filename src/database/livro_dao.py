from src.database import conectar
from src.models import Livro


def cadastrar(livro: Livro) -> None:
    """
    Cadastra um novo livro no banco de dados.

    Args:
        livro (Livro): Objeto contendo os dados do livro.
    """
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO livros (titulo, autor, lancamento, genero)
    VALUES (?, ?, ?, ?)
    """,
    (livro.titulo, livro.autor, livro.lancamento, livro.genero)
    )

    conn.commit()
    conn.close()


def buscar_titulo(titulo: str) -> list[tuple]:
    """
    Busca livros pelo título no banco de dados.

    Args:
        titulo (str): Termo de busca.

    Returns:
        list[tuple]: Lista contendo os livros encontrados ou vazia.
    """
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros WHERE titulo LIKE ?", (f"%{titulo}%",))

    resultado = cursor.fetchall()

    conn.close()
    return resultado


def buscar_id(id_livro: int) -> list[tuple]:
    """
    Busca um livro pelo ID no banco de dados.

    Args:
        id_livro (int):Identificador do livro.

    Returns:
        list[tuple]: Lista contendo o livro encontrado ou vazia.
    """
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros WHERE id = ?", (id_livro,))
    resultado = cursor.fetchall()

    conn.close()
    return resultado


def listar() -> list[tuple]:
    """
    Retorna todos os livros do banco de dados.

    Returns:
        list[tuple]: Lista de livros cadastrados.
    """
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    conn.close()
    return livros


def editar_titulo(id_livro: int, titulo: str) -> None:
    """
    Atualiza o título de um livro no banco de dados.

    Args:
        id_livro (int): Identificador do livro.
        titulo (str): Novo título.
    """
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("UPDATE livros SET titulo = ? WHERE id = ?", (titulo, id_livro))

    conn.commit()
    conn.close()


def editar_autor(id_livro: int, autor: str) -> None:
    """
    Atualiza o autor de um livro no banco de dados.

    Args:
        id_livro (int): Identificador do livro.
        autor (str): Novo autor.
    """
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("UPDATE livros SET autor = ? WHERE id = ?", (autor, id_livro))

    conn.commit()
    conn.close()


def editar_lancamento(id_livro: int, lancamento: int) -> None:
    """
    Atualiza o ano de lançamento de um livro no banco de dados.

    Args:
        id_livro (int): Identificador do livro.
        lancamento (int): Novo ano de lançamento.
    """
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("UPDATE livros SET lancamento = ? WHERE id = ?", (lancamento, id_livro))

    conn.commit()
    conn.close()


def editar_genero(id_livro: int, genero: str) -> None:
    """
    Atualiza o gênero de um livro no banco de dados.

    Args:
        id_livro (int): Identificador do livro.
        genero (str): Novo gênero.
    """
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("UPDATE livros SET genero = ? WHERE id = ?", (genero, id_livro))

    conn.commit()
    conn.close()


def deletar(id_livro: int) -> None:
    """
    Remove um livro do banco de dados pelo ID.

    Args:
        id_livro (int): Identificador do livro.
    """
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM livros WHERE id = ?", (id_livro,))

    conn.commit()
    conn.close()
