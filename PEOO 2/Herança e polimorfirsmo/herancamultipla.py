# Basicamente usamos a herança para criar uma árvore de heranças maiores
# EXERCÍCIO 1 --------------------------------------------
class A:
    def metodo(self):
        print("Método de A")
    def metodo3(self):
        print("Método 3 de A")
class B(A):
    def metodo(self):
        print("Método de B")
    def metododeb(self):
        print("Método exclusivo de BBBBB")

class C(A):
    def metodo(self):
        print("Método de C")
    def metodo2(self):
        print("Método 2 de C")
    def metododec(self):
        print("Método exclusivo de CCCCC")

class D(B,C): # Vai herdar de B e C, mas os métodos que tiverem o mesmo nome serão herdados de B, pois é a classe mais à esquerda nos parêntesis.
    def metododed(self):
        super().metododec()
        print("Método de D que puxou o método exclusivo de C")
    def metodo(self):
        print("'metodo' de d")

d=D()
d.metodo()
d.metodo2()
d.metodo3() # Consegue usar os métodos do "avô"
d.metododed()
print(D.__mro__) # Mostra a ordem que as classes serão acessadas

# EXERCÍCIO 2 --------------------------------------------
from abc import ABC, abstractmethod
# Interface de atacante
class Atacante(ABC):
    @abstractmethod
    def chutar_ao_gol(self):
        pass

# Interface de defensor
class Defensor(ABC):
    @abstractmethod
    def bloquear_chute(self):
        pass

# Interface de meio-campista
class MeioCampista(ABC):
    @abstractmethod
    def dar_assistencia(self):
        pass

class Jogador1(Atacante, MeioCampista):
    def chutar_ao_gol(self):
        print("Jogador1 chutou forte no gol!")

    def dar_assistencia(self):
        print("Jogador1 deu uma bela assistência!")

class Jogador2(Defensor, MeioCampista):
    def bloquear_chute(self):
        print("Jogador2 bloqueou o chute!")

    def dar_assistencia(self):
        print("Jogador2 fez um passe incrível!")

j1 = Jogador1()
j1.chutar_ao_gol()
j1.dar_assistencia()

j2 = Jogador2()
j2.bloquear_chute()
j2.dar_assistencia()

class Goleiro(ABC):
    @abstractmethod
    def defender_penalti(self):
        print("O GOLEIRO DEFENDEU UM PÊNALTI!")

class Jogador3(Goleiro,Defensor):
    def defender_penalti(self):
        return super().defender_penalti()
    def bloquear_chute(self):
        print("O goleiro bloqueou o chute!!!")

j3=Jogador3()
j3.defender_penalti()
j3.bloquear_chute()

# EXERCÍCIO 3 --------------------------------------------
# Mixins são classes que são herdadas com métodos para não precisar criar mil instâncias e tal
import json

class LogMixin:
    def log(self, mensagem):
        print(f"LOG: {mensagem}")

class NotificacaoMixin:
    def enviar_notificacao(self, usuario, mensagem):
        print(f"Enviando notificação para {usuario}: {mensagem}")

class SerializacaoMixin:
    def salvar_como_json(self, dados, arquivo="dados.json"):
        with open(arquivo, "w") as f:
            json.dump(dados, f)
        print(f"Dados salvos em {arquivo}")

class AutenticacaoMixin:
    def verificar_senha(self,senha,entrada):
        if entrada==senha:
            print("Senha verificada!")
        else:
            print("Senha incorreta!")

class Usuario(LogMixin, NotificacaoMixin, SerializacaoMixin, AutenticacaoMixin):
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.log(f"Usuário {self.nome} criado.")

    def salvar_dados(self):
        dados = {"nome": self.nome, "email": self.email}
        self.salvar_como_json(dados)
    
    def autenticar(self):
        self.verificar_senha(self.senha, "anderson123")

usuario = Usuario("Anderson", "galego@email.com", "anderson123")
usuario.enviar_notificacao("Suassuna", "Bem-vindo ao sistema!")
usuario.salvar_dados()
usuario.autenticar()

# DESAFIO FINAL --------------------------------------------
class Veiculo:
    def mover(self):
        print("o veículo se moveu")

class Motorizado:
    def ligar_motor(self):
        print("motor ligado")

class Eletrico:
    def carregar_bateria(self):
        print("bateria carregada")

class Carro(Veiculo,Motorizado):
    pass

class CarroEletrico(Veiculo,Eletrico):
    pass

class Bicicleta(Veiculo):
    pass

tesla=CarroEletrico()
# tesla.ligar_motor() # dá erro pois Tesla não faz parte de "motorizado"
tesla.carregar_bateria()
tesla.mover()

bike=Bicicleta()
bike.mover()

# DE ÊNDI --------------------------------------------