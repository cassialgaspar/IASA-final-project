from plan.Plano import Plano

"""(Classe) Representa um plano do planeamento do espaco de estados, onde cada passo é um tuplo (estado, operador)."""
class PlanoPEE(Plano):
    """ Por passo ser imútavel, é necessário criar uma nova lista e passar o valor dos passos de cada solução para essa lista.

        Ao não colocaros parênteses na linha 10, faz com que seja um objeto gerador.
    """
    def __init__(self, solucao):
        self.__passos = [passo for passo in solucao] #lista de passos em cada solucao

    """(Método) 'obter_accao': dado o estado atual, qual o a acao a executar?
        Neste específico o plano pee tem uma lista de passos e a acao que é necessário fazer, de modo verifica-se se o estado do 
        passo é igual ao estado passado, e entao o retorno é o operador desse passo, caso contrário o plano está dissincronizado 
        com o atual e retorna-se None.
    else """
    def obter_accao(self, estado):
        if self.__passos:
            passo = self.__passos.pop(0)

        if passo.estado == estado:
            return passo.operador

    """(Método) Se o plano pee tiver uma lista de passos, itera sobre eles e mostra-se um vector na vista, onde a posição do 
        vector é a posição do estado do passo e o angulo do vector é o angulo do operador do passo."""
    def mostrar(self, vista):
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)