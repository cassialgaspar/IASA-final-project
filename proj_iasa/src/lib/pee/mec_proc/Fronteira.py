from abc import ABC, abstractmethod

"""
(A classe) Existem vários tipos de fronteiras, e o que as distingue é a ordem pela qual 
os nós são inseridos. Por isso, esta classe serve como base (superclasse) e vai ser especializada 
mais à frente pelos diferentes métodos de procura (ex: LIFO, FIFO). A sua função geral 
é memorizar e gerir os nós gerados mas que ainda estão por expandir.
"""
class Fronteira(ABC):

    """
    (Método) Inicia apenas o método para iniciar as estruturas internas.
    """
    def __init__(self):
        self.iniciar()

    """
    (Método) Garante que a fronteira fica sem nós, ao criar uma lista vazia.
    """
    def iniciar(self):
        self._nos = [] # cria uma lista vazia de nós

    """
    (Método abstrato) A forma exata como o nó é inserido dependerá da do tipo de fronteira (ex: inserir no início ou no fim).
        @param no: O nó a ser inserido na fronteira.
    """
    @abstractmethod
    def inserir(self, no):
        """"""

    """
    (Método) Remove o primeiro nó da lista e retorna-o.
        @return: O próximo nó a ser expandido.
    """
    def remover(self):
        return self._nos.pop(0)
    
    """ 
    (Propriedade) Serve como verificação para saber se a fronteira está vazia.
        É uma propriedade derivada, porque não guarda um estado próprio, e retorna apenas 
        valores calculados de outros atributos (neste caso, verifica o tamanho da lista _nos).
        @return: Booleano que indica se a fronteira está vazia.
    """
    @property
    def vazia(self):
        return len(self._nos) == 0