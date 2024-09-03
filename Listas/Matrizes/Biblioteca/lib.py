from tkinter import *
biblioteca=[
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943],
    ["Romeu e Julieta", "William Shakespeare", 1597]
]

def mostrar(texto,j,r,c): # Mostrar texto em determinado grid
    label=Label(j,text=texto)
    label.grid(row=r,column=c)

def mostrarbiblioteca(): # Mostra a biblioteca inteira em uma nova janela
    novajanela=Tk()
    novajanela.title("Biblioteca")
    
    titulos=Label(novajanela,text="Título")
    titulos.grid(row=0, column=0)
    
    autores=Label(novajanela,text="Autor")
    autores.grid(row=0, column=1)
    
    datas=Label(novajanela,text="Ano de publicação")
    datas.grid(row=0, column=2)
    
    for i in range(len(biblioteca)): # Coloca todos os dados dos livros em linhas e colunas da nova janela
        for j in range(3):
            label=Label(novajanela,text=biblioteca[i][j])
            label.grid(row=i+1, column=j)
    novajanela.mainloop()

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
        [biblioteca.append([tituloinput.get(), autorinput.get(), datainput.get()]),
        mostrar("Livro adicionado!", janelaadd,3,0)])
    salvar.grid(row=3,column=1)
    janelaadd.mainloop()

def percorrermatriz(coluna,busca,a):
    x=[]
    for i in range(len(a)):
        if busca==a[i][coluna]:
            x.append(a[coluna])
    return(x)

def pesquisatitulo():
    pesquisar=Tk()
    
    titulo=Entry(pesquisar)
    buscar=Button(pesquisar,text="Buscar título",command=lambda: mostrarbiblioteca())
    buscar.grid(row=0, column=0)
    
    pesquisar.mainloop()

def janeladebuscas():
    buscasjanela=Tk()
    
    tituloimg=PhotoImage(file=r"C:\Users\ander\OneDrive\Documentos\MeusProjetos\Atividades-PEOO\Listas\Matrizes\Biblioteca\img\pngtree-notebook-icon-png-image_8993869.png")
    tituloimgmenor=tituloimg.subsample(4,4)
    titulobotao=Button(buscasjanela,image=tituloimgmenor,command=pesquisatitulo)
    titulobotao.grid(row=1,column=1)
    
    buscasjanela.mainloop()