from personagem.ControloPersonagem import ControloPersonagem
from agente.AgenteJogo import AgenteJogo

"""
(A classe) Representa um personagem(agente) no jogo e herdar atributos e métodos da classe AgenteJogo, 
para percepcionar eventos e agir.

    @param ambiente: o ambiente do jogo onde o personagem irá atuar
    
"""
class Personagem (AgenteJogo):
    def __init__(self, ambiente):
        super().__init__(ambiente, ControloPersonagem())
    
    def mostrar(self):
        """mostra o estado do controlo(herdado da classe Agente)"""
        print(f"\nEstado: {self._controlo.estado}")
    