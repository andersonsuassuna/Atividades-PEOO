def q1():
    sn=input("Deseja realizar uma operação? ")
    sn=sn.lower()
    while sn=="sim":
        op=input("Operação (+, -, *, /): ")
        n1=float(input("Número 1: "))
        n2=float(input("Número 2: "))
        if op=="+":
            r=n1+n2
        elif op=="-":
            r=n1-n2
        elif op=="*":
            r=n1*n2
        elif op=="/":
            r=n1/n2
        print(f"Resultado: {r}")
        sn=input("Deseja realizar mais uma operação? ")
    print("Obrigado por usar nossa calculadora!")

def q2():
    n=0
    areas=[]
    while n<5:
        l=float(input("Lado do quadrado: "))
        if l<0:
            print("Não são aceitos valores negativos!")
            continue
        print(f"Área: {l*l}")
        areas.append(l)
        n=n+1
    print(f"O maior quadrado foi o de área {max(areas)})")

def q3():
    n=0
    while n<10:
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
        n=n+1

def q4():
    n=0
    while n<10:
        n1=float(input(f"Nota 1 do aluno {n+1}: "))
        n2=float(input(f"Nota 2 do aluno {n+1}: "))
        if (n1+n2)/2>=7:
            print(f"Aluno {n+1} aprovado!")
        else:
            print(f"Aluno {n+1} reprovado!")
        n=n+1

def q5():
    sn="s"
    numeros=[]
    while sn=="s":
        numero=float(input("Número: "))
        numeros.append(numero)
        sn=input("Deseja escrever outro número? (s): ")
        if sn!="s":
            break
    print(f"Média: {sum(numeros)/len(numeros)}")

def q6():
    n=1
    while n<=5:
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
        n=n+1

def q7():
    sn="s"
    while sn=="s":
        anos=int(input("Anos: "))
        cpd=int(input("Cigarros por dia: "))
        pcc=float(input("Preço de carteira com 20 cigarros: "))
        cpa=(anos*365)*cpd
        print("Você gastou R${} com cigarros".format((cpa*pcc)/20))
        sn=input("Deseja calcular denovo? (s): ")
        if sn!="s":
            break
    print("Obrigado por usar nossa calculadora!")

def q8():
    sn="s"
    while sn=="s":
        n=input("Nome: ")
        i=int(input("Idade: "))
        if i>=50:
            p="está perto de se aposentar."
        else:
            p="não está perto de se aposentar."
        print("Seu nome é {} e você tem {} anos. Além disso, você {}".format(n,i,p))
        sn=input("Deseja calcular denovo? (s): ")
        if sn!="s":
            break
    print("Obrigado!")

def q9():
    n=1
    while n<=30:
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
        n=n+1
    print("Obrigado!")

def q10():
    cc=float(input("Consumo do carro em litros/km: "))
    d= float(input("Distância em km: "))
    if cc<0 or d<0:
        print("Não são permitidos valores negativos!")
        exit()
    print("Litros que serão gastos: {}".format(cc*d))

def q11():
    sn="s"
    while sn=="s":
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
    n=2
    while n<=1000:
        print(n)
        n=n+2

def q13():
    n=1002
    while n<2000:
        print(n)
        n+=1

def q14():
    n=1
    t=int(input("Tabuada do número: "))
    while n<=10:
        print(f"{t} x {n} = {t*n}")
        n+=1

def q15():
    useroriginal="AndersonSuassuna"
    senhaoriginal="suassuna123"
    while useroriginal==senhaoriginal:
        print("Seus dados originais não podem ser iguais! Corrija-os!")
        continue
    user=input("Nome de usuário: ")
    senha=input("Senha: ")
    while user==senha:
        print("O usuário e a senha não podem ser iguais!")
        continue
    if user==useroriginal and senha==senhaoriginal:
        print("Você fez login com sucesso!")
    else:
        print("Seu usuário ou senha estão incorretos!")

def q16():
    sn="s"
    pares=[]
    impares=[]
    while sn=="s":
        n=int(input("Informe o número: "))
        if n%2==0:
            pares.append(n)
        else:
            impares.append(n)
        sn=input("Deseja informar outro número? (s): ")
        if sn!="s":
            break
    print(f"Foram {len(pares)} números pares e {len(impares)} números ímpares.")