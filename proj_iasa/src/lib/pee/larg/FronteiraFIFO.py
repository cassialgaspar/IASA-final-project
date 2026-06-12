from pee.mec_proc.Fronteira import Fronteira

"""
(A classe) Representa uma fronteira de exploração baseada em First-In, First-Out (FIFO).
Em PEE, esta classe procura em largura. Ao atuar como uma fila, garante que o processo explora sempre 
primeiro os nós mais antigos da árvore de procura, que correspondem aos mais altos na árvore de procura.
"""
class FronteiraFIFO(Fronteira):
    
    """
    (Método) Insere um novo nó na fronteira.
        Sendo uma fronteira FIFO, os nós mais recentes devem aguardar a sua vez,
        sendo inseridos no fim da fronteira de exploração. O método '.append()' 
        das listas serve para este propósito, pois adiciona automaticamente o nó 
        no final da lista '_nos'.
        
        @param no: O nó a ser inserido na fronteira de exploração.
    """
    def inserir(self, no):
        self._nos.append(no)