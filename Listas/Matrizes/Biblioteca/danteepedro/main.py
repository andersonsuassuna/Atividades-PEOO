from lib import *

def menu():
    livros = []
    while True:
        print("\nMenu de Opções:")
        print("1. Adicionar Livro") 
        print("2. Listar Todos os Livros")
        print("3. Buscar Livro por Título")
        print("4. Contar Livros por Autor")
        print("5. Listar Livros por Ano")
        print("6. Remover Livro")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("título do livro: ")
            autor = input("autor do livro: ")
            ano = int(input("ano de publicação: "))
            adicionar_livro(livros, titulo, autor, ano)
            print(f"Livro '{titulo}' adicionado com sucesso.")

        elif opcao == "2":
            print("\nLista de livros:")
            for livro in livros:
                print(f"Título: {livro[0]}, Autor: {livro[1]}, Ano: {livro[2]}")

        elif opcao == "3":
            titulo = input("título do livro: ")
            livro = buscar_livro(livros, titulo)
            if livro:
                print(f"título: {livro[0]}, autor: {livro[1]}, ano: {livro[2]}")
            else:
                print("Livro não encontrado.")

        elif opcao == "4":
            autores = contar_livros_por_autor(livros)
            print("\nquantidade de livros por autor:")
            for autor, contagem in autores:
                print(f"autor: {autor}, quantidade de livros: {contagem}")

        elif opcao=="5":
            ano=int(input("ano de Publicação: "))
            livros_ano = listar_livros_por_ano(livros, ano)
            if livros_ano:
                print(f"\nlivros publicados em {ano}:")
                for livro in livros_ano:
                    print(f"título: {livro[0]}, autor: {livro[1]}")
            else:
                print("nenhum livro encontrado referente ao ano solicitado.")

        elif opcao=="6":
            titulo=input("título do livro: ")
            if remover_livro(livros, titulo):
                print(f"livro '{titulo}' removido com sucesso.")
            else:
                print("livro não encontrado.")

        elif opcao == "7":
            print("saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()