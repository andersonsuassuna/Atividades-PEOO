from conta import * # Aqui importamos as classes "Conta" e "Cliente" do arquivo "conta.py"
# conta=Conta() # criamos o objeto "conta"
# type(conta) # Aqui vemos o tipo da variável "conta"
# Se rodarmos apenas "Conta()" na linha 2, o programa vai dar erro pois requer 4 argumentos. Agora, fazendo certo:

data=date.today()

conta = Conta('123-4', 'João', 120.0, 1000.0,data) # Criamos o objeto com os atributos
print(conta.numero) # imprimimos o número da conta
print(conta.titular) # imprimimos o titular da conta
conta1=Conta("444-4", "Anderson", 500, 2000,data) # Criei a conta 1
conta2=Conta("222-2", "Inácio", 1000, 3000,data) # Criei a conta 2

# Testando métodos
conta1.deposita(100)
conta1.extrato()
conta1.saca(50)
conta1.extrato

Anderson=Cliente("Anderson","Suassuna",70180308467) # Questão 15: criei um cliente e relacionei ele com o titular da conta
conta1.titular=Anderson
Anderson.dados()

print(conta1.abertura) # Questão 16: mostra a data de abertura da conta