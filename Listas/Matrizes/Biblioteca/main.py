from lib import *
from tkinter import *
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
botaobuscar.grid(row=0,column=2)

janela.mainloop() # Mainloop