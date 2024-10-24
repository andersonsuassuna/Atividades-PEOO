class Conta: # Aqui criamos a classe "Conta"
    def __init__(self, numero, titular, saldo, limite): # Usamos o método construtor com atributos para dar esses atributos ao objeto
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def deposita(self, valor): # Serve para depositar um valor dado na conta destinada. o "self" é usado para localizar o próprio objeto
        self.saldo += valor

    # def saca(self, valor): # Saca (retira) um valor dado da conta dada. Se fizermos assim, há a possibilidade de sacar mais do que se tem na conta, o que não pode ser possível.
    #    self.saldo -= valor

    def extrato(self): # Mostra o número e o saldo da conta
        print("numero: {} \nsaldo: {}".format(self.numero, self.saldo))

    def saca(self, valor): # Dessa forma, o valor a ser sacado não ultrapassa o valor que está dentro da conta
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
        return True

    def transfere_para(self, destino, valor): # Essa função transfere um valor dado de uma conta para outra. Veja que as contas envolvidas são dadas nos parâmetros
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True

class Cliente: # Questão 15: criei a classe "Cliente" e adicionei os dados
    def __init__(self,nome,sobrenome,cpf):
        self.nome=nome
        self.sobrenome=sobrenome
        self.cpf=cpf
    
    def dados(self): # Função para mostrar os dados de uma conta
        print(f"Nome: {self.nome}\nSobrenome: {self.sobrenome}\nCPF: {self.cpf}")