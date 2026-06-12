from enum import Enum

class EstadoPersonagem(Enum):
    PROCURA = 1
    INSPECAO = 2
    OBSERVACAO = 3
    REGISTO = 4

    """(Classe) Mostra o estado atual do personagem"""
    def mostrar(self):
        print(f"\nEstado do personagem: {self.name}")
    