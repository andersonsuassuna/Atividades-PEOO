from funcionario import Funcionario
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtd_gerenciaveis):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciaveis = qtd_gerenciaveis
    def get_bonificacao(self):
        return super().get_bonificacao()+1000

# testes
# f1=Gerente("Anderson","70180308467",1000,"anderson123",1)
# f1._salario=f1.get_bonificacao()+f1._salario
# print(f1._salario)