from mod.Operador import Operador
from mod_prob.estado_contagem import EstadoContagem

"""
(A classe) Representa uma ação específica no problema de contagem, neste caso, incrementar o valor.
Os operadores modelam as ações que produzem a transição de uma configuração do problema para outra, gerando os nós sucessores.
Esta classe faz o operador genérico, definindo como o incremento é aplicado ao estado e qual o seu custo.
"""
class OperadorIncremento(Operador):
    
    """
    (Método) Construtor.
        Inicializa o operador com o valor do incremento a ser aplicado.
        O valor é guardado de forma privada para garantir o encapsulamento.
        
        @param incremento: O valor numérico a somar à contagem atual.
    """
    def __init__(self, incremento):
        self.__incremento = incremento

    """
    (Método) Aplica o operador a um estado para gerar um novo estado sucessor.
        
        @param estado: O estado atual (objeto EstadoContagem) onde a ação vai ocorrer.
        @return: Um novo objeto 'EstadoContagem' contendo o valor já incrementado.
    """
    def aplicar(self, estado):
        return EstadoContagem(estado.contagem + self.__incremento)

    """
    (Método) Calcula o custo de aplicar este operador.
        Aplica a regra do problema para calcular o "esforço" desta transição.
        Neste caso particular, o custo é o quadrado do valor do incremento.
        
        @param estado: O estado de origem.
        @param estado_suc: O estado de destino.
        @return: O inteiro que correspondente ao esforço da transição.
    """
    def custo(self, estado, estado_suc):
        return (self.__incremento**2)

    """
    (Propriedade) Devolve o valor do incremento associado a este operador {read only}.
    """
    @property
    def incremento(self):
        return self.__incremento