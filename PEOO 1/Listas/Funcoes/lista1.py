import itertools as it
lista=[]
def q1():
    def reverse(lista):
        for i in it.count():
            n=float(input("Número: "))
            lista.append(n)
            sn=input("Continuar? ('s' ou 'n'): ")
            if sn!="s":
                break
        lista2=[]
        for i in range(len(lista)):
            lista2.append(lista[i])
        for i in range(len(lista)):
            lista2[-(i)]=lista[i-1]
        return(lista2)
    print(reverse(lista))

def q2():
    alturas=[]
    def mediadealturas(lista):
        soma=0
        for i in it.count():
            n=float(input(f"Altura {i+1}: "))
            soma=soma+n
            lista.append(n)
            sn=input("Continuar? ('s' ou 'n'): ")
            if sn!="s":
                break
        return (soma/len(alturas))
    print(f"Média: {mediadealturas(alturas)}")

def q3():
    numeros=[1,2,3,4,5,6,7,8,9,0]
    def pares(lista):
        parestotais=0
        for i in (lista):
            if i%2==0:
                parestotais+=1
        return parestotais
    print(pares(numeros))