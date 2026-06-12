from agente_prosp.accoes.Avancar import Avancar

"""
(A classe) Comportamento que explora com memória. 
Guarda as situações recentes (posição e direção) para não repetir acções nos mesmo lugares.
"""
class ExplorarMem():
    
    """
    (Método) Construtor.
        Inicializa o limite de memória e a ação Avançar.

        @param dim_max_mem: Memória máxima (100 por omissão).
    """
    def __init__(self, dim_max_mem = 100):
       self.__dim_max_mem = dim_max_mem # tamanho limite da memoria
       self.__memoria = []
       self.__accao = Avancar()

    """
    (Método) Ativa o comportamento.
        Se a situação em que o agente se encontrar for nova, regista-a na memória e permite o mesmo avançar.

        @param percepcao: A perceção do ambiente.
        @return: Ação de Avançar se a situação for nova.
    """
    def activar(self, percepcao):
        situacao = (percepcao.posicao, percepcao.direccao)
        
        # Só atua se o agente ainda não passou por esta exata situação
        if situacao not in self.__memoria:
            self.__memoria.append(situacao)
            
            # Descarta a situação mais antiga se exceder o limite
            if len(self.__memoria) > self.__dim_max_mem:
                self.__memoria.pop(0)
                
            return self.__accao
            
        # Retorna None (implícito em Python) se já conhece a situação