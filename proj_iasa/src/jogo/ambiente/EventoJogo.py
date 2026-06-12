from enum import Enum

"""
    (O Enum) Representa os eventos que podem ocorrer no ambiente do jogo.
"""
class EventoJogo(Enum):
    SILENCIO = 's'
    RUIDO = 'r'
    ANIMAL = 'a'
    FUGA = 'f'
    FOTOGRAFIA = 'p'
    TERMINAR = 't'

    def mostrar(self):
        print(f"\nEvento: {self.name} ")