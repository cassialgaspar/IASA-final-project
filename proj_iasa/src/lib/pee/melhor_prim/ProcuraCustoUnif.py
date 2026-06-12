from pee.melhor_prim.ProcuraMelhorPrim import ProcuraMelhorPrim
from pee.melhor_prim.aval.avaliadorCustoUnif import AvaliadorCustoUnif

"""
(Classe) Representa o mecanismo de Procura de Custo Uniforme.
    Consiste num caso especifico da Procura Melhor-Primeiro, baseado na expressão f(n) = g(n). 
    Ao expandir sempre o nó com menor custo acumulado, garante encontrar a melhor solução do problema.
     Herda de Procura Melhor-Primeiro, de modo a especificar a estratégia de avaliação.
"""
class ProcuraCustoUnif(ProcuraMelhorPrim):
    
    """
    (Método) Construtor.
        Concretiza a estratégia injetando o 'AvaliadorCustoUnif' no mecanismo.
        Utiliza a função super() para referenciar a classe mãe (ProcuraMelhorPrim),
        invocando o seu construtor base de modo a inicializar corretamente a FronteiraPrioridade.
    """
    def __init__(self):
        super().__init__(AvaliadorCustoUnif()) # invoca o construturor da super classe