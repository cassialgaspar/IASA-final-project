import math
from pee.melhor_prim.Heuristica import Heuristica

"""(Classe) Representa a heuristica baseada na distancia em linha reta entre o estado atual e o final. 
    Vai auxiliar a procura para encontrar o estados que parecem ser melhores para alcançar o objetivo.
    Afeta a procura informada no pee pois ordena a fronteira. """
class HeurDist(Heuristica):

    def __init__(self, estado_final):
        self.__estado_final = estado_final

    """(Método) Precisa de saber o estado final para calcular a distancia entre a posição do 
    estado atual e a posição do estado final, com a função math.dist"""
    def h(self, estado):
        return math.dist(estado.posicao, self.__estado_final.posicao)