from pee.melhor_prim.aval.AvaliadorHeur import AvaliadorHeur

"""
(A classe) Representa o avaliador de nós específico para o algoritmo de Procura Sofrega.
Ao herdar de 'AvaliadorHeur', tem acesso à heurística do problema, utilizando-a para determinar
a prioridade de um nó na fronteira de exploração.
"""
class AvaliadorSof(AvaliadorHeur):
    
    """
    (Método) Calcula a prioridade de um dado nó segundo a regra da Procura Sôfrega.
        A prioridade do nó baseia-se na estimativa heurística da distância 
        desde o estado atual até ao estado objetivo, ignorando por completo o custo.
        Quanto menor o valor heurístico, maior a prioridade na fronteira.
        
        @param no: O nó da árvore de procura a ser avaliado.
        @return: O valor numérico correspondente à estimativa heurística do nó.
    """
    def prioridade(self, no):
        return self.heuristica.h(no.estado) # f(n) = h(n)