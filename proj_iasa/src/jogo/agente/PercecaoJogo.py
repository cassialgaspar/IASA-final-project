from agente.Percecao import Percecao 

"""
(A classe) Representa uma ação no ambiente do jogo. Implementa a interface Percecao.
"""
class PercecaoJogo(Percecao):
    """Classe que representa a perceção do ambiente do jogo"""
    def __init__(self, evento):
        self.__evento = evento

    @property
    def evento(self):
        """Retorna o evento do jogo"""
        return self.__evento  #privado para evitar que houvessem duas entradas de eventos (distinguir entrada de eventos do jogo e entrada de eventos do agente inteligente)

