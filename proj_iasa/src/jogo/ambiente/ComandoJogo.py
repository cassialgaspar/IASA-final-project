from enum import Enum

""" 
    (O Enum) Representa os comandos que o agente pode executar no jogo.
"""
class ComandoJogo(Enum):
    PROCURAR = 1
    APROXIMAR = 2
    OBSERVAR = 3
    FOTOGRAFAR = 4

    def mostrar(self):
        print(f"\nComando: {self.name} ")