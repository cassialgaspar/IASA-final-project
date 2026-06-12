from abc import ABC


"""
(Classe Abstrata) Representa a base para Avaliadores Informados.
    Usa o conhecimento do domínio do problema (Heurística) para ordenar a fronteira de exploração, 
    o que torna o algoritmo numa procura guiada que explora o espaço de estados de forma seletiva.
"""
class AvaliadorHeur(ABC):

    """(Método) Construtor. Inicializa o atributo protegido que guardará a referência para a heurística."""
    def __init__(self):
        self._heuristica = None


    """(Getter) Permite aceder à heurística atual."""
    @property
    def heuristica(self):
        return self._heuristica
    
    """(Setter) Define a heurística a utilizar."""
    @heuristica.setter
    def heuristica(self, valor):
        self._heuristica = valor