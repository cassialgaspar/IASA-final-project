from pee.mec_proc.ProcuraGrafo import ProcuraGrafo
from abc import ABC
from pee.melhor_prim.FronteiraPrioridade import FronteiraPrioridade


"""
(Classe Abstrata) Representa o mecanismo de Procura Melhor-Primeiro (Best-First).
    Explora o espaço de estados simulando as opções de menor 
    custo primeiro, baseando-se numa função de avaliação f(n) definida por um Avaliador.
    Dependendo do avaliador dado, pode comportar-se como um destes três algoritmos:
      1. Procura de Custo Uniforme (Exaustiva não-informada, f(n) = g(n))
      2. Procura Sôfrega (Informada por heurística pura, f(n) = h(n))
      3. Procura A* (Ótima, combinando custo e heurística, f(n) = g(n) + h(n))
    Atua como classe-base para algoritmos baseados em prioridade.
"""
class ProcuraMelhorPrim(ProcuraGrafo, ABC):

    """
    (Método) Construtor. Usa a estratégia de avaliação recebida na FronteiraPrioridade, 
        e invoca o construtor da superclasse (ProcuraGrafo) para inicializar a memória.
    """
    def __init__(self, avaliador):
        super().__init__(FronteiraPrioridade(avaliador)) #invoca o construtor da super classe com uma fronteira de prioridade
        self._avaliador = avaliador

    """
    (Método) Vai determinar se um nó já gerado deve ser mantido. Usa Procura Geral em Grafos, em que se o agente 
        gerar um estado que já explorou no passado, mas o custo do novo percurso (no.custo) for menor do que 
        o custo do percurso antigo já guardado em memória, o nó representa um melhor percurso e deve ser mantido 
        para exploração.
        
        @param no: O nó mais recente a avaliar.
        @return: True se deve manter o nó, False se deve descartar.
    """
    def _manter(self, no):
        """return boolean"""
        return super()._manter(no) or no.custo < self._explorados[no.estado].custo
    
    