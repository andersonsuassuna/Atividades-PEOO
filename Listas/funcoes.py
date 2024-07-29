def q1():
    def paridade(i):
        if i%2==0:
            return "Par"
        else:
            return "Ímpar"
    x=int(input("Número: "))
    print(paridade(x))

def q2():
    def media_aritmetica(i):
        return sum(i)/len(i)
    def media_ponderada(i, p):
        contador=0
        final=[]
        for a in range(len(i)): # pega o nº valor de cada lista e multiplica eles
            final.append((i[contador])*(p[contador]))
            contador+=1
        return(sum(final)/sum(p))
    lista=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    pesos=[1, 4, 3, 4, 2, 2, 1, 2, 3]
    print (media_aritmetica(lista))
    print (media_ponderada(lista, pesos))

def q3():
    def soma(lista): # no caso essa função faz a mesma coisa da função sum()
        somafinal=0
        contador=0
        for i in range(len(lista)):
            somafinal=somafinal+(lista[contador])
            contador+=1
        return(somafinal)

    def mostrar(i):
        for a,b in i.items(): # essa função items() serve para pegar o valor respectivo de cada objeto, no caso do nome, idade e curso, né?
            print(f"{a}: {b}.")

    numeros=[1,2,3,4,5,6,7,8,9]
    print(soma(numeros))

    dados={"Nome":"Anderson", "Idade":"16 (vou fazer 17 dia 01/08 ^^)", "Curso":"Informática"}
    mostrar(dados)