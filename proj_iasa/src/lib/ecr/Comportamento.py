from abc import ABC, abstractmethod

"""(Interface) Define a base todos os comportamentos.
"""
class Comportamento(ABC):

    """
    (Método Abstrato) Activa o conportamento e produz uma resposta.
        Define o padrão para todos os comportamentos (simples ou compostos),
        em que o comportamento avalia a informação vinda de percepção e decide a ação executar.
        
        @param percepcao: A perceção do ambiente.
        @return: A ação da avaliação do comportamento.
    """
    @abstractmethod
    def activar(self,percepcao):
        """"""
        