def q1():
    a=[0,1,2,3,4,5,6,7,8,9]
    x=float(input("Número: "))
    m=[]
    for i in a:
        m.append(i*x)
    print(m)

def q2():
    r=[]
    for i in range(20):
        x=float(input(f"Número {i+1}: "))
        r.append(x)
    r.reverse()
    print(r)

def q3():
    a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    b=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15]
    soma=[]
    for i in range(len(a)):
        soma.append(a[i]+b[i])
    print(soma)

def q4():
    temp=[30,28,29,32,33,34,32,31,31,30,29,30]
    print(f"Menor temperatura do ano foi de {min(temp)}°")
    print(f"Maior temperatura do ano foi de {max(temp)}°")
    print(f"Temperatura média do ano foi de {(sum(temp))/len(temp)}°")

def q5():
    numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    n=float(input("Número: "))
    quantidade=0
    for i in numeros:
        if i==n:
            quantidade+=1
    print(f"O número {n} aparece {quantidade} vezes.")

def q6():
    quantidades=[0,1,2,3,4,5,6,7,8,9]
    precos=[20,22,19,23,25,30,18,19.5,18.5,21]
    for i in range(len(quantidades)):
        print(f"O vendedor {i+1} vendeu {quantidades[i]} peças e obteve R${quantidades[i]*precos[i]}")

def q7():
    gabarito=["a","a","a","b","b","b","c","c","c","d"]
    gabaritodoaluno=[]
    todos={}
    nota=0
    for i in range(15):
        nota=0
        matricula=input("Matrícula: ")
        for i in range(10):
            r=input(f"Resposta da questão {i+1}: ")
            if r==gabarito[i]:
                nota+=1
        todos[matricula]=nota
    print(todos)
q7()