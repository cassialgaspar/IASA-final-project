from sae import Direccao, Elemento
from agente_prosp.control_delib.modelo.OperadorMover import OperadorMover
import math
from agente_prosp.control_delib.modelo.EstadoAgente import EstadoAgente
from plan.modelo.ModeloPlan import ModeloPlano

"""
(Classe) Atua como a memória de representação onde a informação sensorial concreta é codificada pelo espaço de estados.
"""
class ModeloMundo(ModeloPlano):

    """
    (Método) Construtor.
    """
    def __init__(self):
        self.__estado = None
        self.__estados = []
        self.__elementos = {} #segundo uml é um dicionario

        self.__operadores = [OperadorMover(self, direccao) for direccao in Direccao]# em que direccao contem 4 ações base disponíveis (N, S, E, O)
        self.__alterado = False

    """
    (Método Python) Permite verificar se um determinado estado se encontra na lista de estados 
        reconhecidos atualmente pelo modelo, usando a sintaxe fluida: 'estado in modelo'.
    """
    def __contains__(self, estado):
        return estado in self.__estados


    """
    (Método) Retorna o estado atual no espaço de estados.
        @return: O EstadoAgente atual.
    """
    def obter_estado(self):
        return self.__estado

    """
    (Método) Retorna todos os estados gerados .
        @return: Uma lista de EstadoAgente (List<EstadoAgente>).
    """
    def obter_estados(self):
        return self.__estados

    """
    (Método) Retorna as ações possíveis.
        @return: Uma lista de OperadorMover contendo as transições de estado.
    """
    def obter_operadores(self):
        return self.__operadores


    """
    (Método) Verifica o tipo de elemento presente numa determinada posição/estado.
        Usa o dicionário .get() para retornar None com segurança se a célula estiver vazia.
        @param estado: O estado que contém a posição a verificar.
        @return: O Elemento correspondente ou None.
    """
    def obter_elemento(self, estado):
        return self.__elementos.get(estado.posicao) 
    

    """
    (Método) Avalia a distância entre um estado dado e o estado atual do agente.
        É/pode ser usado na deliberação heurística para apurar o alvo mais vantajoso.

        @param estado: O estado do alvo a avaliar.
        @return: A distância (double).
    """
    def distancia(self, estado):
        return math.dist(estado.posicao, self.__estado.posicao)


    """
    (Método) Converte a perceção nas estruturas abstratas de 'EstadoAgente', através da flag alterado caso o mapa de elementos 
        tenha sofrido modificações, permitindo ao agente saber se deve reconsiderar o plano.

        @param percepcao: O objeto com a informação do ambiente físico.
    """
    def actualizar(self, percepcao):
        """"""
        self.__estado = EstadoAgente(percepcao.posicao)
        self.__alterado = self.__elementos != percepcao.elementos
        
        if self.__alterado:
            self.__elementos = percepcao.elementos
            self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]
 
    """ (Método) O Modelo do Mundo é a memória de representação do agente. 
                Este método vai mostrar alvos e obstáculos, bem como a posição atual do agente, usando a interface 'vista' para a visualização.

                O método 'items' faz com que o elemento passe para um tuplo
    """
    def mostrar(self, vista):
        """"""
        for posicao, elemento in self.__elementos.items(): #mostra todos os elementos do mundo
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
                vista.marcar_posicao(self.__estado.posicao)

    """
    (Propriedade) Permite ver se o modelo foi alterado na última perceção.
        @property garante o encapsulamento, concretizando a parte {read only} exigida na arquitetura.
        @return: booleano (True se alterado, False se inalterado).
    """
    @property
    def alterado(self):
        """returns a boolean"""
        return self.__alterado
    
    @property
    def elementos(self):
        return self.__elementos
