from mod.Estado import Estado

class EstadoContagem(Estado):

    def __init__(self, contagem):
        self.__contagem = contagem


    """
    (Método) Associa um número inteiro único a cada estado, de modo a que o algoritmo de procura 
        em grafos perceba se já expandiu este estado.
    """
    def id_valor(self):
        return self.__contagem # inteiro que representa o estado
    # é possivel tambem fazer hash(self.__contagem) 


    """
    (Getter) Permite consultar o valor da contagem atual do estado.
    """
    @property 
    def contagem(self):
        return self.__contagem
