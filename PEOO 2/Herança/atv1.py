class Item:
    all_items=[]
    def __init__(self,nome,quantidade):
        self.nome=nome
        self.quantidade=quantidade
        Item.all_items.append(self)
    
    def __str__(self):
        return(f"Nome:{self.nome} Quantidade:{self.quantidade}")

class Equipamento(Item):
    def detalhes_manutencao(self):
        return("O equipamento precisa de manutenção anual")

class Consumivel(Item):
    def verificar_validade(self):
        return("O Item é consumível")

item1 = Equipamento("Notebook", 10)
item2 = Equipamento("Impressora", 5)
item3 = Consumivel("Caneta", 100)
item4 = Consumivel("Papel A4", 500)

print("Itens no inventário:")
for item in Item.all_items:
    print(item)

print("\nChamando métodos específicos:")
print(item1.detalhes_manutencao())
print(item2.detalhes_manutencao())
print(item3.verificar_validade())
print(item4.verificar_validade())