"""
(A classe) Representa um nó da árvore.
Cada nó é um elemento da árvore, mantendo não só o estado, 
como também o caminho de como o agente lá chegou, a que nível de profundidade se encontra e o custo acumulado.
"""
class No():
    
    """
    (Método) Inicializa o nó com o estado atual, a ação que gerou este estado, o nó antecessor e o custo acumulado.
        @param estado: O estado a que corresponde o nó.
        @param operador: O operador que gerou o estado a que corresponde o nó.
        @param antecessor: O nó antecessor na árvore de procura.
        @param custo: O custo do percurso desde a raiz até a este nó.
    """
    def __init__(self, estado, operador = None, antecessor = None, custo = 0):
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        self.__custo = custo
        self.__prioridade = 0

        # Calcula a profundidade automaticamente, se tiver antecessor, é a profundidade dele + 1
        if antecessor:
            self.__profundidade = antecessor.profundidade + 1
        else:
            self.__profundidade = 0
    
    """
    (Método) Faz com que os nós possam ser comparados com base na sua prioridade.
        @param no: O nó com o qual este vai ser comparado.
        @return: Retorna True se a prioridade deste nó for estritamente menor que a do outro.
    """
    def __lt__(self, no): # lt == less than
        return self.prioridade < no.prioridade

    """ (Propriedade) Devolve a profundidade do nó na árvore de procura {read only}. """
    @property
    def profundidade(self):
        return self.__profundidade

    """ (Propriedade) Devolve o custo até ao nó {read only}. """
    @property
    def custo(self):
        return self.__custo

    """ (Propriedade) Devolve o valor da prioridade do nó ( para ordenar). """
    @property
    def prioridade(self):
        return self.__prioridade

    """ (Propriedade) Devolve o estado a que corresponde o nó {read only} . """
    @property
    def estado(self):
        return self.__estado
    
    """ (Propriedade) Devolve o nó antecessor na árvore de procura {read only}  """
    @property
    def antecessor(self):
        return self.__antecessor

    """ (Propriedade) Devolve o operador que criou o estado atual {read only} """
    @property
    def operador(self):
        return self.__operador
    
    @prioridade.setter
    def prioridade(self, valor):
        self.__prioridade = valor