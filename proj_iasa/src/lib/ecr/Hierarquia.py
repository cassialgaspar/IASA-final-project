from ecr.ComportComp import ComportComp

"""
(Classe) implementa um comportamento composto que seleciona a ação a ser executada com base na 
prioridade mais alta entre as ações fornecidas. 
Ela herda da classe ComportComp, que é uma classe base para comportamentos compostos."""
class Hierarquia(ComportComp):

    def __init__(self,comportamentos):
        super().__init__(comportamentos)
        

    """(Método) Seleciona a ação a executar com base na prioridade mais alta entre as ações fornecidas.
        @param accoes: Lista de ações a serem avaliadas."""
    def seleccionar_accao(self, accoes):

       if accoes: 
           return accoes[0]