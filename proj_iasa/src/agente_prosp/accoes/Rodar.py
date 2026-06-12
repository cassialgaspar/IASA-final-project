
from ecr.Accao import Accao
from sae import Movimento


"""
(Classe) Movimento de rotação do agente (girar para a esquerda ou direita).
"""
class Rodar(Movimento, Accao):


    """
    (Método) Construtor.
        @param direccao: A nova direção para a qual queremos que o agente rode.
        
        Chama a classe, passando a direção e um passo de '0' . 
        Passamos o valor 0 porque a intenção é que o agente rode apenas sobre si mesmo, 
        sem dar qualquer passo em frente no cenário.
    """
    def __init__(self, direccao):
        
        super().__init__(direccao, 0)

