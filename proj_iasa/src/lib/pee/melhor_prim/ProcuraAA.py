from pee.melhor_prim.ProcuraInformada import ProcuraInformada
from pee.melhor_prim.aval.avaliadorAA import AvaliadorAA

"""
(A classe) Representa o mecanismo de Procura AA .
Esta usa à semelhança da ProcuraSof uma estratégia de Procura Informada, mas pelo contrário dela, avalia o "mérito" 
de um nó ao combinar o custo real percorrido até ao momento com a estimativa heurística do custo restante até ao objetivo.
"""
class ProcuraAA(ProcuraInformada):
    
    """
    (Método) Inicializa o mecanismo instanciando um 'AvaliadorAA' e passando-o para a superclasse (ProcuraInformada).
        Este avaliador determina a ordem dos nós abertos, minimizando a soma do custo acumulado com o valor heurístico.
    """
    def __init__(self):
        super().__init__(AvaliadorAA())