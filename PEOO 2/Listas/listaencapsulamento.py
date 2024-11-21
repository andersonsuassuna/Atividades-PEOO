class BombaCombustivel:
    def __init__(self,tipoCombustivel,valorLitro,quantidadeCombustivel):
        self.__tipoCombustivel=tipoCombustivel
        self.__valorLitro=valorLitro
        self.__quantidadeCombustivel=quantidadeCombustivel

    def abastecerPorValor(self,valor):
        if valor/self.__valorLitro<=self.__quantidadeCombustivel:
            print(f"Quantidade abastecida: {valor/self.__valorLitro} litros.")
            self.__quantidadeCombustivel-=valor/self.__valorLitro
        else:
            print(f"A bomba não possui essa quantidade de combustível! Ela só tem {self.__quantidadeCombustivel} litros!")
    
    def abastecerPorLitro(self,litro):
        if litro<=self.__quantidadeCombustivel:
            print(f"Preço a pagar: R${litro*self.__valorLitro}")
            self.__quantidadeCombustivel-=litro
        else:
            print(f"A bomba não possui essa quantidade de combustível! Ela só tem {self.__quantidadeCombustivel} litros!")
    
    def alterarValor(self,valor):
        self.__valorLitro=valor

    def alterarCombustivel(self,combustivel):
        self.__tipoCombustivel=combustivel

    def alterarQuantidadeCombustivel(self,quantidade):
        self.__quantidadeCombustivel=quantidade
    
    def get_tipoCombustivel(self):
        return self.__tipoCombustivel

class Veiculo:
    def __init__(self,litrosnotanque,limite,combustivel):
        self.litrosnotanque=litrosnotanque
        self.limite=limite
        self.combustivel=combustivel
        

bomba=BombaCombustivel("Gasolina",5,100)
bomba.alterarCombustivel("Alcool")
print(bomba.get_tipoCombustivel())