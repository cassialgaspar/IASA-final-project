from pee.melhor_prim.ProcuraMelhorPrim import ProcuraMelhorPrim

"""
(Classe) Representa o mecanismo de Procura Informada.
    Especifica a procura Melhor-Primeiro e adiciona o conhecimento do 
    domínio (Heurísticas). É possível abandonar a exploração exaustiva para abordar 
    uma exploração seletiva e guiada do espaço de estados.
    Atua como base para os algoritmos de Procura A* e Sôfrega.
"""
class ProcuraInformada(ProcuraMelhorPrim):
    
    """
    (Método) Atribui a heurística no avaliador antes de começar a execução do 
        algoritmo à superclasse. Isto permite reutilizar a mesma 
        instância do planeador para testar diferentes heurísticas.
        
        @param problema: A representação do problema a resolver.
        @param heuristica: A estimativa de custo até ao objetivo (Heuristica).
        @return: A Solucao.
    """
    def procurar(self, problema, heuristica):
        
        self._avaliador.heuristica = heuristica 
        
        return super().procurar(problema)