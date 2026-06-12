from ecr.Estimulo import Estimulo
from sae import Elemento


"""(Classe) Representa o estímulo de um alvo
"""

class EstimuloAlvo(Estimulo):
    def __init__(self, direccao, gama=0.9):
        """ """
        self.__direccao = direccao
        self.__gama = gama

    def detectar(self,percepcao):
        elemento, distancia, _ = percepcao[self.__direccao]

        if elemento == Elemento.ALVO:
            intensidade = self.__gama **distancia
        else: 
            intensidade = 0
            
        return intensidade


    """

    outra maneira de fazer o codigo seria:
    return 
    """