def q1():
    x=float(input("x: "))
    y=float(input("y: "))
    op=input("Adição(+), Subtração(-), Multiplicação (*) ou Divisão (/)? ")
    if op=="+":
        print(x+y)
    elif op=="-":
        print (x-y)
    elif op=="*":
        print (x*y)
    elif op=="/":
        print (x/y)
    else:
        print("Operação inválida!")

def q2():
    l=float(input("Lado do quadrado: "))
    if l<0:
        print("O lado não pode ser menor que 0!")
    a=l**2
    print("A área de um quadrado {} x {} é {}".format(l,l,a))

def q3():
    l=input("Letra: ")
    if l=="a" or l=="e" or l=="i" or l=="o" or l=="u":
        print("É vogal!")
    else:
        print("É consoante!")

def q4():
    n1=float(input("Nota 1: "))
    n2=float(input("Nota 2: "))
    m=(n1+n2)/2
    if m>=7:
        print("Aprovado!")
    else:
        print("Reprovado!")

def q5():
    x=float(input("x: "))
    y=float(input("y: "))
    z=float(input("z: "))
    print("Média: {}".format(round((x+y+z)/3), 2))
    print("Maior número: {}".format(max(x,y,z)))

def q6():
    a=input("A:")
    b=input("B: ")
    c=a
    a=b
    b=c
    if a<0:
        print("a é negativo!")
    if b<0:
        print("b é negativo!")
    print(a,b)

def q7():
    anos=int(input("Anos: "))
    cpd=int(input("Cigarros por dia: "))
    pcc=float(input("Preço de carteira com 20 cigarros: "))
    cpa=(anos*365)*cpd
    print("Você gastou R${} com cigarros".format((cpa*pcc)/20))

def q8():
    n=input("Nome: ")
    i=int(input("Idade: "))
    if i>=50:
        p="está perto de se aposentar."
    else:
        p="não está perto de se aposentar."
    print("Seu nome é {} e você tem {} anos. Além disso, você {}".format(n,i,p))

def q9():
    anos=int(input("Quantos anos você tem? "))
    aem=anos*12
    aed=anos*365
    aeh=aed*24
    aemin=aeh*60
    q=input("Gostaria de saber quantos meses (1), dias (2), horas (3) ou minutos (4)? ")
    if q=="1":
        print("Você viveu {} meses.".format(aem))
    elif q=="2":
        print("Você viveu {} dias.".format(aed))
    elif q=="3":
        print("Você viveu {} horas.".format(aeh))
    elif q=="4":
        print("Você viveu {} minutos.".format(aemin))
    else:
        print("Insira um número válido!")

def q10():
    cc=float(input("Consumo do carro em litros/km: "))
    d= float(input("Distância em km: "))
    if cc<0 or d<0:
        print("Não são permitidos valores negativos!")
        exit()
    print("Litros que serão gastos: {}".format(cc*d))

def q11():
    g=float(input("Preço da gasolina: "))
    a=float(input("Preço do álcool: "))
    if g<0 or a<0:
        print("Não são permitidos valores negativos!")
        exit()
    if g<a:
        print("É mais vantajoso abastecer com gasolina!")
    elif g==a:
        print("Os dois têm o mesmo preço!")
    else:
        print("É mais vantajoso abastecer com álcool!")