
class MecUtil:

    def __init__(self, modelo, gama, delta_max):
        """Construtor do mecanismo de utilidade."""
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max

    """ De acordo com um PDM, o agente vai querer descobrir qual a melhor solução em cada situação, num ambiente com incerteza, a longo prazo, logo mede 
    a vantagem de cada ação, dita de utilidade. Assim sendo escolhe esta ação para executar.
    O código implementa o algoritmo de cálculo interativo de Utilidade.U[s] representa o valor acumulado do que o agente
    espera obter apartir daquele estado até ao final, o max() garante que o agente escolhe a ação com maior beneficio.
    

       """
    def utilidade(self):
        """
        PSEUDO-CÓDIGO:
            1. Inicializar os estados utilidade(U(s) que é igual ao máximo) a 0 para todos os estado s pertencentes a S.
              (Poderá ser feito um dicionário)
            2. Fazer os seguintes passos (de 3-7) enquanto erro de iteração (delta) for maior que o erro máximo admissível
            (delta máximo) que corresponde ao limiar de convergência:
            3. Inicializar U anterior igual a U
            4. Inicializar delta a 0
            5. Para cada estado s em S fazer (6-7):
            6. U(s) vai ser igual ao máximo da ação(a) pertencente a A(s) de util ação(s, a , U anterior) 
            (função ainda por definir com os paramentros s, a ,U anterior)
            7. Definir delta como o máximo entre o valor de delta e o valor absoluto de U(s) - U anterior(s)
            8. Fora do ciclo iniciado no passo 2, retornar U
        """

        S, A = self.__modelo.S, self.__modelo.A #Não foi especificado que S e A viriam de modelo, nem que era necessário inicializá-los, mas de modo a ter código mais limpo foi adotada esta abordagem.
        U = {s: 0.0 for s in S()} #foi dito inicialmente no ponto 2 que U(s) era igual ao máximo, no entanto essa lógica não foi implementada logo neste ponto por não fazer sentido.

        while True: #ciclo referido no ponto 2, apesar de não ser explicitado claramente que seria um while (foi apenas dito enquanto que é subjetivo, podendo-se referir a um do while)
            U_ant = U.copy() #Não foi dito que era necessário criar uma cópia de U, no entanto é preciso para não perder o valor original de U.
            delta = 0 #ponto 4 do pseudocódigo.
            
            for s in S(): #ponto 5 do pseudocódigo
                U[s] = max([self.util_accao(a, s, U_ant) for a in A(s)], default = 0)# default é para a eventualidade de A[s] ser vazio, caso que não foi incluido no ponto 6.
                delta = max(delta, abs(U[s]- U_ant[s])) #ponto 7 do pseudocódigo, apesar de não ser explicito que se usaria a função max(máximo entre os valores) e abs( valor absoluto) do python.

            if delta < self.__delta_max: #limiar de convergência dito no ponto 2.
                break
        return U #passo 8
        

        

    """Como as ações são não determinísticas, isto é para um mesmo estado, posso fazer várias ações baseadas numa probabilidade, 
    o sistema nunca terá a certeza do que irá acontecer, podendo fazer um movimento bem-sucedido ou um desvio indesejado.
    Assim, a função tem como objetivo calcular a utilidade de uma ação, que nada mais é que o valor esperado da mesma.
    A recompensa serve essencialmente para o agente perceber que as recompensas imediatas têm mais valor que a mesma no futuro. 
    Este conceito é essencial pois o agente planeia sequências longas, e se somasse todas as recompensas futuras sem as descontar, 
    a soma cresceria até ao infinito, o que o impossibilitaria isso de tomar a decisão de qual o melhor caminho a 
    seguir
. """
    def util_accao(self, a, s, U):
        """
        PSEUDO-CÓDIGO:
            1. Fazer um ciclo somatório de modo a calcular U (utilidade da ação) com os seguintes passos:
            2. Calcular a probabilidade de transição (com a função T (ainda não desenvolvida)) através da a (ação) do o estado 
            para o estado sucessor
            3. Calcular a recompensa esperada(função R(ainda não desenvolvida)) através da a (ação) da transição do estado atual 
            para o sucessor
            4. Multiplicar o valor da utilidade do estado (U) sucessor com gama (desconto)
            5. Retornar o resultado 

        """

        #Ao contrário do que foi dito no pseudocódigo as funções T, R e suc já tinham sido desenvolvidas, apenas não nesta classe.
        #E assim, para ter código mais limpo, foi feito a atribuição das mesmas a variáveis locais.
        T, R, suc = self.__modelo.T, self.__modelo.R, self.__modelo.suc
        # a soma não foi feita em ciclo, mas sim através o método sum, de modo a ser mais eficiente
        # e os passos ditos em 2, 3, 4 e 5 foram feitos apenas em uma linhas.
        return sum(T(s, a, sn) * (R(s, a , sn) + self.__gama * U[sn]) for sn in suc(s, a))