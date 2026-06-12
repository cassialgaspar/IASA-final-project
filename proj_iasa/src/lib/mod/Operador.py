from abc import ABC, abstractmethod

""" (A interface) Representa as várias ações que produzem a mudança de uma configuração do problema para outra
No espaço de estados, a aplicação de um operador faz uma transição de estado, que cria estados sucessores para a procura """
class Operador(ABC): # interface

    """
    (Método abstrato) Aplica o operador a um estado, que gera uma transição para um novo estado
        @param estado: O estado atual onde o operador vai ser aplicado.
        @return: O novo estado gerado.
    """
    @abstractmethod
    def aplicar(self, estado):
        """"""

    """
    (Método abstrato) Função de custo de transição de estado.
        @param estado: O estado atual (de origem).
        @param estado_suc: O estado sucessor (destino) gerado pela aplicação do operador.
        @return: O valor do custo da transição (retorna um double / float).
    """
    @abstractmethod
    def custo(self, estado, estado_suc):
        """ """