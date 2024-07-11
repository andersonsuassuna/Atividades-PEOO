def q6():
    n=int(input("Número: "))
    numerodedivisores=0
    divisor=1
    for i in range(n):
        if n%divisor==0:
            numerodedivisores=numerodedivisores+1
        divisor=divisor+1
    print(f"O número {n} tem {numerodedivisores} divisores")

def q7():
    base=int(input("Base: "))
    expoente=int(input("Expoente: "))
    numerooriginal=base
    for i in range (expoente-1):
        base=base*numerooriginal
    print(base)

def q8():
    n=int(input("Número: "))
    divisores=[]
    divisor=0
    for i in range(n):
        divisor=divisor+1
        if n==divisor:
            break
        if n%divisor==0:
            divisores.append(divisor)
    if n==sum(divisores):
        print(f"O número {n} é perfeito!")
    else:
        print(f"O número {n} não é perfeito!")
    print(divisores)

def q9():
    n=input("Número: ")
    algarismos=[]
    casa=0
    for i in range(len(n)):
        algarismos.append(int(n[casa]))
        casa=casa+1
    print(f"A soma dos dígitos de {n} é {sum(algarismos)}!")

def q10():
    n=int(input("Número: "))
    if (n**(1/2)).is_integer():
        print(f"{n} é um quadrado perfeito!")
    else:
        print(f"{n} não é um quadrado perfeito!")
q10()