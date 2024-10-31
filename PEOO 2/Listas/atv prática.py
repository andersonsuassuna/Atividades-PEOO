class Livro: # Aqui criamos a classe para os livros, dando título, autor e ano de publicação para eles
    def __init__(self,titulo,autor,ano_publicacao):
        self.titulo=titulo
        self.autor=autor
        self.ano_publicacao=ano_publicacao

# Livro 1 e Livro 2 criados
livro1=Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
livro2=Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)

# Mostrando informações dos dois livros
print(f"Título do livro 1: {livro1.titulo}")
print(f"Autor do livro 1: {livro1.autor}")
print(f"Ano de publicação do livro 1: {livro1.ano_publicacao}")
print(f"Título do livro 2: {livro2.titulo}")
print(f"Autor do livro 2: {livro2.autor}")
print(f"Ano de publicação do livro 2: {livro2.ano_publicacao}")

# Novo livro para ver se ele tem as mesmas propriedades do livro1
novo_livro=livro1
novo_livro.autor="Algum autor aí"

print(f"Autor do livro 1: {livro1.autor}")
print(f"Autor do novo livro: {novo_livro.autor}")

print(f"id do livro1: {id(livro1)}")
print(f"id do novo livro: {id(novo_livro)}")

# Criando função de mostrar os dados dos livros
def imprime_livro(livro):
    print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publicacao}")

# Criando uma referência para a função agora criada e vendo elas têm a mesma funcionadade e tipo.
funcaoimpressao=imprime_livro
funcaoimpressao(livro1)
print(type(funcaoimpressao))

# Criando a classe biblioteca
class Biblioteca:
    def __init__(self, nome): # Método __init__ com nome da biblioteca e lista de livros nela
        self.nome=nome
        self.livros=[]

    def adicionar(self,livro): # Método para adicionar um livro à biblioteca
        self.livros.append(livro)

    def listar(self): # Método para listar os livros que tem na biblioteca
        print(f"Livros da biblioteca {self.nome}:")
        for i in self.livros:
            print(f"Título: {i.titulo}. Autor: {i.autor}. Ano: {i.ano_publicacao}.")

    def buscar(self,titulo): # Método para buscar livros pelo título. Quando o título de um livro é igual à busca, ele o adiciona numa lista com os resultados e depois mostra essa lista
        resultados=[]
        for i in self.livros:
            if i.titulo==titulo:
                resultados.append(i)
        print("Resultados da busca:")
        for i in resultados:
            print(f"Título: {i.titulo}. Autor: {i.autor}. Ano: {i.ano_publicacao}.")

    def remover(self,titulo): # Método de remover um livro. Quando achar um livro com o mesmo título da busca ele vai removê-lo da biblioteca
        for i in self.livros:
            if i.titulo==titulo:
                self.livros.remove(i)
                
# Testando métodos da classe Biblioteca
biblioteca=Biblioteca("Biblioteca Central")
biblioteca.adicionar(livro1)
biblioteca.adicionar(livro2)
biblioteca.listar()
biblioteca.buscar("O Pequeno Príncipe")

# Verificando se os dados de um mesmo livro dentro ou fora da biblioteca são alterados simultaneamente
biblioteca.livros[0].autor = "Autor Desconhecido"
print(f"Autor de livro1: {livro1.autor}")
print(f"ID de livro1: {id(livro1)}")
print(f"ID de biblioteca.livros[0]: {id(biblioteca.livros[0])}")

# Criando novos livros e adicionando-os na biblioteca
livro3=Livro("A Revolução dos Bichos", "George Orwell", 1945)
livro4=Livro("Dom Quixote", "Miguel de Cervantes", 1605)
biblioteca.adicionar(livro3)
biblioteca.adicionar(livro4)

# Removendo livro e verificando
biblioteca.remover("Dom Quixote")
biblioteca.listar()

# Verificando se o livro ainda existe na memória mesmo após tirá-lo da biblioteca
print(f"Título de livro4 após remoção: {livro4.titulo}")