from ecr.Comportamento import Comportamento
from agente_prosp.accoes.Rodar import Rodar
from agente_prosp.accoes.Avancar import Avancar
from sae import Direccao

import random

"""
se o criterio for especifico usa-se, caso contrário é aleatório.
O agente, neste caso, avança espera, roda  e volta a avançar aleatoriamente, ou seja, o comportamento é aleatório.
"""
class Explorar(Comportamento):
    def __init__(self,prob_rotacao = 0.7):
        self.__prob_rotacao = prob_rotacao


    """
    (Método) roda aleatoriamente ou avança, dependendo do valor de um número gerado aleatóriamente 
    comparado com a probabliddade de rotação definida nos parametros do construtuor.
    Para calcular a direção é utilizado o random.choice() no Enum Direccao (Norte, Sul, Este, Oeste).
        @param percecao: não é utilizado neste comportamento, mas é necessário pois foi implementado na classe mãe.
        @return: acção a ser executada pelo agente(Rodar ou Avançar).
    """
    def activar(self, percecao):
        
        aleatorio = random.random()

        if aleatorio < self.__prob_rotacao:
            accao = Rodar(random.choice(list(Direccao)))
        
        else: 
            accao = Avancar()
        return accao