from ecr.ComportComp import ComportComp

"""(Classe) implementa um comportamento composto que seleciona a ação a ser executada com base na 
prioridade mais alta entre as ações fornecidas. 
Ela herda da classe ComportComp, que é uma classe base para comportamentos compostos."""
class Prioridade(ComportComp):


    def __init__(self,comportamentos):
        super().__init__(comportamentos)

    """
    (Método) Seleciona a ação a executar de acordo com prioridade mais alta(função max).
    Caso existam ações com a mesma prioridade é indiferente qual delas é escolhida. 
    @param accoes: Lista de ações a serem avaliadas.
    """
    def seleccionar_accao(self,accoes):
        return max(accoes, key=lambda accao: accao.prioridade)
    
        #for acao in accoes:
        #   if acao.prioridade > max_prioridade:
        #        max_prioridade = acao.prioridade
        #return max_prioridade