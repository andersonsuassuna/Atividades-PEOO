def q1():
    matriz=[
        [1,2],
        [3,4]
    ]
    def transposta(matriz):
        return [[matriz[i][j] for i in range(len(matriz[j]))]for j in range(len(matriz[0]))]

def q2():
    matriz=[
        [1,0],
        [0,1]
    ]
    def identidade(matriz):
        contadorde1=0
        contadorde0=0
        for i in range(len(matriz)):
            if matriz[i][i]==1:
                contadorde1+=1
        if contadorde1!=len(matriz):
            return(False)
        for i in range(len(matriz[0])):
            contadorde0=contadorde0+(matriz[i].count(0))
        if contadorde0==len(matriz)*len(matriz[0])-contadorde1:
            return(True)
        else:
            return(False)
    print(identidade(matriz))

def q3():
    matriz=[
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    def borda(matriz,n):
        if len(matriz)==len(matriz[0]):
            for i in range(len(matriz)):
                matriz[0][i]=n
                matriz[-1][i]=n
                matriz[i][0]=n
                matriz[i][-1]=n
            return(matriz)
        else:
            print("Não é quadrada!")
    print(borda(matriz,1))

def q4():
    