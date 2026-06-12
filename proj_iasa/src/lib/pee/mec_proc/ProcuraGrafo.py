from pee.mec_proc.MecanismoProcura import MecanismoProcura 

"""
(A classe) Representa uma extensão do mecanismo de procura genérico, otimizada para espaços de estados com ciclos (Grafos).
Garante que os estados não são explorados repetidamente. Para isso, introduz uma memória global de nós 'explorados' 
(abertos e fechados) indexada pelo estado.
"""
class ProcuraGrafo(MecanismoProcura):
    
    """
    (Método protegido) Inicia as estruturas de memória do mecanismo de procura.
        Ao começar ou reiniciar uma procura, chama primeiro o método da superclasse para garantir 
        que a fronteira de exploração é limpa/iniciada. Em seguida, cria um dicionário vazio para 
        guardar todos os nós que vão sendo explorados.
    """
    def _iniciar_memoria(self):
        super()._iniciar_memoria()
        self._explorados = {} # dicionario vazio para guardar os nos explorados

    """
    (Método protegido) Memoriza um nó gerado durante o processo de procura.
        Além de acionar a memorização da classe mãe, guarda este nó no dicionário de explorados. 
        @param no: O nó a ser memorizado.
    """
    def _memorizar(self, no):

        if self._manter(no): # corrigido e adicionado na ultima entrega, pois o teste 4 não respondia.
            self._explorados[no.estado] = no # guarda o no explorado (no dict criado anteriormente)
            super()._memorizar(no)

    """
    (Método protegido) Avalia se um nó mais recente deve ser mantido para exploração futura.
        Se o estado associado a este nó já estiver no dicionário de estados explorados, significa que este estado é repetido, 
        logo o nó deve ser descartado (retorna False).
        
        @param no: O nó que está a ser avaliado.
        @return: Retorna um booleano (True se o nó for novo e dever ser mantido, False se for repetido).
    """
    def _manter(self, no):
        # returns boolean
        return no.estado not in self._explorados