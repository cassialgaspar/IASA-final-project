from pee.mec_proc.Fronteira import Fronteira

"""
(A classe) Representa uma fronteira de exploração baseada em Last In, First Out (LIFO).
Esta classe faz a procura em profundidade e ao utilizar o LIFO, garante que o processo explora sempre 
primeiro os nós gerados mais recentemente, que correspondem aos mais baixos na árvore de procura.
"""
class FronteiraLIFO(Fronteira):
    
    """
    (Método) Insere um novo nó na fronteira.
        Sendo uma fronteira LIFO, os nós mais recentes têm de ser os primeiros a ser explorados. 
        Como a classe 'Fronteira' já define que a remoção se faz sempre no índice 0, 
        este método insere os novos nós precisamente no índice 0 (o início da lista).
        
        @param no: O nó (sucessor) a ser inserido na fronteira de exploração.
    """
    def inserir(self, no):
        self._nos.insert(0, no)