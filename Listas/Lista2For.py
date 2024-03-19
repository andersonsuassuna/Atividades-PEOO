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