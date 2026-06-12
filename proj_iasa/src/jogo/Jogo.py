from personagem.Personagem import Personagem
from ambiente.AmbienteJogo import AmbienteJogo

"""(Classe) Teste 1 - Executa o jogo, criando o ambiente e o personagem e fazendo a interação entre eles"""
class Jogo:
    def __init__(self):
        self.__ambiente = AmbienteJogo()
        self.__personagem = Personagem(self.__ambiente)

        self.__personagem.mostrar()


    def executar(self):
        
        while True:
            self.__ambiente.evoluir()
            self.__personagem.executar()
            
            self.__personagem.mostrar()

            if self.__ambiente.observar().value == "t":
                print("Jogo a terminar...")
                break


if __name__ == "__main__":
    Jogo().executar()        