import sae
from agente.Controlo import Controlo
from agente_prosp.control_delib.modelo.ModeloMundo import ModeloMundo
from agente_prosp.control_delib.MecDelib import MecDelib


"""
(Classe) Representa a componente de Controlo Deliberativo de um agente.
Herda de 'Controlo'.
"""
class ControloDelib(Controlo):
    
    """
    (Método) Inicializa todos os módulos do raciocínio prático como atributos privados e recebe o planeador.
    """
    def __init__(self, planeador):
        self.__planeador = planeador
        self.__modelo_mundo = ModeloMundo()

        self.__mec_delib = MecDelib(self.__modelo_mundo) 
        self.__objetivos = None # não há objetivos
        self.__plano = None #não há plano

    """(Método) Processa a percepção que o agente recebee retorna uma ação. 
    """
    def processar(self, percepcao):
        """ returns an action"""
        self.__assimilar(percepcao)

        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        #como o executar é feito independemente do reconsiderar, não faz sentido fazer um else e basta apenas retorná-lo
        return self.__executar() # executar é uma ação
        


    """
    (Método Privado) Atualizando a abstração interna (espaço de estados).
    """
    def __assimilar(self, percepcao):
        self.__modelo_mundo.actualizar(percepcao)
    
    """
    (Método Privado) Vê se os planos/objetivos devem ser reavaliados.
        Facilita o dinamismo do ambiente, a ativar a deliberação apenas se o mundo tiver sofrido alterações.

        @return: Um booleano (True se precisar de novos planos, False caso contrário).
    """
    def __reconsiderar(self):
        return self.__modelo_mundo.alterado or not self.__plano

    """
    (Método Privado) Em conjunto com a deliberação determina "o que fazer" a seguir, 
        atualizando o objetivo.
    """
    def __deliberar(self):
        self.__objetivos = self.__mec_delib.deliberar()

    """(Método Privado) """
    def __planear(self):
        if self.__objetivos:
            self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objetivos)
            #print(self.__plano) debug


    """(Método Privado) Executa um passo do plano, retornando a ação a ser tomada."""
    def __executar(self):
        self.__mostrar()

        if self.__plano: # se existir plano, obter operador do plano para o estado atual do agente
            estado = self.__modelo_mundo.obter_estado()
            operador = self.__plano.obter_accao(estado)

            if operador:
                return operador.accao
            else: #plano está dissincronizado, pois não há operador para o estado atual do agente
                self.__plano = None
                return None
            
    """(Método Privado) Mostra o modelo do mundo, o plano e os objetivos através do simulador"""
    def __mostrar(self):
        sae.vista.limpar() #limpa a vista 
        self.__modelo_mundo.mostrar(sae.vista) 

        if self.__plano: # verifica a existencia de plano para não tentar mostrar um plano inexistente
            self.__plano.mostrar(sae.vista)

        if self.__objetivos: # vertifica se existem objetivos para não mostrar objetivos inexistentes
            for objetivo in self.__objetivos:
                sae.vista.marcar_posicao(objetivo.posicao) # para cada objetivo de objetivos vamos itera-los e marcar a posição de cada um.

