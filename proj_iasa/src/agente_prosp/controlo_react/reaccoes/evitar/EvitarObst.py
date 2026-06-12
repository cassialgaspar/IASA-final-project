from ecr.Reaccao import Reaccao
from agente_prosp.controlo_react.reaccoes.evitar.EstimuloObst import EstimuloObst
from agente_prosp.controlo_react.reaccoes.evitar.RespostaEvitar import RespostaEvitar

"""(Classe) Representa o comportamento de evitar um obstáculo

    Reaccao : estende esta classe porque tem um estímulo (detetar um obstáculo) e uma resposta (evitar o obstáculo)
"""
class EvitarObst(Reaccao):
    def __init__(self):

        """EstimuloObst é para detetar o obstáculo e RespostaEvitar é para evitar o obstáculo."""
        super().__init__(EstimuloObst(),RespostaEvitar())  

