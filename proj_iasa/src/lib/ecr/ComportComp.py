from abc import ABC, abstractmethod
from ecr.Comportamento import Comportamento

class ComportComp(Comportamento, ABC):

    """(A classe) Representa um comportamento composto, com múltiplos comportamentos mais simples.
        É uma classe abstrata que herda de Comportamento e de ABC.
        """
    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos


    """(Método) com comportamento composto que itera sobre todos os comportamentos, ativando cada um com a sua perceção atualizada.
        As ações diferentes de None são guardadas numa lista.
        
        @param percepcao: instância da perceção atual do ambiente,  que alimenta os varios comportamentos internos.
        @return: instância da Accao final escolhida (após seleção), ou None se nenhum comportamento gerar ação.
    """
    def activar(self, percepcao):
        
        accoes = []
        for comportamento in self.__comportamentos:

            accao = comportamento.activar(percepcao)

            if accao:
                accoes.append(accao)

            if accoes:
                accao = self.seleccionar_accao(accoes)
            
        return accao


    @abstractmethod
    def seleccionar_accao(accoes):
        """ """

