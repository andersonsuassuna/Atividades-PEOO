from funcionario import *
class ControleDeBonificacoes:
    def __init__(self):
        self.__total_bonificacoes = 0
    def registra(self, funcionario):
        self.__total_bonificacoes=self.__total_bonificacoes+funcionario.get_bonificacao()
    def total_bonificacoes(self):
        return self.__total_bonificacoes

# testes
# f1=Funcionario("Anderson","70180308467",1500)
# cdb=ControleDeBonificacoes()
# cdb.registra(f1)
# print(cdb.total_bonificacoes())