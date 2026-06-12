from abc import ABC, abstractmethod

"""(Interface) Representa o modelo de plano """
class ModeloPlano(ABC):
    """Procura o estado atual """
    @abstractmethod 
    def obter_estado(self):
        """Returns an Estado"""
    
    """ Procura a totalidade do espaço de estados conhecido, de modo a que planeador conheça as soluções possíveis para o problema"""
    @abstractmethod
    def obter_estados(self):
        """Returns a list of Estados"""

    @abstractmethod
    def obter_operadores(self):
        """Returns a list of Operadores"""
        