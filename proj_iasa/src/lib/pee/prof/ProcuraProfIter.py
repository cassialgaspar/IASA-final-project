from pee.prof.ProcuraProfLim import ProcuraProfLim

"""
(A classe) Representa o mecanismo de Procura em Profundidade Iterativa.
É um método de procura resolve o problema dos ramos infinitos da procura em profundidade "normal". 
Herda de 'ProcuraProfLim' (Procura em Profundidade Limitada), utilizando-a várias vezes com limites 
de profundidade cada vez maiores até encontrar a solução do problema.
"""
class ProcuraProfIter(ProcuraProfLim): 
    
    """
    (Método) Executa o processo de procura no espaço de estados repetidamente.
        A cada iteração do ciclo, aumenta o limite de profundidade ('prof_max') de acordo com o 
        incremento ('inc_prof'). Recorre ao método super().procurar() para que a classe mãe (ProcuraProfLim) 
        realize a execução prática da PEE.
        
        @param problema: O problema a resolver.
        @param inc_prof: O incremento da profundidade a cada iteração (por omissão é 1).
        @param limite_prof: A profundidade máxima absoluta que o algoritmo tem permissão para atingir (por omissão é 100).
        @return: Retorna a Solucao encontrada ou None se ultrapassar o limite_prof sem sucesso.
    """

    def procurar(self, problema, inc_prof = 1, limite_prof = 100):
        
        # O ciclo começa na profundidade 0 e vai até ao limite_prof, saltando inc_prof
        for prof_max in range(0, limite_prof, inc_prof):

            solucao = super().procurar(problema, prof_max)
            
            # Se a classe mãe devolver uma solução válida (não nula), o processo termina e devolve-a
            if solucao:
                return solucao
                