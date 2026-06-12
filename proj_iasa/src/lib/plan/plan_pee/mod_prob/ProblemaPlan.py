from mod.Problema import Problema

"""(Classe) Representa o problema de planeamento, ou seja, o estado inicial, os operadores e o objetivo"""
class ProblemaPlan(Problema):
    def __init__(self, modelo_plan, estado_final):
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())
        self.__estado_final = estado_final

    """(Método) Verifica se o estado atual é o estado final desejado pela condição de objetivo"""
    def objectivo(self, estado):

        return estado == self.__estado_final