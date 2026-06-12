from agente_prosp.control_delib.ControloDelib import ControloDelib
from plan.plan_pee.PlaneadorPEE import PlaneadorPEE
from agente_prosp.AgenteProsp import AgenteProsp
from sae import Simulador

"""Teste 4 - implementação da lógica do modelo do mundo, planeadores e o mecanismo de deliberação, assim como as
 classes associadas/afetadas por estas."""
if __name__ == "__main__":
    planeador = PlaneadorPEE()
    controlo = ControloDelib(planeador)
    agente = AgenteProsp(controlo)

    simulador = Simulador(4, agente, vista_modelo = True) # mostra o painel lateral quando vista_modelo = True
    
    simulador.executar()
    