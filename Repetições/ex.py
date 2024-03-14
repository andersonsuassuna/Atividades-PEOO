n=1
l=[]
while n<=10:
    x=int(input("Valor: "))
    n=n+1
    l.append(x)
print(f"Lista de números: {l}")
print(f"Maior número: {max(l)}")