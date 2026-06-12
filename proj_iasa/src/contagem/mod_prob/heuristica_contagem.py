from pee.melhor_prim.Heuristica import Heuristica

"""
(A classe) Representa a heurística específica para o Problema de Contagem.
Fornece uma estimativa de quão longe um determinado nó está do objetivo final, 
permitindo aos algoritmos de procura informada tomarem decisões inteligentes 
sobre que ramos da árvore explorar primeiro.
"""
# guarda o valor final e retorna uma metrica da distancia do valor do estado
class HeuristicaContagem(Heuristica):
    
    """
    (Método) Construtor.
        Inicializa a heurística guardando o valor alvo do problema.
        Este valor é mantido de forma privada para ser usado mais tarde como 
        referência no cálculo das distâncias.
        
        @param contagem_final: O valor numérico que o agente pretende alcançar.
    """
    def __init__(self, contagem_final):
        self.__contagem_final = contagem_final

    """
    (Método) Calcula a estimativa heurística h(n) para um dado estado.
        Aplica as regras do problema para estimar o esforço restante. 
        Neste caso, a distância ao objetivo é a diferença absoluta entre o objetivo 
        e o valor numérico em que o estado atual se encontra.
        
        @param estado: O estado atual da procura a ser avaliado.
        @return: Um valor numérico representando a distância estimada até ao objetivo.
    """
    def h(self, estado):
        # Retorna a diferença absoluta, garantindo que a métrica de distância é sempre não-negativa.
        return abs(self.__contagem_final - estado.contagem)