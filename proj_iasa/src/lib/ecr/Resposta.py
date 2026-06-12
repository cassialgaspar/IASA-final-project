
"""(Classe) que define qual é a accão que o agente vai 
tentar fazer quando este deteta um estímulo, assim como a sua prioridade"""
class Resposta():

    """
    (Método) Construtor da resposta.
        Guarda a ação a executar quando esta resposta não for nula.
        @param accao: A ação que fica associada a esta resposta.
    """
    def __init__(self, accao = None):
        self._accao = accao

    """
    (Método) Prepara a ação para ser execcutada.
        Converte a 'força' do estímulo para a ação, através da prioridade. 
        
    """
    def activar(self, percepcao, intensidade = 0):

        accao = self._obter_accao(percepcao)

        if accao:
            accao.prioridade = intensidade
        
        return accao
        
        
    
    """
    (Método Protegido) Extrai a ação a executar face ao contexto.
        [Software] Padrão Hook / Ponto de extensão. Por norma devolve a ação estática, 
        mas permite que subclasses (como RespostaEvitar) reescrevam a lógica 
        para consultar a percepção e gerar uma ação dinamicamente.
        
        @param percepcao: A informação vetorial ou simbólica do ambiente (Percepcao).
        @return: A ação determinada por esta resposta (Accao).
    """

    #parametro percepcao n esta a ser usado mas é para caso se queira por uma 
    # restrição mais tarde
    def _obter_accao(self, percepcao):
        return self._accao
      