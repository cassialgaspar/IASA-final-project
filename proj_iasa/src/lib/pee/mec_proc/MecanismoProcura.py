from abc import ABC
from pee.mec_proc.No import No
from pee.mec_proc.Solucao import Solucao

"""
(A classe abstrata) Representa contêm o raciocínio automático através de procura.
Esta classe agrega a lógica transversal (o ciclo de procura e a expansão de nós) que é comum a qualquer algoritmo de resolução 
de problemas, delegando os detalhes específicos (como a política da fronteira) para as suas subclasses.
"""
class MecanismoProcura(ABC):
    
    """
    (Método) Construtor.
        Guarda a fronteira de exploração no seu respetivo atributo protegido. 
        A fronteira injetada (LIFO, FIFO, Prioridade) é o que vai ditar a estratégia de controlo 
        do mecanismo durante o ciclo de procura.
        @param fronteira: Estrutura responsável por gerir os nós gerados mas abertos.
    """
    def __init__(self, fronteira): 
        self._fronteira = fronteira

    """
    (Método protegido) É responsável por inicializar as estruturas de memória do mecanismo de procura.
        Nesta classe base, limita-se a iniciar a fronteira de exploração (garantindo que está limpa). 
    """
    def _iniciar_memoria(self):
        self._fronteira.iniciar()

    """
    (Método protegido) Responsável por memorizar um nó na memória do mecanismo de procura.
        Na sua forma mais simples (procura em árvore), memorizar um nó significa apenas 
        inseri-lo na fronteira de exploração para que seja avaliado mais tarde.
        @param no: O nó gerado que deve ser guardado na memória.
    """
    def _memorizar(self, no): 
        self._fronteira.inserir(no)

    """ 
    (Método) Executa o ciclo principal de procura para encontrar a solução do problema.
        Cria o nó inicial, arranca o ciclo de exploração e retira sucessivamente nós da fronteira.
        Avalia cada nó: se atingir o objetivo, retorna a Solução; caso contrário, expande-o e 
        memoriza os seus sucessores para continuar o ciclo.
        
        @param problema: O problema de planeamento a ser resolvido.
        @return: Um objeto do tipo Solucao se encontrar o objetivo, ou None se a fronteira esvaziar sem sucesso.
    """
    def procurar(self, problema):
        self._iniciar_memoria()
        no = No(problema.estado_inicial)
        self._memorizar(no)

        # Enquanto existirem nós abertos por explorar na fronteira
        while not self._fronteira.vazia:
            no = self._fronteira.remover()

            # Se o estado do nó atual for o objetivo do problema
            if problema.objectivo(no.estado): 
                return Solucao(no)
            
            # Expande o nó atual e memoriza todos os sucessores válidos gerados
            for no_suc in self._expandir(problema, no):
                self._memorizar(no_suc)
                
        # Retorna None implicitamente se acabar o espaço de estados sem sucesso

    """
    (Método protegido) Responsável por expandir um nó e devolver uma lista de nós sucessores.
        Aplica todos os operadores disponíveis no problema ao estado do nó atual. 
        Para cada transição válida, calcula o custo acumulado (custo do antecessor + custo da transição) 
        e cria um novo Nó que é adicionado à lista de sucessores.
        
        @param problema: O problema (que contém a lista de operadores a aplicar).
        @param no: O nó atual que pretendemos expandir.
        @return: Uma lista de objetos No (list of No) correspondentes aos estados gerados.
    """
    def _expandir(self, problema, no):
        sucessores = []
        estado = no.estado
        
        for operador in problema.operadores:
            estado_suc = operador.aplicar(estado) # transforma no estado sucessor atraves do atual
            
            # verificacao da existencia do estado (se o operador pôde ser aplicado)
            if estado_suc is not None:
                # Calcula o novo custo acumulado do percurso desde a raiz até este sucessor
                custo = no.custo + operador.custo(estado, estado_suc)
                # Instancia o novo nó referenciando o pai (no) e a ação tomada
                no_suc = No(estado_suc, operador, no, custo) 
                sucessores.append(no_suc)
                
        return sucessores