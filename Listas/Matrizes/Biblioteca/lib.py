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
    for i in range(len(biblioteca)):
        label=Label(novajanela,text=biblioteca[i])
        label.grid(row=i, column=0)
    novajanela.mainloop()

def adicionar():
    a=[]
    