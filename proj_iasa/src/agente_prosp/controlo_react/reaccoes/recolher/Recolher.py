from ecr.Hierarquia import Hierarquia
from agente_prosp.controlo_react.reaccoes.evitar.EvitarObst import EvitarObst
from agente_prosp.controlo_react.reaccoes.explorar.Explorar import Explorar
from agente_prosp.controlo_react.reaccoes.explorar.ExplorarMem import ExplorarMem
from agente_prosp.controlo_react.reaccoes.aproximar.AproximarAlvo import AproximarAlvo

"""
(A classe) Representa o comportamento composto do agente na tarefa de recolha.
Herda de 'Hierarquia', o que significa que usa vários outros comportamentos organizados em níveis de relevância, 
dando sempre prioridade aos que estão primeiro na lista
"""
class Recolher(Hierarquia):
    
    """
    (Método) Construtor.
        Inicializa a hierarquia com a lista dos comportamentos do agente. 
        A ordem na lista estabelece diretamente as prioridades (do mais importante para o menos importante) segundo o seguinte código:

    """
    def __init__(self):
        super().__init__([
            AproximarAlvo(),
            EvitarObst(),
            ExplorarMem(),
            Explorar()
        ])