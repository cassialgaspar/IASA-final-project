from pee.melhor_prim.ProcuraInformada import ProcuraInformada  
from pee.melhor_prim.aval.avaliadorSof import AvaliadorSof

"""
(A classe) Representa o mecanismo de Procura Sôfrega, que é um tipo de Procura Informada.
Em vez de explorar o grafo às cegas, utiliza conhecimento do domínio (heurística) para guiar o processo.
A sua regra é que o próximo nó a ser expandido deve ser o que parece estar mais perto do estado objetivo,
ignorando o custo já percorrido.
"""
class ProcuraSof(ProcuraInformada):
    
    """
    (Método) Construtor da Procura Sofrega.
        Inicializa o mecanismo so instanciar 'AvaliadorSof' e passando-o para a superclasse (ProcuraInformada).
        A superclasse faz com que a fronteira de prioridade utilize esse avaliador específico. 
        É a 'AvaliadorSof' que garante que a prioridade dos nós será definida somente pela estimativa de 
        distância até ao objetivo (valor heuristico).
    """
    def __init__(self):
        super().__init__(AvaliadorSof())