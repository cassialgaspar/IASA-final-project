from ecr.Accao import Accao
from sae import Movimento


# tendo as duas classes construtor// superClasses, colocamos o movimento primeiro para ser o priorizado
class Mover(Movimento, Accao):

    def __init__(self, direccao):

        super().__init__(direccao, 1)

