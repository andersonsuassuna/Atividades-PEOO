class Pato:
    def grasna(self):
        print("quack!")

class Ganso:
    def grasna(self):
        print("quack!")

pato=Pato()
ganso=Ganso()

# É util pra realizar vários métodos iguais
for bixo in [pato,ganso]:
    bixo.grasna()

# Conceito "interface" e classes abstratas
import abc
class Pato(abc.ABC):
    @abc.abstractclassmethod
    def grasna(self):
        pass
