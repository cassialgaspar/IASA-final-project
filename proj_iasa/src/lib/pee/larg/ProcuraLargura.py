from pee.mec_proc.ProcuraGrafo import ProcuraGrafo
from pee.larg.FronteiraFIFO import FronteiraFIFO

"""
(A classe) Representa o mecanismo de Procura em Largura.
É um método de procura não informada focado em explorar os nós mais antigos primeiro, originando uma exploração exaustiva em cada nível de profundidade.
Herda de 'ProcuraGrafo' para beneficiar do mecanismo de memória global de nós 'explorados', permitindo-lhe detetar e evitar ciclos no espaço de estados.
"""
class ProcuraLargura(ProcuraGrafo):
    
    """
    (Método) Construtor da Procura em Largura.
        Inicializa o mecanismo passando para a classe mãe (ProcuraGrafo) uma FronteiraFIFO.
        A utilização exclusiva desta fronteira em formato fila (First-In, First-Out) é o que 
        garante que os novos nós (sucessores) vão para o fim da fila, forçando a avaliação 
        dos nós mais antigos primeiro.
    """
    def __init__(self):
        super().__init__(FronteiraFIFO())