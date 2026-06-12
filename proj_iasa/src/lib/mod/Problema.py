from abc import ABC, abstractmethod

"""
(A classe) Representa o modelo geral de um problema em PEE.
Sendo uma classe abstrata (herda de ABC), define a base de como qualquer problema é resolvido. 
"""
class Problema(ABC): # abstract class

    """
    (Método) Guarda a configuração inicial do problema e os operadores que permitem as transições dos estados.
        @param estado_inicial: O estado a partir do qual o processo de procura inicia.
        @param operadores: Uma lista de ações que geram novos estados sucessores, quando aplicadas a um estado.
    """
    def __init__(self, estado_inicial, operadores):
        self.estado_inicial = estado_inicial
        self.operadores = operadores

    """
    (Método abstrato) Verifica se um estado corresponde à configuração final que resolve o problema. 
        Sendo um método abstrato, obriga a que qualquer problema que herde desta classe tenha de definir a sua própria regra.
        
        @param estado: O estado atual do problema que queremos avaliar.
        @return: Retorna um booleano (True se o estado for o objetivo, False caso contrário).
    """
    @abstractmethod
    def objectivo(self, estado):
        """ """