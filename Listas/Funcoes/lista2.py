def q1():
    numeros=[1, 2, 3, 4, 5]
    def presente(lista, n):
        for i in lista:
            if i!=n:
                continue
            else:
                return True
        return False
    print(presente(numeros, 6))

def q2():
    listadenotas=[{"Anderson":10}, {"Inácio",9}, {"Pâmela",8}]
    def mostrarnotas(lista,indice):
            return(f"{listadenotas[indice]}")
    print(mostrarnotas(listadenotas,0))