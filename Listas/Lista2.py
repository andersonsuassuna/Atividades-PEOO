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
    print(f"O maior quadrado foi o de área {l*l} (lado {l})")

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
q4()