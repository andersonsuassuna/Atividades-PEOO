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
q7()