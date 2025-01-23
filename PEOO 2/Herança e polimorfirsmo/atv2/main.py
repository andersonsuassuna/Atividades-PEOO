from funcionario import Funcionario
from gerente import Gerente
from vendedor import Vendedor
from controledebonificacoes import ControleDeBonificacoes
# Criar os objetos Funcionario, Gerente e Vendedor
f1=Funcionario("Anderson","70180308467",1500)
g1=Gerente("Demétrios","11111111111",5000,12345,1)
v1=Vendedor("João Neto","22222222222",10000,100,100)
# Controle de Bonificações
controle = ControleDeBonificacoes()
# Registre os funcionários no controle
controle.registra(f1)
controle.registra(g1)
controle.registra(v1)
print(f"Bonificação Funcionário: {f1.get_bonificacao()}")
print(f"Bonificação Gerente: {g1.get_bonificacao()}")
print(f"Bonificação Vendedor: {v1.get_bonificacao()}")
print(f"Total de Bonificações: {controle.total_bonificacoes()}")