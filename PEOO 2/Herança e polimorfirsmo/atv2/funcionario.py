class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    def get_bonificacao(self):
        return self._salario*0.1
        

# testes
# f1=Funcionario("Anderson","70180308467",1000)
# f1._salario=f1.get_bonificacao()+f1._salario