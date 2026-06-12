import math
from  agente_prosp.control_delib.modelo.EstadoAgente import EstadoAgente
from mod.Operador import Operador 
from agente_prosp.accoes.Mover import Mover

"""
(Classe) Representa as ações reais possíveis que geram mudanças no problema.
    Herda de Operador, estendendo a sua base com atributos específicos(o ângulo e a ação física de movimento).
"""
class OperadorMover(Operador): 
    
    """
    (Método) Recebe o modelo do mundo e a direção pretendida, encapsula 
        estes valores de forma privada e inicializa a ação .
    """
    def __init__(self, modelo_mundo, direccao):
        self.__modelo_mundo = modelo_mundo
        self.__ang = direccao.value

        self.__accao = Mover(direccao)

    
    """(Método) Aplica a mudança de estado ao receber o estado atual e retorna o estado sucessor.
            Aplica uma translaçao geomética segundo o estado dado.

            No simulador as coordenadas em y têm direção de cima para baixo, e no cartesiano é o contrário desse modo dy terá de ser negativo.

    """
    def aplicar(self, estado):

        x, y = estado.posicao

        dx = round(self.__accao.passo * math.cos(self.__ang)) # Ação é da sae, e todas as acoes da sae têm passo
        dy = - round(self.__accao.passo * math.sin(self.__ang))

        estado_suc = EstadoAgente((x + dx, y + dy))

        if estado_suc in self.__modelo_mundo:
            return estado_suc 

    
    """ 
    (Método) Utiliza a métrica math.dist para o cálculo otimizado do esforço.
        
        @param estado: O EstadoAgente de origem.
        @param estado_suc: O EstadoAgente de destino.
        @return: Um double correspondente à distância percorrida.
    """
    def custo(self, estado, estado_suc):

        return max(math.dist(estado.posicao, estado_suc.posicao), 1)
    
    """
    (Método Python) Atua como ferramenta de debugging, mostrando a ação sem comprometer o encapsulamento da classe.
        Sobrescreve o comportamento nativo do __repr__. Utiliza o 
        operador '%' para injetar o valor dinâmico da 'accao' na string devolvida.
        
        @return: Representação textual do operador (string).
    """
    def __repr__(self):

        return f"OperadorMover(%)" % self.accao

    """
    (Propriedade) Retorna o ângulo do movimento associado ao operador.
        Como no UML concretiza a restrição {read only}, encapsulando o acesso.
        @return: Ângulo em radianos (double).
    """
    @property
    def ang(self):
        return self.__ang

    """
    (Propriedade) Retorna a ação física encapsulada neste operador.
        Põe como {read only} definido no UML, permitindo extrair 
        a ação que será efetivamente enviada aos atuadores do agente.
        @return: Objeto Mover (Accao).
    """
    @property
    def accao(self):
        return self.__accao