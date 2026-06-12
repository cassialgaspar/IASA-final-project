from mod.Problema import Problema
from mod_prob.estado_contagem import EstadoContagem
from mod_prob.operador_incremento import OperadorIncremento

"""
(A classe) Representa a formulação do problema específico de contagem no espaço de estados.
A modelação de um problema requer a integração do estado inicial, do conjunto de operadores e do teste de objetivo.
"""
class ProblemaContagem(Problema):

    """
    (Método) Construtor do problema de contagem.
        Inicializa o problema injetando na superclasse o 'EstadoContagem' inicial e a lista de 
        'OperadorIncremento' gerados a partir das opções fornecidas.
        Guarda também o valor alvo (contagem_final) num atributo privado para ser usado na validação do objetivo.
        
        @param contagem_inicial: O valor numérico onde o processo começa.
        @param contagem_final: O valor limite numérico que o agente tenta atingir.
        @param incrementos: Uma lista (iterável) de valores possíveis para incrementar a contagem em cada passo.
    """
    def __init__(self, contagem_inicial, contagem_final, incrementos):
        super().__init__(EstadoContagem(contagem_inicial), [OperadorIncremento(inc) for inc in incrementos])
        self.__contagem_final = contagem_final

    """ 
    (Método) Neste problema específico, é objetivo atingido quando o valor numérico do estado atinge ou supera o valor final estipulado.
        
        @param estado: O estado a ser avaliado.
        @return: Retorna um booleano (True se o estado for objetivo, False caso contrário).
    """
    def objectivo(self, estado):
        return estado.contagem >= self.__contagem_final