from abc import ABC, abstractmethod

"""
(A interface) Representa o comportamento de controlo do agente inteligente, onde a ação gerada através da perceção do 
ambiente feita pelo agente inteligente é processada. 

    @param ABC (biblioteca Abstract Base Classes) para que a classe seja abstrata.
"""
class Controlo(ABC):

    @abstractmethod
    def processar(self, percepcao):
        """Processar percepção gerando uma ação"""