from ecr.Resposta import Resposta
from agente_prosp.accoes.Rodar import Rodar


"""(Classe) Representa a resposta de evitar um obstáculo, para tal necessita de estender Resposta. Quando o agente deteta 
uma percepção de um obstáculo, a resposta é rodar para uma direção diferente daquela onde o obstáculo se encontra."""
class RespostaEvitar(Resposta):
    def _obter_accao(self, percepcao):
        dir_agente = percepcao.direccao
        dir_resposta = dir_agente.rodar()

        return Rodar(dir_resposta)
    
