from funcionario import Funcionario
class Vendedor(Funcionario):
    def __init__(self, nome, cpf, salario, total_vendas, comissao):
        super().__init__(nome, cpf, salario)
        self._total_vendas = total_vendas
        self._comissao = comissao # Percentual de comissão sobre as vendas
    def get_bonificacao(self):
        return (self._salario*0.1)+(self._total_vendas*(self._comissao/100))

# testes
# v1=Vendedor("Anderson","70180308467",1000,100,100)
# v1._salario=v1.get_bonificacao()+v1._salario
# print(v1._salario)