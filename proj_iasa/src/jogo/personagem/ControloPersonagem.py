from agente.Controlo import Controlo
from jogo.agente.AccaoJogo import AccaoJogo
from jogo.ambiente.ComandoJogo import ComandoJogo
from jogo.ambiente.EventoJogo import EventoJogo

from maqest.MaquinaEstados import MaquinaEstados
from jogo.personagem.EstadoPersonagem import EstadoPersonagem

"""
(A classe) Implementa o controlo específico da personagem, herdando da interface Controlo.
Utiliza uma máquina de estados para gerir a dinâmica de comportamento baseada nos eventos do ambiente.
"""
class ControloPersonagem(Controlo):
    
    """
    (Método) Construtor do controlo da personagem.
        Inicializa a superclasse, define as instâncias de ações possíveis (associando os comandos do jogo) 
        e instancia a máquina de estados (no atributo privado self.__maq_est) com o estado inicial (PROCURA) 
        e a lista detalhada de transições (Estado_Anterior, Evento, Estado_Sucessor, Accao).
    """
    def __init__(self):
        # Instanciação das ações possíveis da personagem encapsulando os respetivos comandos
        procurar = AccaoJogo(ComandoJogo.PROCURAR)
        aproximar = AccaoJogo(ComandoJogo.APROXIMAR)
        observar = AccaoJogo(ComandoJogo.OBSERVAR)
        fotografar = AccaoJogo(ComandoJogo.FOTOGRAFAR)

        # Estado inicial da personagem é o de procura, e a máquina de estados
        # recebe a configuração completa da dinâmica da personagem baseada em tuplos de transição
        self.__maq_est = MaquinaEstados(
            EstadoPersonagem.PROCURA, 
                [(EstadoPersonagem.PROCURA, EventoJogo.ANIMAL, EstadoPersonagem.OBSERVACAO, aproximar), 
                (EstadoPersonagem.PROCURA, EventoJogo.RUIDO, EstadoPersonagem.INSPECAO, aproximar),
                (EstadoPersonagem.PROCURA, EventoJogo.SILENCIO, EstadoPersonagem.PROCURA, procurar),

                (EstadoPersonagem.INSPECAO, EventoJogo.SILENCIO, EstadoPersonagem.PROCURA),
                (EstadoPersonagem.INSPECAO, EventoJogo.RUIDO, EstadoPersonagem.INSPECAO, procurar),
                                         
                            
                (EstadoPersonagem.INSPECAO, EventoJogo.ANIMAL, EstadoPersonagem.OBSERVACAO, aproximar),

                (EstadoPersonagem.OBSERVACAO, EventoJogo.FUGA, EstadoPersonagem.INSPECAO),
                (EstadoPersonagem.OBSERVACAO, EventoJogo.ANIMAL, EstadoPersonagem.REGISTO, observar),
                                         
                (EstadoPersonagem.REGISTO, EventoJogo.ANIMAL, EstadoPersonagem.REGISTO, fotografar),
                (EstadoPersonagem.REGISTO, EventoJogo.FUGA, EstadoPersonagem.PROCURA),
                (EstadoPersonagem.REGISTO, EventoJogo.FOTOGRAFIA, EstadoPersonagem.PROCURA)])


    """
    (Método) Exibe textualmente na consola a classe de controlo.
    """
    def mostrar(self):
        print(f"\nControlo: {self.__class__.__name__} ")

    
    """
    (Método) Processa uma nova perceção do ambiente de forma a que a personagem tome uma decisão.
        Extrai a propriedade 'evento' da perceção recebida e invoca o processamento 
        desse evento na máquina de estados interna.

        @param percepcao: instância de PercepcaoJogo (interface que contém o evento atualizado).
        @return: instância de AccaoJogo (ou Nulo) correspondente à transição feita pela máquina de estados.
    """
    def processar(self, percepcao):
        evento = percepcao.evento
        acao = self.__maq_est.processar(evento)
        return acao
        

    """
    (Propriedade) Acesso ao estado atual (marcado como {read only} na arquitetura).
        @return: O valor Enum (EstadoPersonagem) do estado atual em que a máquina de estados se encontra.
    """
    @property
    def estado(self):
        return self.__maq_est.estado