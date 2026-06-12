from pee.melhor_prim.aval.Avaliador import Avaliador

"""
(A classe) Representa o avaliador de nós específico para a Procura de Custo Uniforme.
É focada na otimização do custo real do percurso. Herda a interface 'Avaliador', mas não utiliza 
qualquer heurística, definindo o mérito de um nó apenas pelo esforço já despendido para o alcançar e nunca pelo esforço
estimando para o alcançar.
"""

class AvaliadorCustoUnif(Avaliador):
    
    """
    (Método) Calcula a prioridade de um dado nó para a Procura de Custo Uniforme.
        A prioridade do nó é estritamente igual ao custo do percurso desde o primeiro nó até ao atual.
        Na fronteira com prioridade, isto garante que os nós com menor custo acumulado serão sempre os 
        primeiros a ser expandidos, fazendo com que a solução encontrada seja de menor custo possível.
        
        @param no: O nó da árvore de procura a ser avaliado.
        @return: O valor numérico correspondente ao custo real acumulado do nó.
    """
    def prioridade(self, no):
        # Retorna o custo que está guardado no nó (g(n))
        return no.custo  # f(n) = g(n)