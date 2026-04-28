import sqlite3


def conectar() -> sqlite3.Connection:
    """
    Estabelece conexão com o banco de dados SQLite.

    Returns:
        sqlite3.Connection: Objeto de conexão com o banco de dados.
    """
    return sqlite3.connect("data/biblioteca.db")


def criar_tabela() -> None:
    """
    Cria a tabela 'livros' no banco de dados, caso ela ainda não exista.

    A tabela armazena informações sobre os livros, incluindo
    id, título, autor, ano de lançamento e gênero.
    """
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        autor TEXT,
        lancamento INTEGER,
        genero TEXT
    )
    """)

    conn.commit()
    conn.close()
