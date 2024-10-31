class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura
    
    def envelhecer(self,anos):
        if anos<=0:
            print("Coloque uma quantidade de anos maior que 0!")
        else:
            self.idade+=anos

    def rejuvenecer(self,anos):
        if anos>self.idade:
            print("Coloque uma quantidade de anos menor do que sua idade!")
        else:
            self.idade-=anos
    
    def engordar(self,kg):
        if kg<0:
            print("Coloque uma quantidade de kilos maior que 0!")
        else:
            self.peso+=kg
    
    def emagrecer(self,kg):
        if kg>self.peso:
            print("Coloque uma quantidade de kilos menor do que seu peso!")
        else:
            self.peso-=kg
    
    def crescer(self,cm):
        if cm<0:
            print("Coloque uma quantidade de cm maior que 0!")
        else:
            self.altura+=cm
    
    def diminuir(self,cm):
        if cm>self.altura:
            print("Coloque uma quantidade de cm menor do que sua altura!")
        else:
            self.altura-=cm

pessoa1=Pessoa("Anderson",17,60,178)
pessoa1.crescer(22)
print(pessoa1.altura)
pessoa1.emagrecer(10)
print(pessoa1.peso)
pessoa1.envelhecer(13)
print(pessoa1.idade)