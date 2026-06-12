#herda de acao e movimento

from ecr.Accao import Accao
from sae import Movimento



class Avancar(Movimento, Accao):

    def __init__(self):
        
        super().__init__(None) #por default avança 1 unidade

