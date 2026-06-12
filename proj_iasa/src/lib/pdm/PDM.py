from pdm.MecUtil import MecUtil

class PDM():
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__mec_utis = MecUtil(modelo, gama, delta_max)


    """(Método) Utiliza a utilidade (U) para calcular a política ótima (π*(s)) e representa a política de tomada de decisão.
    Define qual a única ação que deve ser tomada em cada estado de modo a maximizar a utilidade esperada, e desse modo é considerado determinista.
    A função max() quando usada sem argumentos extra retorna o maior dos argumentos, no entanto esse não é o caso, e por isso funciona da seguinte forma:
    percorre a lista de ações A(s), passa-a pelo argumento key e retorna a ação com melhor pontuação(melhor) e não pontuação em si, que nada mais é que a política. 
    Esta lógica tornou-se mais fácil pela decisão de implementar um dicionário pol, onde a chave é o estado e o valor é ação ótima para esse estado.
    """
    def politica(self, utilidade):
        """vai retornar uma politica, corresponde às setas a vermelho"""
        A, S = self.__modelo.A, self.__modelo.S 
        pol = {} # inicialização de um dicionário vazio
        for s in S():
            if A(s): # verifica se existe uma ação para o estado s
                pol[s] = max( A(s), key = lambda a : self.__mec_utis.util_accao(a, s, utilidade)) # escolhe a ação que maximiza a utilidade esperada.

        return pol
    

    """ (Método) Para resolver o processo de decisão é preciso calcular a utilidade de cada estado e apartir dela calculara política.
    """
    def resolver(self):

        util = self.__mec_utis.utilidade() # calculo da utilidade de cada estado
        pol = self.politica(util) # calcula da politica apartir da utilidade

        return util, pol #retorna um tuplo com utilidade e política ótima
