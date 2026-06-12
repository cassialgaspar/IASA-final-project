from agente_prosp.controlo_react.reaccoes.recolher.Recolher import Recolher
from AgenteProsp import AgenteProsp
from agente_prosp.controlo_react.ControloReact import ControloReact
from sae import Simulador


"""Teste 3"""
if __name__ == "__main__":
    #Definea regra que o agente vai se basear em.
    comportamento = Recolher()

    # Damos explorar ao controlo para que este saiba exatamente a quem deve passar a perceção do ambiente.
    controlo = ControloReact(comportamento)


    # Damos-lhe ocontrolo recém-criado, para garantir que o agente consegue tomar decisões automáticas.
    agente = AgenteProsp(controlo)

    # O simulador é iniciado, carrega o mapa '1' e coloca lá o agente.
    simulador = Simulador(1, agente)

    # Executa o simulador, onde o agente percepciona o ambiente, processa a reação e atua sobre ela.
    simulador.executar()
