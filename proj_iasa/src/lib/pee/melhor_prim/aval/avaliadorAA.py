from pee.melhor_prim.aval.AvaliadorHeur import AvaliadorHeur

"""
(A classe) Representa o avaliador de nós específico para o algoritmo de Procura AA.
Herda de 'AvaliadorHeur' para ter acesso à estimativa heurística do problema, utilizando-a para o custo da árvore de procura.
"""
class AvaliadorAA(AvaliadorHeur):
    
    """
    (Método) Calcula a prioridade de um dado nó segundo a regra do algoritmo AA.
        Ao contrário da procuraSof, a prioridade aqui é definida pela soma entre o custo
        acumulado desde o nó inicial até ao nó atual (g(n)) e o valor estimado pela 
        heurística do nó atual até ao objetivo (h(n)). 
        Por esta lógica, na fronteira com prioridade, os nós com menor valor total serão expandidos primeiro.
        
        @param no: O nó da árvore de procura a ser avaliado.
        @return: O valor numérico correspondente ao custo total do nó.
    """
    def prioridade(self, no):
        return no.custo + self.heuristica.h(no.estado) 