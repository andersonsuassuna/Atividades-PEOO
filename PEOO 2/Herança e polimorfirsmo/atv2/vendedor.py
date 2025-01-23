from funcionario import Funcionario
class Vendedor(Funcionario):
    def __init__(self, nome, cpf, salario, total_vendas, comissao):
        super().__init__(nome, cpf, salario)
        self._total_vendas = total_vendas
        self._comissao = comissao # Percentual de comissão sobre as vendas
    def get_bonificacao(self):
        """
        Implementar:
        Deve retornar a bonificação baseada no salário (10%) + comissão sobre as vendas.
        Exemplo: self._total_vendas * (self._comissao / 100)
        """
        pass