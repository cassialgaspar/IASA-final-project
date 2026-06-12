from ecr.Prioridade import Prioridade
from sae import Direccao
from agente_prosp.controlo_react.reaccoes.aproximar.AproximarDir import AproximarDir

"""

(Classe) Representa o comportamento de aproximar-se um alvo específico, para tal necessita de 
estimulos (deteta algo), e a resposta (aproximar-se).
Como a prioridade depende da distancia ao alvo, há selecao, por isso estende a classe Prioridade.
"""
class AproximarAlvo(Prioridade):
    def __init__(self):
        super().__init__([AproximarDir(direcao) for direcao in Direccao]) #cria todas as direcoes em que o agente se pode aproximar do alvo

