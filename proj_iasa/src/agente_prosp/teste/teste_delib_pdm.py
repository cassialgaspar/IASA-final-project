from agente_prosp.control_delib.ControloDelib import ControloDelib
from plan.plan_pdm.PlaneadorPDM import PlaneadorPDM
from agente_prosp.AgenteProsp import AgenteProsp
from sae import Simulador

"""Teste 5 - Teste de planeador PDM (NOT WORKING YET)"""
if __name__ == "__main__":
    planeador = PlaneadorPDM()
    controlo = ControloDelib(planeador)
    agente = AgenteProsp(controlo)

    simulador = Simulador(1, agente, vista_modelo = True) # mostra o painel lateral quando vista_modelo = True
    simulador.executar()