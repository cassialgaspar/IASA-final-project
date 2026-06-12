from pee.prof.ProcuraProfundidade import ProcuraProfundidade

# só expande os nos se a profundadade do no for menor que a definida
"""
(A classe) Representa o mecanismo de Procura em Profundidade Limitada.
Esta classe estende a Procura em Profundidade clássica, introduzindo um limite de profundidade máximo para a árvore de exploração. 
Isto previne que o algoritmo se perca infinitamente em ramos muito profundos ou infinitos.
"""
class ProcuraProfLim(ProcuraProfundidade):

    """
    (Método) Inicializa o mecanismo garantindo que a classe mãe (ProcuraProfundidade) 
        é invocada, o que por sua vez configura a FronteiraLIFO necessária.
    """
    def __init__(self):
        super().__init__()

    """
    (Método) Inicia o processo de procura com um limite de profundidade estipulado.
        Antes de iniciar a procura, guarda o limite de profundidade no atributo privado.
        
        @param problema: O problema a resolver.
        @param prof_max: O limite máximo de profundidade permitido (por omissão, é 10).
        @return: A Solução encontrada ou None caso não encontre solução dentro do limite.
    """
    def procurar(self, problema, prof_max = 10):
        self.__prof_max = prof_max 
        return super().procurar(problema) 
    
    """
    (Método protegido) Interceta a expansão de um nó para aplicar a restrição de profundidade.
        Avalia se a profundidade do nó atual ainda é inferior ao limite máximo estabelecido. 
        Se for, invoca o método de expansão "normal" da classe mãe para gerar os sucessores. 
        Se o limite já tiver sido atingido, bloqueia a expansão e retorna uma lista vazia, 
        forçando o algoritmo a recuar (backtracking).
        
        @param problema: O problema que fornece os operadores.
        @param no: O nó que pretendemos expandir.
        @return: Uma lista de nós sucessores (List<No>), ou uma lista vazia se o limite for atingido.
    """
    def _expandir(self, problema, no):
        return super()._expandir(problema, no) if no.profundidade < self.__prof_max else []