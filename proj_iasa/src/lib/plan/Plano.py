from abc import ABC, abstractmethod

"""(Interface) Representa um plano, ou seja, uma sequência de acções a executar para atingir um objectivo (solução) """
class Plano(ABC):

    """(Método Abstrato) Verifica a próxima ação a executar de acordo com a situação atual."""
    @abstractmethod
    def obter_accao(self, estado):
        """Returns an Operador"""
    
    """(Método Abstrato) Obriga o plano a ter uma representação visual."""
    @abstractmethod
    def mostrar(self, vista):
        """ vista is a VistaAmb"""