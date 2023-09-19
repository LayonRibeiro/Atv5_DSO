from abc import ABC, abstractmethod
from animal import Animal

class Mamifero(Animal, ABC):
    @abstractmethod
    def __init__(self, volume_do_som: int, tamanho_passo:int):
        super().__init__(tamanho_passo)
        self.__volume_do_som = volume_do_som
    
    @property
    def volume_do_som(self):
        return self.__volume_do_som
    
    @volume_do_som.setter
    def volume_do_som(self, volume_do_som):
        self.__volume_do_som = volume_do_som
    
    def mover(self):
        return super().mover()
    
    def produzir_som(self):
        return "MAMIFERO:" + super().produzir_som() + str(self.__volume_do_som)