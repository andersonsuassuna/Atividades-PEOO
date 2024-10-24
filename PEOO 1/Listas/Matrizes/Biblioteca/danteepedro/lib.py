def adicionar_livro(livros, titulo, autor, ano):
    """
    Adiciona um novo livro à matriz de livros.
    """
    livros.append([titulo, autor, ano])

def buscar_livro(livros, titulo):
    """
    Busca um livro pelo título na matriz de livros.
    """
    for livro in livros:
        if livro[0].lower() == titulo.lower():
            return livro

def contar_livros_por_autor(livros):
    """
    Conta o número de livros de cada autor presente na matriz.
    Retorna uma lista com cada autor e o número de livros correspondente.
    """
    contagem = {}
    for livro in livros:
        autor = livro[1]
        if autor in contagem:
            contagem[autor] += 1
        else:
            contagem[autor] = 1
    return list(contagem.items())

def listar_livros_por_ano(livros, ano):
    """
    Retorna uma lista de livros publicados em um determinado ano.
    """
    livros_ano = [livro for livro in livros if livro[2] == ano]
    return livros_ano

def remover_livro(livros, titulo):
    """
    Remove um livro da matriz pelo título.
    Retorna True se o livro foi removido, ou False se o livro não foi encontrado.
    """
    for i, livro in enumerate(livros):
        if livro[0].lower() == titulo.lower():
            del livros[i]
            return True
    return False
