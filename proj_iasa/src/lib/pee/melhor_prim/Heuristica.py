from abc import ABC, abstractmethod

"""
(Interface) Torna possivel fazer uma estimativa da solução de um problema para guiar qual poderá ser a melhor resolução, 
no entanto pode não corresponder exatamente ao valor real. Depende apenas do estado atual, e não de como se chegou a este estado.
A heuristica corresponde ao custo da solução, e só é utilizada caso não existam restrições no problema.
"""
class Heuristica(ABC):
    @abstractmethod
    def h(self, estado):
        """retorna o custo do estado"""