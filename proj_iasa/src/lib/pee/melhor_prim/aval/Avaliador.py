from abc import ABC, abstractmethod

"""
(A interface) Representa o contrato para a avaliação da prioridade de um nó e é a peça central dos mecanismos 
de "Procura Melhor-Primeiro". É ela que abstrai a regra de cálculo do prioridade de um nó, 
permitindo que a fronteira de exploração ordene os nós com base na sua prioridade em vez simplemeste por tempo.
"""
class Avaliador(ABC):  
    
    """
    (Método abstrato) Calcula e devolve a prioridade de um dado nó. 
        O valor numérico retornado indica a posição do nó na fronteira com prioridade.
        
        @param no: O nó da árvore de procura cuja prioridade pretendemos calcular.
        @return: Um valor numérico que representa a prioridade do nó.
    """
    @abstractmethod
    def prioridade(self, no):
        """"""