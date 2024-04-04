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
    