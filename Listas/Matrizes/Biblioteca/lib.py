from tkinter import *
import csv

with open(r"C:\Users\ander\OneDrive\Documentos\MeusProjetos\Atividades-PEOO\Listas\Matrizes\Biblioteca\biblioteca.csv", encoding='utf-8') as biblioteca:
    leitor_csv=csv.reader(biblioteca)

def mostrar(texto,j,r,c): # Mostrar texto em determinado grid
    label=Label(j,text=texto)
    label.grid(row=r,column=c)

def mostrarbiblioteca(): # Mostra a biblioteca inteira em uma nova janela
    with open(r"C:\Users\ander\OneDrive\Documentos\MeusProjetos\Atividades-PEOO\Listas\Matrizes\Biblioteca\biblioteca.csv", encoding='utf-8') as biblioteca:
        leitor_csv=csv.reader(biblioteca)
        bib=[]
        for i in leitor_csv:
            bib.append(i)
    novajanela=Tk()
    novajanela.title("Biblioteca")
    
    titulos=Label(novajanela,text="Título")
    titulos.grid(row=0, column=0)
    
    autores=Label(novajanela,text="Autor")
    autores.grid(row=0, column=1)
    
    datas=Label(novajanela,text="Ano de publicação")
    datas.grid(row=0, column=2)
    
    for i in range(len(bib)): # Coloca todos os dados dos livros em linhas e colunas da nova janela
        for j in range(3):
            label=Label(novajanela,text=bib[i][j])
            label.grid(row=i+1, column=j)
    novajanela.mainloop()

def escrevercsv(texto):
    with open(r"C:\Users\ander\OneDrive\Documentos\MeusProjetos\Atividades-PEOO\Listas\Matrizes\Biblioteca\biblioteca.csv", "a", newline='\n') as biblioteca:
        escritor=csv.writer(biblioteca)
        escritor.writerow(texto)

def adicionar(): # Adiciona um novo livro com seus dados fornecidos por Entries
    janelaadd=Tk()
    
    titulo=Label(janelaadd,text="Título: ")
    tituloinput=Entry(janelaadd)
    tituloinput.grid(row=0,column=1)
    titulo.grid(row=0,column=0)
    
    autor=Label(janelaadd,text="Autor: ")
    autorinput=Entry(janelaadd)
    autorinput.grid(row=1,column=1)
    autor.grid(row=1,column=0)
    
    data=Label(janelaadd,text="Ano de publicação: ")
    datainput=Entry(janelaadd)
    datainput.grid(row=2,column=1)
    data.grid(row=2,column=0)
    
    
    # Esse botão executa dois comandos: um para adicionar o livro na matriz e outro para mostrar na tela que o livro foi adicionado
    salvar=Button(janelaadd,text="Adicionar Livro", command=lambda: 
        [escrevercsv([tituloinput.get(), autorinput.get(), datainput.get()]),
        mostrar("Livro adicionado!", janelaadd,3,0)])
    salvar.grid(row=3,column=1)
    janelaadd.mainloop()

def percorrermatriz(coluna,busca): # Anda por toda a matriz conferindo se a busca corresponde a algum item da biblioteca
    x=[]
    for i in range(len(biblioteca)):
        if busca==biblioteca[i][coluna]:
            x.append(biblioteca[i])
    return(x)

def pesquisa(coluna,busca): # Cria uma janela que mostra os resultados da busca
    pesquisar=Tk()
    
    titulos=Label(pesquisar,text="Título")
    titulos.grid(row=0, column=0)
    
    autores=Label(pesquisar,text="Autor")
    autores.grid(row=0, column=1)
    
    datas=Label(pesquisar,text="Ano de publicação")
    datas.grid(row=0, column=2)
    
    for i in range(len(percorrermatriz(coluna,busca))):
        for j in range(3):
            label=Label(pesquisar,text=percorrermatriz(coluna,busca)[i][j])
            label.grid(row=i+1, column=j)
    pesquisar.mainloop()

def janeladebuscas(): # Serve para o usuário escolher por qual valor (título, autor, data) ele vai buscar
    buscasjanela=Tk()
    
    busca=Entry(buscasjanela)
    busca.grid(row=0,column=1)
    
    titulobotao=Button(buscasjanela,text="Título",command=lambda: pesquisa(0,busca.get()))
    titulobotao.grid(row=1,column=0)
    
    autorbotao=Button(buscasjanela,text="Autor",command=lambda: pesquisa(1,busca.get()))
    autorbotao.grid(row=1,column=1)
    
    databotao=Button(buscasjanela,text="Ano de Publicação",command=lambda: pesquisa(2,busca.get()))
    databotao.grid(row=1,column=2)
    
    buscasjanela.mainloop()

def apagar(busca):
    with open(r"C:\Users\ander\OneDrive\Documentos\MeusProjetos\Atividades-PEOO\Listas\Matrizes\Biblioteca\biblioteca.csv", encoding='utf-8') as biblioteca:
        leitor_csv=csv.reader(biblioteca)
        bib=[]
        for i in leitor_csv:
            bib.append(i)
    for i in range(len(bib)):
        if busca==bib[i][0]:
            biblioteca.drop(i)
            break

def deletar():
    remover=Tk()
    
    digite=Label(remover,text="Título do livro: ")
    digite.grid(row=0,column=0)
    
    escreva=Entry(remover)
    escreva.grid(row=0,column=1)
    
    botaodeletar=Button(remover,text="Deletar livro",command=lambda: 
        [apagar(escreva.get()), 
        mostrar("Livro deletado!",remover,1,0)])
    botaodeletar.grid(row=1,column=1)
    remover.mainloop