from lib import *
from tkinter import *
from tkinter import ttk
janela=Tk()
janela.title("Biblioteca")

# Botão de mostrar a biblioteca
showimg=PhotoImage(file=r"C:\Users\ander\OneDrive\Documentos\MeusProjetos\Atividades-PEOO\Listas\Matrizes\Biblioteca\img\141947.png")
showimgmenor=showimg.subsample(4,4) # diminui tamanho da imagem
mostrarbiblioteca=Button(janela,image=showimgmenor,command= mostrarbiblioteca)
mostrarbiblioteca.grid(row=0,column=1)

# Botão de adicionar um livro à biblioteca
addimg=PhotoImage(file=r"C:\Users\ander\OneDrive\Documentos\MeusProjetos\Atividades-PEOO\Listas\Matrizes\Biblioteca\img\livro-com-botao-adicionar.png")
addimgmenor=addimg.subsample(4,4) # diminui tamanho da imagem
addlivro=Button(janela, image=addimgmenor, command=adicionar)
addlivro.grid(row=0, column=0)

# Botão de pesquisas
lupaimg=PhotoImage(file=r"C:\Users\ander\OneDrive\Documentos\MeusProjetos\Atividades-PEOO\Listas\Matrizes\Biblioteca\img\16492.png")
lupaimgmenor=lupaimg.subsample(4,4)
botaobuscar=Button(janela,image=lupaimgmenor,command=janeladebuscas)
botaobuscar.grid(row=1,column=0)

# Botão de remover um livro da biblioteca
delimg=PhotoImage(file=r"C:\Users\ander\OneDrive\Documentos\MeusProjetos\Atividades-PEOO\Listas\Matrizes\Biblioteca\img\2012132.png")
delimgmenor=delimg.subsample(4,4)
dellivro=Button(janela,image=delimgmenor,command=deletar)
dellivro.grid(row=1,column=1)

janela.mainloop() # Mainloop