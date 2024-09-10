from lib import *

biblioteca=[["a cinco passos de voce", "Rachel Lippincott", "2019"],
            ["como eu era antes de voce", "Jojo Moyes", "2012"],
            ["depois de voce", "Jojo Moyes", "2015"],
            ["ainda sou eu", "Jojo Moyes", "2018"],
            ["o pequeno principe", "Antoine de Saint-Exupéry", "1943"],
            ["1984", "George Orwell", "1949"],
            ["a mao e a luva", "Machado de Assis", "1879"],
            ["dom casmurro", "Machado de Assis", "1899"]]

menu = [["BIBLIOTECA"],
        ["MENU DE OPCOES:"],
        ["1. Adicionar livro."],
        ["2. Listar todos os livros."],
        ["3. Buscar livro."],
        ["4. Contar livros por autor."],
        ["5. Listar livros por ano."],
        ["6. Remover livro."],
        ["7. Sair."]]

def imprimir_menu(menu):
    for linha in menu:
        print(" ".join(linha))

imprimir_menu(menu)

opcao = int(input(" escolha uma opcao: "))

if opcao == 1:
    titulo = input("titulo: ")
    autor = input("autor: ")
    ano = input("ano: ")
    adicionar_livro(biblioteca,titulo,autor,ano)
    for livro in biblioteca:
        print("TITULO:", livro[0], ". AUTOR:", livro[1], ". ANO:", livro[2])

elif opcao == 2:
    for livro in biblioteca:
        print("TITULO:", livro[0], ". AUTOR:", livro[1], ". ANO:", livro[2])

elif opcao == 3:
    titulo = input("titulo que deseja buscar: ").strip().lower()
    print(buscar_livro(biblioteca,titulo))
            
elif opcao == 4:
    autorinput=input("autor que deseja buscar: ").lower()
    numero = contar_livros_por_autor(biblioteca,autorinput)
    print("Esse autor tem",numero,"livros.")

elif opcao == 5:
    anos = listar_livros_por_ano(biblioteca)
    print("anos: ", anos)

elif opcao == 6:
    titulo = input("Título do livro que deseja remover: ").strip().lower()
    print(remover_livros(biblioteca, titulo))
    for livro in biblioteca:
        print("TITULO:", livro[0], ". AUTOR:", livro[1], ". ANO:", livro[2])

elif opcao == 7:
    print('BIBLIOTECA FECHADA')