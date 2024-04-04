def q1():
    import itertools as it
    for i in it.count():
        n1=float(input("x: "))
        n2=float(input("y: "))
        op=input("operação: ")
        if op=="+":
            r=n1+n2
        elif op=="-":
            r=n1-n2
        elif op=="*":
            r=n1*n2
        elif op=="/":
            r=n1/n2
        print(f"Resultado: {r}")
        sn=input("Deseja parar de realizar operações? (s): ")
        if sn == "s":
            break
    print("Obrigado por usar nossa calculadora!")

def q2():
    areas=[]
    for i in range (5):
        l=float(input("Lado do quadrado: "))
        if l<0:
            print("Não são aceitos valores negativos!")
            continue
        print(f"Área: {l*l}")
        areas.append(l)
    print(f"O maior quadrado foi o de área {l*l} (lado {l})")

def q3():
    for i in range (10):
        vc=input("Digite uma letra: ")
        vc=vc.lower()
        if vc.isalpha():
            if vc=="a" or vc=="e" or vc=="i" or vc=="o" or vc=="u":
                print("Vogal!")
            elif len(vc)!=1:
                print("Digite apenas UMA letra!")
                continue
            else:
                print ("Consoante!")
        else:
            print("Só são permitidas letras!")
            continue

def q4():
    n=0
    for i in range (10):
        n1=float(input(f"Nota 1 do aluno {n+1}: "))
        n2=float(input(f"Nota 2 do aluno {n+1}: "))
        if (n1+n2)/2>=7:
            print(f"Aluno {n+1} aprovado!")
        else:
            print(f"Aluno {n+1} reprovado!")
        n=n+1

def q5():
    l=[]
    n=int(input("Quantos números? "))
    for i in range(n):
        cont=1
        x=float(input(f"Número {cont}: "))
        l.append(x)
        cont=cont+1
    soma=sum(l)
    print(f"A média foi de {round(soma/n,2)}.")

def q6():
    for i in range(5):
        a=int(input("A: "))
        b=int(input("B: "))
        c=a
        a=b
        b=c
        if a<0:
            print("a é negativo!")
        elif a==0:
            print("a é zero!")
        else:
            print("a é positivo!")
        if b<0:
            print("b é negativo!")
        elif b==0:
            print("b é zero!")
        else:
            print("b é positivo!")
        print(a,b)

def q7():
    import itertools as it
    for i in it.count():
        anos=int(input("Anos: "))
        cpd=int(input("Cigarros por dia: "))
        pcc=float(input("Preço de carteira com 20 cigarros: "))
        cpa=(anos*365)*cpd
        print("Você gastou R${} com cigarros".format((cpa*pcc)/20))
        sn=input("Deseja parar? (s): ")
        if sn=="s":
            break
    print("Obrigado por usar nossa calculadora!")

def q8():
    import itertools as it
    for i in it.count():
        n=input("Nome: ")
        i=int(input("Idade: "))
        if i>=50:
            p="está perto de se aposentar."
        else:
            p="não está perto de se aposentar."
        print("Seu nome é {} e você tem {} anos. Além disso, você {}".format(n,i,p))
        sn=input("Deseja parar? (s): ")
        if sn=="s":
            break
    print("Obrigado!")

def q9():
    for i in range(30):
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
    import itertools as it
    for i in it.count():
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
        sn=input("Deseja calcular denovo? (s): ")
        if sn !="s":
            break
    print("Obrigado por usar nossa calculadora!")

def q12():
    for i in range(2,1000,2):
        print(i)

def q13():
    for i in range(1001,2000):
        print(i)

def q14():
    n=int(input("Tabuada do: "))
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

def q15():
    useroriginal="AndersonSuassuna"
    senhaoriginal="suassuna123"
    if useroriginal==senhaoriginal:
        print("Seus dados originais não podem ser iguais! Corrija-os!")
        exit()

    user=input("Nome de usuário: ")
    senha=input("Senha: ")
    if user==senha:
        print("O usuário e a senha não podem ser iguais!")
        exit()
    if user==useroriginal and senha==senhaoriginal:
        print("Você fez login com sucesso!")
    else:
        print("Seu usuário ou senha estão incorretos!")

def q16():
    import itertools as it
    pares=[]
    impares=[]
    for i in it.count():
        n=int(input("Informe o número: "))
        if n%2==0:
            pares.append(n)
        else:
            impares.append(n)
        sn=input("Deseja informar outro número? (s): ")
        if sn!="s":
            break
    print(f"Foram {len(pares)} números pares e {len(impares)} números ímpares")