from funcionario import Funcionario
from gerente import Gerente
from vendedor import Vendedor
from controledebonificacoes import ControleDeBonificacoes
# Criar os objetos Funcionario, Gerente e Vendedor
funcionario = Funcionario("João", "111111111-11", 2000.0)
# Implemente a criação de um objeto Gerente aqui
# gerente = ...
# Implemente a criação de um objeto Vendedor aqui
# vendedor = ...
# Controle de Bonificações
controle = ControleDeBonificacoes()
# Registre os funcionários no controle
# controle.registra(funcionario)
# controle.registra(gerente)
# controle.registra(vendedor)
# Imprima os valores das bonificações e o total
# print(f"Bonificação Funcionário: {funcionario.get_bonificacao()}")
# print(f"Bonificação Gerente: {gerente.get_bonificacao()}")
# print(f"Bonificação Vendedor: {vendedor.get_bonificacao()}")
# print(f"Total de Bonificações: {controle.total_bonificacoes}")