from mamifero import Mamifero


class Gato(Mamifero):
    def __init__(self):
        super().__init__(2,2)
    
    def mover(self):
        return super().mover() + self.__tamanho_passo
    
    def miar(self):
        return super().produzir_som() + " SOM: MIAU"
        