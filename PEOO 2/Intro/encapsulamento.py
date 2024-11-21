class Classe:
    def __init__(self,at1,at2):
        self.__at1=at1 # Com dois underline (__) tornamos um atributo privado
        self.__at2=at2 # Eles só podem ser acessados indiretamente, ou seja, por um método externo
        
    # Geralmente usamos métodos "set" e "get" para acessar esses atributos privados
    def get_at1(self):
        return self.__at1
    
    def set_at2(self,at2):
        self.__at2=at2