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

q16()