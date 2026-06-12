from jogo.ambiente.EventoJogo import EventoJogo

class AmbienteJogo:
    def __init__(self):
        self.__eventos ={evento.value : evento for evento in EventoJogo}
        self.__evento = None 
        #dicionário que associa o valor do evento à sua representação num Enum

    def evoluir(self):
        """Evoluir o ambiente do jogo, gerando um evento"""
        self.__evento = self.gerar_evento()
        if self.__evento is not None:
            self.__evento.mostrar()

    def observar(self):
        """Observar o ambiente e retornar um evento"""
        return self.__evento

    def executar(self, comando):
        """Mostra o comando que é passado"""
        comando.mostrar()

    def gerar_evento(self):
        """Pergunta ao utilizador qual o evento que deseja gerar, e retorna o evento correspondente"""
        texto = input("\nEvento? ")
        return self.__eventos.get(texto)