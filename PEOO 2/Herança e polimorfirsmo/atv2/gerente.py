from funcionario import Funcionario
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_gerenciaveis):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciaveis = qtd_gerenciaveis
    def get_bonificacao(self):
        """
        Implementar:
        Deve retornar a bonificação do salário (10%) + 1000 reais.
        Utilize super() para chamar o método da classe base.
        """
        pass