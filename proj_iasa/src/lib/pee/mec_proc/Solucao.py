from pee.mec_proc.PassoSolucao import PassoSolucao

"""
(A classe) Representa um percurso correspondente à solução de um problema.
A solução de um problema corresponde a uma sequência de estados e operadores que liga um estado inicial a um estado objetivo.
É um objeto imutável que contêm a dimensão, o custo total e a os passos que o agente deve executar.
"""
class Solucao():
    
    """
    (Método) Construtor da solução.
        @param no_final: O nó que tem o estado "objetivo".
        
        A partir do nó final dado, o algoritmo vai pelos antecessores até à raiz (estado inicial),
        construindo a lista de passos que têm a solução pretendida.
    """
    def __init__(self, no_final):
        self.__dimensao = no_final.profundidade
        self.__custo = no_final.custo
        self._passos = []
        
        no = no_final
        while no.antecessor:
            passo = PassoSolucao(no.antecessor.estado, no.operador)
            self._passos.insert(0, passo) # insere o passo no início da lista
            no = no.antecessor

    """
    (Propriedade) Retorna a dimensão da solução .
        @return: O valor da dimensão (int).
    """
    @property
    def dimensao(self):
        return self.__dimensao

    """
    (Propriedade) Retorna o custo total do percurso.
        O custo da solucao é o custo acumulado do nó final.
        @return: O valor do custo (double).
    """
    @property 
    def custo(self):
        return self.__custo

    """
    (Método) Torna a classe iterável.
        Permite a iteração no percurso, que deixa que a solução 
        seja usada de forma simples num ciclo.
    """
    def __iter__(self):
        return iter(self._passos)

    """
    (Método) Permite obter os passos da solução através do seu índice.
        Este método permite usar parênteses retos diretamente no objeto, tal como fazemos nas listas, mantendo sempre
        o encapsulamento. 
        
        @param index: O índice do passo pretendido (int).
        @return: O PassoSolucao na posição solicitada.
    """
    def __getitem__(self, index):
        return self._passos[index]