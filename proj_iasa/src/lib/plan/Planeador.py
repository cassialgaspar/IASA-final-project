from abc import ABC, abstractmethod

"""(Interface) Define o contrato obrigatório para o plano de ação a ser implementado"""
class Planeador(ABC):

    """(Método Abstracto) Define a assinatura obrigatória para o processo de planeamento."""
    @abstractmethod
    def planear(self, modelo_plan, objetivos):
        """Returns a Plano"""