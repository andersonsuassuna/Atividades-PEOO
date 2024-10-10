class Conta:
    def __init__(self,numero,titular,saldo,limite,poupanca):
        self.numero=numero
        self.titular=titular
        self.saldo=saldo
        self.limite=limite
        self.poupanca=poupanca
    
    def colocarnapoupanca(self,valor):
        self.poupanca+=valor
        self.saldo-=valor

    def deposita(self,valor):
        self.saldo+=valor
    
    def saca(self,valor):
        if self.saldo>=valor:
            return True
        else:
            return False
    
    def extrato(self):
        print(f"{self.numero}\n{self.saldo}")

conta1=Conta(input("Número da conta 1: "),input("Titular da conta 1: "),int(input("Saldo da conta 1: ")),int(input("Limite da conta 1: ")),int(input("Poupança da conta 1: ")))
conta2=Conta(input("Número da conta 2: "),input("Titular da conta 2: "),int(input("Saldo da conta 2: ")),int(input("Limite da conta 2: ")),int(input("Poupança da conta 2: ")))

def transferir(a,valor,b):
        a.saldo-=valor
        b.saldo+=valor

transferir(conta1,100,conta2)
conta1.colocarnapoupanca(100)
print(conta1.saldo)
print(conta2.saldo)