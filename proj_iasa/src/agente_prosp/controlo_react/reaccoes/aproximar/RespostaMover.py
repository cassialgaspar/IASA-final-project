from ecr.Resposta import Resposta
from agente_prosp.accoes.Mover import Mover


"""
(Classe) A resposta de o agente se mexer para uma direção.
"""
class RespostaMover(Resposta):
    def __init__(self, direccao = None):
        super().__init__(Mover(direccao))
        
