def adicionar_livro(biblioteca,titulo,autor,ano):
    biblioteca.append([titulo,autor,ano])
    return biblioteca

def buscar_livro(biblioteca,titulo):
    lista = []
    for livro in biblioteca:
        if livro[0].lower() == titulo.lower():
            lista.append(["TITULO: ", livro[0], ". AUTOR: ", livro[1], ". ANO: ", livro[2]])
            return lista
    else: 
        return ("livro não encontrado!")

def contar_livros_por_autor(biblioteca,autor):
    contador=0
    for i in range(len(biblioteca)):
        if autor==biblioteca[i][1].lower():
            contador+=1
    return(contador)

def listar_livros_por_ano(biblioteca):
    anos = {}
    for livro in biblioteca:
        ano = livro[2]
        if ano in anos:
            anos[ano]+=1
        else:
            anos[ano] = 1
    return anos

def remover_livros(biblioteca,titulo):
    titulo = titulo.lower()
    for livro in biblioteca:
        if livro[0].lower() == titulo:  
            biblioteca.remove(livro) 
            return ("o livro foi removido!")
    return ("livro nao encontrado!")
def sair():
    return "Biblioteca fechada."