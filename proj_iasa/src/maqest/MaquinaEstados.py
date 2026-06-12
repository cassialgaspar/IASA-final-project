
"""(A classe) Resposável por transicionar estados a partir de eventos, e por
            determinar as ações a executar a partir do estado atual e do evento recebido.
"""
class MaquinaEstados():

    def __init__(self, estado_inicial, transicoes):

        self.__estado = estado_inicial


        self.__tte =  {} #tabela trasição-estado
        self.__tae = {} #tabela ação-estado

        if transicoes:
            for transiccao in transicoes:
                estado_ant, evento, estado_suc, accao = transiccao \
                if len(transiccao) == 4 else transiccao + (None,)
                self.definir_transicao(estado_ant, evento, estado_suc, accao)



    def definir_transicao(self, estado_ant, evento, estado_suc, accao):
        """Define a mudança de um estado para outro, a partir de um evento e de uma ação."""
        self.__tte[(estado_ant, evento)] = estado_suc

        if accao:
            self.__tae[(estado_ant, evento)] = accao


    def processar(self, evento):
        """A partir do estado atual e do evento recebido, determina o próximo estado e a ação a executar."""
        accao = self.__tae.get((self.__estado, evento)) # obtem a ação a executar apartir do estado atual e do evento

        novo_estado = self.__tte.get((self.__estado, evento)) # obtem o próximo estado apartir do estado atual e do evento
        if novo_estado is not None: # caso exista uma transição definida para o estado atual
            self.__estado = novo_estado # atualiza o estado atual para o próximo estado

        return accao
    
    @property
    def estado(self):
        return self.__estado
    