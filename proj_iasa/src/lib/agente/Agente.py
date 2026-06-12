from abc import ABC, abstractmethod

"""
(A classe abstrata) Representa um agente inteligente com os comportamentos perceção, processamento e ação.
A classe será abstrata, pois os métodos percecionar e atuar também o são.

    @param ABC (biblioteca Abstract Base Classes) para que a classe seja abstrata.
"""
class Agente(ABC):

    """
    (Construtor)  onde o atributo controlo é classificado como protegido (possuindo na sua variável self um _), sendo apenas
    utilizado por instâncias que herdam a classe Agente. 
    É um método privado, será apenas utilizado pela mesma ("__")
    """
    def __init__(self, controlo):
        self._controlo = controlo

    """
    (O método) Obter perceção do ambiente. O método é abstrato, pois a perceção do ambiente é algo que depende do tipo de agente inteligente.
     O método é privado, pois é apenas utilizado pela classe Agente e suas subclasses.
    """
    @abstractmethod 
    def _percecionar(self):
        """Obter perceção do ambiente"""

    """
    (O método) Gera uma ação gerada através do processamento de uma dada perceção. A ação executada por
    este método será gerada através da interface Controlo.
    """
    @abstractmethod    
    def _actuar(self, acao):
        """Atua a ação do agente autónomo"""


    """
    (O método) Processamenta a perceção feita pelo agente inteligente. 
    Não possui underscore na sua designação, pois é público.
    """
    def executar(self):
        percecao = self._percecionar()

        acao = self._controlo.processar(percecao)
        if acao:
            self._actuar(acao)