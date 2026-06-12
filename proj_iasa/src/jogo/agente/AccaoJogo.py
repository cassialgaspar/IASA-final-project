from agente.Accao import Accao

"""guarda comandos do jogo"""
class AccaoJogo(Accao):
    """Classe que representa a ação do agente no jogo"""
    def __init__(self, comando):
        self.__comando = comando

    @property
    def comando(self):
        """Retorna o comando do jogo"""
        return self.__comando  #privado para evitar que houvessem duas entradas de eventos (distinguir entrada de eventos do jogo e entrada de eventos do agente inteligente)
    
