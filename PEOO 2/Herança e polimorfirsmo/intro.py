# Usamos a herança para passar tudo de uma classe para outra. É basicamente fazer uma cópia
class ContactList(list):
    def search(self,name):
        results=[]
        for contact in self:
            if name in contact.name:
                results.append(contact)
        return(results)


class Contact:
    all_contacts=ContactList() # variável de classe

    def __init__(self,name,email):
        self.name=name
        self.email=email
        Contact.all_contacts.append(self)
    
    def __str__(self): # configurar print de uma classe
        return(f"{self.name} {self.email}")

class Supplier(Contact):
    def order(self,pedido):
        print(f"Pedido para {self.name}: {pedido}")

c1=Contact("Anderson", "andersonssgf7@gmail.com")
f1=Supplier("Amazon", "amazon@gmail.com")
print(c1.name,c1.email)
print(f1.name,f1.email)

f1.order("Camisa do Liverpool")
#c1.order("Camisa do Flamengo")

c2=Contact("Inácio","inacio@gmail.com")
c3=Contact("Gustavo","gustavo@gmail.com")

Contact.all_contacts.search("Anderson")
print(c3)

# Super
# O Super é usado para herdar os atributos da classe pai. Observe:

class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone=phone

friend1=Friend("MaisLuan","maisluan@gmail.com", "40028922")
friend1.phone

class Funcionario:
    def _init_(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
    def get_bonificacao(self):
        return self.salario * 0.1

class Gerente(Funcionario):
    def _init_(self, nome, cpf, salario, senha, qtd_gerenciaveis): 
        super().__init_(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciaveis = qtd_gerenciaveis
        def get_bonificacao():
            return super().get_bonificacao() + 1000

