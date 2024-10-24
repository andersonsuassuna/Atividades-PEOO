class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura
    
    def envelhecer(self,anos):
        self.idade+=anos

    def rejuvenecer(self,anos):
        self.idade-=anos
    
    def engordar(self,kg):
        self.peso+=kg
    
    def emagrecer(self,kg):
        self.peso-=kg
    
    def crescer(self,cm):
        self.altura+=cm
    
    def diminuir(self,cm):
        self.altura-=cm

pessoa1=Pessoa("Anderson",17,60,178)
pessoa1.crescer(22)
print(pessoa1.altura)
pessoa1.emagrecer(10)
print(pessoa1.peso)
pessoa1.envelhecer(13)
print(pessoa1.idade)