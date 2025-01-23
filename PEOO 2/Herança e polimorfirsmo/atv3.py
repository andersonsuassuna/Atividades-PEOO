# ABSTRAÇÃO
import abc

class Conta:
    def __init__(self, numero, titular,saldo,limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
    
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa

c = Conta("1111","anderson",0,1000)
# Questão "O que ocorre?":
# O site pede para criarmos a instância tendo criado o método "atualiza" abstrato logo depois da classe "Conta" inicial, fazendo ele ignorar a primeira classe criada. Isso é provado com o python printando "Conta() takes no arguments" no terminal.
cc = Conta('123-4', 'João',500,1500)
cp = Conta('123-5', 'José',1000,2000)

cc.atualiza(0.01)
cp.atualiza(0.01)

print(cc._saldo)
print(cp._saldo)

class ContaInvestimento(Conta):
    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo, limite)
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 5

ci = ContaInvestimento('123-6', 'Maria', 1000.0, 3000)
ci.atualiza(0.01)
print(ci._saldo)

# Classe Abstrata
class Conta(abc.ABC):
    @abc.abstractclassmethod
    def atualiza(self):
        pass