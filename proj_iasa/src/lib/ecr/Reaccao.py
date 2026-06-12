from ecr.Comportamento import Comportamento

"""
(Classe) Associação de um estímulo a uma reposta. É a unidade base de um agente reativo e é um comportamento simples.
"""
class Reaccao(Comportamento):
    def __init__(self, estimulo, resposta):
        self.__estimulo = estimulo
        self.__resposta = resposta


    """(Método) Ativa a reação com base na perceção do ambiente (correspondente ao Diagrama de Sequência do slide 4, ProjetoIASA - Parte2.pdf).
        Avalia a presença de um estímulo e, se a sua intensidade for maior que zero, ativa a resposta associada, 
        definindo a prioridade da ação igual à intensidade obtida.
         
        @param percepcao: a perceção atual recebida do ambiente.
        @return: a ação (Accao) gerada pela resposta se o estímulo for detetado, ou None caso contrário.
    
    """
    def activar(self,percepcao):
        """Através do argumento percepcao ativa a reação"""

        intensidade = self.__estimulo.detectar(percepcao)

        if intensidade > 0:
        
            accao = self.__resposta.activar(percepcao, intensidade)
            return accao
       

