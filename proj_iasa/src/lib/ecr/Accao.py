from agente.Accao import Accao as AccaoAgente

"""
(A classe) Especializa a ação anteriormente feita do agente para o contexto ECR(arquitetura reativa).
Ao acrescentar o conceito de prioridade, permite selecionar qual a ação a executar nos 
comportamentos compostos com base nesse valor
"""
class Accao(AccaoAgente):

    """
    (Método) Construtor da ação reativa.
        @param prioridade: float que define a prioridade da ação (o valor por omissão é 0).
    """
    def __init__(self, prioridade = 0):
        self.__prioridade = prioridade

    
    # Para gerar propriedades ou se faz com getters e setters de atributos privados(como 
    # neste caso seguinte) ou criando dinamicamente como em Controlo
    
    """
    (Propriedade) Getter da prioridade associada à ação (marcado como {read/write} na arquitetura).
        @return: O valor float correspondente à prioridade atual da ação.
    """
    @property
    def prioridade(self):
        return self.__prioridade
    
    """
    (Propriedade) Setter da prioridade associada à ação.
        @param valor: Novo valor em float a ser atribuído à prioridade.
    """
    @prioridade.setter
    def prioridade(self, valor):
        self.__prioridade = valor
