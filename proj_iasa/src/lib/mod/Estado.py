from abc import ABC, abstractmethod

"""
(Classe) Representa uma situação possível na resolução de um problema."""
class Estado(ABC):
    """
    (Método) Fornece a identidade única da instância (hash).
    @return: O identificador numérico (inteiro) único do estado.
    """
    def __hash__(self):
        return self.id_valor() ##retorna um inteiro
    
    """
    (Método) Avalia se este estado é igual a outro objeto.
    @param objecto: O outro objeto de estado a ser comparado.
    @return: Um valor booleano (True se forem o mesmo estado, False caso contrário).
    """
    def __eq__(self, objecto):
        return self.__hash__() == objecto.__hash__() ## objetos iguais se tiverem a mesma identidade
    #compara a igualdade dos objetos

    @abstractmethod
    def id_valor(self):
        """"""