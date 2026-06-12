from plan.modelo.ModeloPlan import ModeloPlano

from pdm.modelo.ModeloPDM import ModeloPDM

from plan.modelo.ModeloPlan import ModeloPlano
from pdm.modelo.ModeloPDM import ModeloPDM

"""
(Classe) Usa herança múltipla e otimiza a velocidade de procura pré-calculando toda a dinâmica do mundo.
"""
class ModeloPDMPlan(ModeloPDM, ModeloPlano):

    """
    (Método) Construtor. Instancia as "regras" do problema e o ganho máximo (rmax, default 1000).
        Faz o mapeamento e guarda antecipadamente todas as transições possíveis para não 
        sobrecarregar o algoritmo iterativo mais tarde.
    """
    def __init__(self, modelo_plan, objectivos, rmax = 1000):
        self.__modelo_plan = modelo_plan
        self.__rmax = rmax
        self.__objectivos = objectivos

        
        #só é possível fazer esta lógica por ser um modelo determinístico, caso contrário teriamos de usar probabilidades
        self.__transicoes = {} #guarda todas as transições possíveis, usa tuplos (estado, accao) como chaves

        for s in self.obter_estados(): # varer todos os estados
            for a in self.obter_operadores(): # por todas as ações possíveis
                sn = a.aplicar(s) #obter o estado seguinte
                if sn is not None: #verifica se a ação é possível
                    self.__transicoes[(s, a)] = sn #guarda a transição no dicionário

    """(Método) Implementado de acordo com ModeloPlan """
    def obter_estado(self):
        return self.__modelo_plan.obter_estado()

    """(Método) Implementado de acordo com ModeloPlan """
    def obter_estados(self):
        return self.__modelo_plan.obter_estados()

    """(Método) Implementado de acordo com ModeloPlan """
    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()

    """(Método) Implementado de acordo com ModeloPDM, apesar de obter_estados ter a mesma implementação, é necessário implementar 
    este para garantir compatibilidade com o modelo PDM"""
    def S(self):
        return self.obter_estados()


    """(Método) Se  s nao tem objetivo, não há nada a fazer( 0 ações possíveis), por isso retorna-se uma lista vazia"""
    def A(self, s):
        return self.obter_operadores() if s not in self.__objectivos else []

    """(Método)Se no dicionário de transições existir a ação indicada, a probabilidade deverá ser 100% (1), se não é 0%"""
    def T(self, s, a, sn ):
        return 1 if sn is self.__transicoes[(s, a)] else 0
        
    """
    (Método) Modelo de Recompensa que penaliza custos de movimento (valores negativos) 
        e entrega o rmax (1000) se a transição o colocar num objetivo.
    """
    def R(self, s, a, sn):
        r = - a.custo(s, sn) #obter o custo da ação e identificá-lo como perda com o sinal negativo
        if sn in self.__objectivos:
            r += self.__rmax #se o estado for um dos objetivos, adiciona-se a recompensa máxima

        return r
    
    """(Método) """
    def suc(self, s, a):
        sn = self.__transicoes.get((s, a))
        if sn:
            return [sn]
        
        else:
            return []
    

