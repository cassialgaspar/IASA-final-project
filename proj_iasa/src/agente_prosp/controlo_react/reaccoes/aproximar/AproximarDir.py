from ecr.Reaccao import Reaccao
from agente_prosp.controlo_react.reaccoes.aproximar.EstimuloAlvo import EstimuloAlvo
from agente_prosp.controlo_react.reaccoes.aproximar.RespostaMover import RespostaMover  

"""
(A classe) Representa uma reação simples para aproximar o agente de um alvo.
Faz a connecao direta entre o estímulo (detetar um alvo nessa direção) e a resposta (mover nessa direção). 
Várias destas reações (Norte, Sul, Este, Oeste) vão estar em grupos para formar o comportamento  de "AproximarAlvo".
"""
class AproximarDir(Reaccao):
    
    """
    (Método) Construtor da reação de aproximar numa direção.
        @param direcao: Específica que direção do Enum que esta reação vai usar.
        
        Inicializa a classe mãe com EstimuloAlvo para a direção recebida e RespostaMover.
    """
    def __init__(self, direcao):
        super().__init__(EstimuloAlvo(direcao), RespostaMover(direcao))