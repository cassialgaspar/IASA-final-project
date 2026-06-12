from agente.Controlo import Controlo


"""
(Classe) Representa a unidade interna de um agente que produz uma resposta por reação ao 
estímulo da percepção.
O controlo limita-se a atribuir a decisão de Comportamento
"""

class ControloReact(Controlo):
    def __init__(self,comportamento):
        self.__comportamento = comportamento


    """
    (Método) Recebe a perceção atual(os estímulos captados pelo agente) do ambiente para decidir 
        a próxima ação através do método activar. 
        @param percecao: Estado atual ambiente à volta do agente.
        @return: A ação a executar no ambiente.
    """
    def processar(self, percecao):
        return self.__comportamento.activar(percecao)

