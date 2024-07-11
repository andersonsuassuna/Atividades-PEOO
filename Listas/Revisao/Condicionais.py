def q1():
    valorantigo=float(input("Qual o valor do produto? "))
    cat=input("Qual sua categoria de cliente? ")
    cat=cat.upper()
    if cat=="A":
        desconto=1/10
    elif cat=="B":
        desconto=15/100
    elif cat=="C":
        desconto=2/10
    else:
        print("Digite uma categoria válida!")
        exit()
    valorfinal=valorantigo-(valorantigo*desconto)
    if valorfinal>500:
        valorfinal=valorfinal-(valorfinal*(5/100))
    print(f"O valor final é R${valorfinal}")

def q2():
    salarioanual=float(input("Qual o seu salário anual? "))
    if 0<=salarioanual<=20000:
        aliquota=5/100
    elif 20000<salarioanual<=50000:
        aliquota=1/10
    elif salarioanual>50000:
        aliquota=2/10
    else:
        print("Digite um valor válido!")
        exit()
    salariofinal=salarioanual-(salarioanual*aliquota)
    if salariofinal>30000:
        salariofinal=salariofinal-2000
    print(f"Seu salário final é de {salariofinal}")

def q3(): #tem resultado para todas as possibilidades
    idade=int(input("Sua idade: "))
    tempo=int(input("Tempo de contribuição em anos: "))
    if idade>=65 and tempo >=30:
        print("Pode se aposentar!")    
    if idade>=65 and tempo <30:
        print(f"Ainda faltam {30-tempo} anos de serviço para você poder se aposentar!")   
    if idade<65 and tempo >=30:
        print(f"Ainda faltam {65-idade} anos de idade para você poder se aposentar!")   
    if idade<65 and tempo <30:
        print(f"Ainda faltam {65-idade} anos de idade e {30-tempo} anos de serviço para você poder se aposentar!") 

def q4(): #tem resultado para todas as possibilidades
    salario=float(input("Salário: "))
    emprestimo=float(input("Empréstimo: "))
    parcelas=int(input("Parcelas: "))
    if emprestimo<salario*10 and emprestimo/parcelas<=salario*3/10:
        print("Empréstimo aprovado!")
    if emprestimo>salario*10 and emprestimo/parcelas<=salario*3/10:
        print("Empréstimo reprovado! O valor do empréstimo excede 10x o valor do salário!")
    if emprestimo<salario*10 and emprestimo/parcelas>salario*3/10:
        print("Empréstimo reprovado! O valor de uma parcela é maior que 30% do salário!")
    if emprestimo>salario*10 and emprestimo/parcelas>salario*3/10:
        print("Empréstimo reprovado! O valor do empréstimo excede 10x o valor do salário e o valor de uma parcela é maior que 30% do salário!")

def q5():
    data=input("Data (xx/xx/xxxx): ")
    if 0<(int(data[0:2]))<=31:
        if 0<(int(data[3:5]))<=12:
            if 0<(int(data[6:10])):
                print("Data Válida!")
            else:
                print("Ano inválido!")
        else:
            print("Mês inválido!")
    else:
        print("Dia inválido!")
    print(data[0:2])
    print(data[3:5])
    print(data[6:10])
q5()