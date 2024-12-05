# ETAPA 1
class Banco:
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

meu_banco=Banco("Banco Central")
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
# 