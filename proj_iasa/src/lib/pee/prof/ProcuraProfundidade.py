from pee.mec_proc.MecanismoProcura import MecanismoProcura # (Ver aviso de arquitetura acima)
from pee.prof.FronteiraLIFO import FronteiraLIFO

"""
(A classe) Representa o mecanismo de Procura em Profundidade.
É um método de procura que faz com que os nós mais recentes (os últimos a serem gerados) devam ser os 
primeiros a ser explorados. Isto faz com que o algoritmo explore exaustivamente um ramo da árvore de 
procura em profundidade antes de voltar atrás.
"""
class ProcuraProfundidade(MecanismoProcura):
    
    """
    (Método) Construtor.
        Inicializa o mecanismo de procura em profundidade. 
        O construtor instancia uma FronteiraLIFO e passa-a para a classe mãe. 
        É a utilização exclusiva desta fronteira LIFO que dita todo o comportamento "em profundidade" da procura.
    """
    def __init__(self):
        super().__init__(FronteiraLIFO())
