from plan.Planeador import Planeador
from pee.melhor_prim.ProcuraAA import ProcuraAA
from plan.plan_pee.PlanoPEE import PlanoPEE
from plan.plan_pee.mod_prob.ProblemaPlan import ProblemaPlan
from plan.plan_pee.mod_prob.HeurDist import HeurDist

"""(Classe) só planeado até ao primeiro objetivo, com base no mecanismo de procura A*"""
class PlaneadorPEE(Planeador):
    """(Construtor) Inicializa o mecanismo de procura e atribuí-lo a estratégia de resolução, neste caso a procura AA"""
    def __init__(self):
        self.__mec_pee = ProcuraAA()


    """(Método) Cria um plano para resolver o primeiro objetivo da lista."""
    def planear(self, modelo_plan, objetivos):
        objetivo = objetivos[0] #escolher o objetivo que vamos atingir
        problema = ProblemaPlan(modelo_plan, objetivo) #instancia de problema de planeamento
        heuristica = HeurDist(objetivo) #instancia de heuristica

        solucao = self.__mec_pee.procurar(problema, heuristica) # obtem a solucao atavés do mecanismo de procura definido

        if solucao:
            return PlanoPEE(solucao) #retorna uma instancia de plano PEE com base nessa solução

