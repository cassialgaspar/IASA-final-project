from plan.Planeador import Planeador
from plan.plan_pdm.modelo.ModeloPDMPlan import ModeloPDMPlan
from pdm.PDM import PDM
from plan.plan_pdm.PlanoPDM import PlanoPDM

"""
(Classe) Representa o Planeamento baseado em Processos de Decisão de Markov.
    É feito o desenvolvimento de para lidar com problemas de decisão sequencial em ambientes não-deterministas.
    Implementa a interface 'Planeador'.
"""

class PlaneadorPDM(Planeador):
    
    """
    (Método) Construtor. Recebe os parâmetros para fazer o algoritmo de iteração de valor: 
        o desconto temporal (gama) e o limiar de paragem (delta máximo).
        Utiliza valores por omissão para garantir uma instanciação segura da classe.
        
        @param gama: Fator de desconto temporal (por default 0.9).
        @param delta_max: Limiar de convergência do erro de utilidade (por default 1).
    """
    def __init__(self, gama = 0.9, delta_max = 1):
        self.__gama = gama
        self.__delta_max = delta_max


    """
    (Método) Resolve o Processo de Decisão de Markov para conseguir a política ótima.
        Pega nos objetivos e a abstração do mundo num Modelo PDM,
        resolve matematicamente o problema e consegue a política ótima.

        @param modelo_plan: A representação abstrata do problema.
        @param objetivos: A lista de estados-alvo pretendidos pelo agente.
        @return: Uma instância de PlanoPDM .
    """
    def planear(self, modelo_plan, objetivos):
        modelo_pdm_plan = ModeloPDMPlan(modelo_plan, objetivos)
        
        pdm = PDM(modelo_pdm_plan, self.__gama, self.__delta_max)

        utilidade, politica = pdm.resolver()

        return PlanoPDM(utilidade, politica)

