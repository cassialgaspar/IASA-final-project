from abc import ABC, abstractmethod

'''
(Inteface) Representa a condição que vai ativar uma reacção.
'''
class Estimulo(ABC):

    @abstractmethod
    def detectar(self, percepcao):
        """Deteta um estímulo"""
