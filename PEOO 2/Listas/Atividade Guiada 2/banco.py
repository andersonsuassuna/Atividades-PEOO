# ETAPA 1
class Banco:
    __slots__ = ['__nome']
    __total_bancos=0

    def __init__(self,nome):
        self.__nome=nome
        Banco.__total_bancos+=1
    
    def get_total_bancos():
        return Banco.__total_bancos
    # ou
    # @classmethod
    # def get_total_bancos(cls):
    #     return cls.__total_bancos # O classmethod é usado para se referir à classe que está sendo acessada

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) >= 3:
            self.__nome = novo_nome
        else:
            print("Nome inválido. Deve ter pelo menos 3 caracteres.")
    
    @classmethod
    def reset_total_bancos(cls):
        cls.__total_bancos = 0

meu_banco=Banco("Banco Central")
Banco.reset_total_bancos()
# print(meu_banco.__nome) # Não é possível acessá-lo, pois o protegemos. Isso é usado para evitar mudanças no próprio.
# Os dois underscores servem para o python reescrever o nome do atributo para evitar conflitos

# ETAPA 2
# print(meu_banco.get_nome())
# Agora podemos acessá-lo pois não é diretamente. Estamos usando um return
# Para eles ainda poderem ser usados

# ETAPA 3
# meu_banco.set_nome("Banco Nacional")
# print(meu_banco.get_nome())
# Pois assim como no get, não estamos acessando-o diretamente, mas por meio de uma função
# são usados para acessar e modificar os atributos de uma classe de maneira controlada

# ETAPA 4
# meu_banco.set_nome("BB")
# print(meu_banco.get_nome())
# É importante para termos certeza do que estamos alterando
# Serve para não haver conflitos entre atributos

# ETAPA 5
print(meu_banco.nome)
meu_banco.nome="BNB"
print(meu_banco.nome)
# Reduz o uso de funções, tornando possível acessar atributos privados como se fossem públicos
# Além de reduzir o uso de funções, torna o código muito mais fácil de compreender e trabalhar nele. Tudo isso ainda preservando a privacidade do atributo

# ETAPA 6
banco1 = Banco("Banco A")
banco2 = Banco("Banco B")
banco3 = Banco("Banco C")

print(Banco.get_total_bancos())
# Pois estamos alterando um atributo na classe em geral, e não na instância
# Para conseguirmos diferenciar os atributos de cada instância

# ETAPA 7
Banco.reset_total_bancos()
print(Banco.get_total_bancos())
# Em métodos de classe alteramos atributos da classe em geral. Em métodos de instância apenas alteramos atributos da instância
# Quando queremos contabilizar instâncias, como usamos nesse código, por exemplo

# ETAPA 8
# meu_banco.endereco = "Rua Principal, 123"
# O __slots__ reduz o uso de memória reservando um dicionário para instâncias. Isso faz com que não sejam criados diversos dicionários
# Em códigos grandes o uso dele pode diminuir consideravelmente a memória gasta

# ETAPA 9
class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) >= 3:
            self.__nome = novo_nome
        else:
            print("Nome inválido.")

    @property
    def cpf(self):
        return self.__cpf

class Conta:
    __total_contas=0
    def __init__(self, numero, titular):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = 0
        Conta.__total_contas+=1
    
    @property
    def saldo(self):
        return self.__saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido para depósito.")
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente ou valor inválido.")
    
    @classmethod
    def total_contas(cls):
        return cls.__total_contas

cliente1 = Cliente("Anderson", "701.803.084-67")
conta1 = Conta("4444-44", cliente1)
conta1.depositar(1000)
print(f"Saldo atual: R$ {conta1.saldo}")
conta1.sacar(500)
print(f"Saldo após saque: R$ {conta1.saldo}")
print(Conta.total_contas())
conta2 = Conta("1313-13", cliente1)
print(f"Total de contas criadas: {Conta.total_contas()}")
# Eles se complementam, deixando o código mais leve e simples de se trabalhar