# Vamos usar muito o termo "objetos"

# Dividimos em estado e comportamento. Ex.: Estado: nome, peso, etc. ou Comportamento: pagar, sacar, etc.

# Em PEOO usamos objetos para contruir sistemas mais complexos

# 4 Pilares: abstração, encapsulamento, herança e polimorfismo

# Temos classes, que são descrições de objetos. Exemplo:

class Cadeira(): # PRIMEIRA LETRA SEMPRE MAIUSCULA
    modelo="Racing Series" # ATRIBUTOS SEMPRE COM PRIMEIRA LETRA MINÚSCULA
    fabricante="DT3sports"
    peso=28
    carga=180
    preco=2000

# Intância: objeto criado com base em uma classe. Exemplo:
# variavel=Classe()

cadeira_1=Cadeira()
cadeira_1.preco=2500 # Alterando preço

# Métodos: representam os comportamentos de uma classe. É basicamente uma função que representa o comportamento a ser feito com aquele objeto. Exemplo:
class Conta:
    numero="00000-0"
    saldo=0.0

    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

# o argumento self é obrigatório. Ele é uma referência ao objeto.

# Método contrutor: determina ações logo ao criar o objeto. Ele é acionado pela função __init__ dentro da classe Exemplo:

class Conta:
    numero="00000-0"
    saldo=0.0

    def __init__(self,numero,saldo):
        self.numero=numero
        self.saldo=saldo

    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

conta1=Conta("00000-0", 0)
print(conta1.numero)
print(conta1.saldo)