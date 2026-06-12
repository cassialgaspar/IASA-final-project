from mod.Estado import Estado

"""
(Classe) Especifica a base genérica 'Estado', encapsulando a posição e 
    fornecendo a implementação concreta para a identificação única do nó no grafo.
"""
class EstadoAgente(Estado):
    
    """
    (Método) Recebe a posição concreta e inicializa os atributos de forma privada.
        Ao assumir que a posição é um tipo imutável, o Python garante a criação de 
        um identificador inteiro único, fazendo o método hash() .
        
        @param posicao: As coordenadas físicas do agente no mundo.
    """
    def __init__(self, posicao):
        self.__posicao = posicao
        self.__id_valor = hash(posicao)

    """
    (Método) Cria um identificador único que representa o estado para posteriormente ser usado como ponto de comparação e indexação.
        
        @return: O identificador único gerado por hash (int).
    """
    def id_valor(self):
        return self.__id_valor
    
    """
    (Propriedade) @property torna possivel o atributo privado ser acessado de forma controlad, garantindo que a posição não é corrompida de fora.
        
        @return: A posição do agente.
    """
    @property
    def posicao(self):
        return self.__posicao