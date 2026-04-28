# 📚 Sistema de Biblioteca

Um sistema CRUD desenvolvido em Python para gerenciamento de livros diretamente no terminal.

---

## 🚀 Funcionalidades

- 📋 Cadastrar livros
- 🔎 Buscar livros por título ou ID
- 📖 Listar todos os livros
- 📝 Editar informações de um livro
- 🚮 Deletar livros

---

## 🛠 Tecnologias Utilizadas

- 🐍 Python
- 🗄 SQLite

---

## 📁 Estrutura do Projeto

```text
src/
├── database/   # Acesso ao banco de dados (DAO)
├── ui/         # Interface com o usuário (terminal)
├── utils/      # Funções auxiliares (entrada e saída)
├── models/     # Estrutura de dados (Livro)
└── main.py     # Fluxo do programa
```

---

## ▶ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/jvalencio/sistema-biblioteca.git
```

### 2. Acesse a pasta do projeto

```bash
cd sistema-biblioteca
```

### 3. Crie o ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual

**Windows (PowerShell)**

```bash
.venv\Scripts\Activate.ps1
```

**Windows (CMD)**

```bash
.venv\Scripts\activate.bat
```

**Linux / macOS / WSL**

```bash
source .venv/bin/activate
```

### 5. Executando o projeto

```bash
python -m src.main
```

---

## 💡 Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar:

- Estrutura de projetos em Python
- Separação de responsabilidades (UI, Database, Utils)
- Operações CRUD com banco de dados
- Boas práticas de organização e documentação

---

## 🧪 Aprendizados

- Arquitetura em camadas (MVC simplificado)
- Uso de SQLite com Python
- Modularização de código
- Boas práticas de CLI

---

## 📌 Status do Projeto

✅ Projeto finalizado.

---

## 👨‍💻 Autor

Desenvolvido por João Victor Valencio.
