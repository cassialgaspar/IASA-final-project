"""
(A classe) Representa um passo individual dentro da solução de um problema.
Em PEE (Procura em Espaços de Estados), o processo tenta encontrar um percurso entre um estado inicial e um estado objetivo
"""
class PassoSolucao:
    
    """
    (Método) Construtor do passo de solução.
        @param estado: O estado atual em que o agente fica.
        @param operador: A ação (operador) que produziu a transição para este estado.
    """
    def __init__(self, estado, operador):
        self._estado = estado
        self._operador = operador

    """
    (Propriedade) Retorna a informação do estado deste passo (Read only).
        @return: A instância de Estado.
    """
    @property
    def estado(self):
        return self._estado
    
    """
    (Propriedade) Retorna a informação do operador aplicado(Read only).
        @return: A instância de Operador.
    """
    @property
    def operador(self):
        return self._operador