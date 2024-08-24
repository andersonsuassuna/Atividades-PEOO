def q1():
    a=[[2,4,6],[1,3,5],[7,8,9]]
    def somadematriz(matriz):
        soma=0
        for i in range(len(matriz)):
            for j in range (len(matriz[0])):
                soma=soma+matriz[i][j]
        return(soma)
    print(somadematriz(a))

def q2():
    c=[[2,4],[6,8]]
    x=int(input("Número: "))
    def multiplicarmatriz(matriz,n):
        for i in range(len(matriz)):
            for j in range (len(matriz[0])):
                matriz[i][j]*=n
        return(matriz)
    print(multiplicarmatriz(c,x))

def q3():
    d=[[10,20],[30,40],[50,60]]
    def maiordamatriz(matriz):
        maior=0
        for i in range(len(matriz)):
            for j in range (len(matriz[0])):
                if matriz[i][j]>maior:
                    maior=matriz[i][j]
        return(maior)
    print(maiordamatriz(d))

def q4():
    e=[[1,2,3],[4,5,6],[7,8,9]]
    def soma_diagonal_principal(matriz):
        soma=0
        for i in range(len(matriz)):
            soma=soma+matriz[i][i]
        return(soma)
    print(soma_diagonal_principal(e))

def q5():
    estoque=[
        [10,11,14],
        [6,20,12],
        [7,6,3]
    ]
    def exibir_estoque(matriz):
        print(*matriz,sep="\n")
    def atualizar_estoque(matriz,i,j,n):
        matriz[i][j]=n
    exibir_estoque(estoque)
    atualizar_estoque(estoque,0,0,20)
    exibir_estoque(estoque)