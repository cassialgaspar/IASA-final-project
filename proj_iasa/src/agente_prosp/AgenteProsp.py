from agente.Agente import Agente
import sae


"""
(A classe) Representa o Agente Prospector, que interage sempre com o ambiente mas nunca 
o afeta diretamente por pertencer a um simulador (SAE), usando Transdutor( para "tradução").


//pq ele so precisa de estesdois metodos???
"""
class AgenteProsp(Agente):
    
    """
    (Método) Percepciona o ambiente com o Transdutor para captar os dados do simulador e devolver a Percepção
    do ambiente atual (futuramente para estímulo para uma resposta rápida).
        @return: instância de Percepcao(conjunto de estímulos captados).
    """
    def _percecionar(self):
        return sae.transdutor.percepcionar()
    

    """
    (Método) Age no ambiente com auxilio do Transdutor.
        @return: instância de Accão.
    """
    def _actuar(self, accao):
        sae.transdutor.actuar(accao)
        