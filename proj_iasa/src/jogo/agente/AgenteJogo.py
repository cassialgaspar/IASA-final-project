from agente.Agente import Agente
from jogo.agente.PercecaoJogo import PercecaoJogo

"""
(A classe) Representa um agente presente no jogo, e herda atributos e métodos da classe abstrata Agente. 
São implementados os métodos protegidos de interação do agente. O "_percecionar" 
delega a observação do estado atual ao método "observar()" do ambiente instanciado em self.__ambiente.
Por sua vez, o "_atuar" extrai o comando da ação pretendida e invoca o método "executar()" do 
ambiente para aplicar a ação no jogo.
"""
class AgenteJogo(Agente):

    """
    (Método) Construtor do agente
        @param ambiente: instância de AmbienteJogo representado pelo atributo self.__ambiente [1].
        @param controlo: instância de Controlo (pertencente ao subsistema agente), que é passada para inicializar a 
        superclasse e será responsável por processar as perceções [1, 2].
    """
    def __init__(self, ambiente, controlo):
        super().__init__(controlo)
        self.__ambiente = ambiente



    """
    (Método) Observa o ambiente para gerar uma perceção atualizada.
        @return: Instância de PercecaoJogo, instanciada com o evento devolvido pelo método 
        observar() do ambiente.
    """
    def _percecionar(self):
        evento = self.__ambiente.observar()
        return PercecaoJogo(evento)


    """
    (Método) Utiliza o ambiente de jogo para executar a ação correspondente.
        Extrai o comando (propriedade apenas de leitura) da ação e invoca a execução do mesmo no ambiente.
        @param accao: instância de AccaoJogo que contém o comando (ComandoJogo) a ser executado.
    """
    def _actuar(self, accao):        
        if accao is not None:
            # A classe AmbienteJogo possui o método executar(comando : Comando)
            # A classe AccaoJogo possui a propriedade comando : ComandoJogo
            self.__ambiente.executar(accao.comando)