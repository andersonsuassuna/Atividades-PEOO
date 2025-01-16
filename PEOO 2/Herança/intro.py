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
    
    def __str__(self):
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