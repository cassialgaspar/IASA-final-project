from pee.mec_proc.Fronteira import Fronteira
from heapq import heappush, heappop # importa as funcoes de insercao e remocao de elementos da fila de prioridade
#utiliza o avaliador para gerar a rioridade do no, e o remover retira da lista dos nos
"""
(A classe) Representa uma fronteira de exploração baseada na prioridade dos nós.
Esta classe é o ponto central de "Procura Melhor-Primeiro". Ao contrário das fronteiras "cegas" (LIFO/FIFO), 
esta fronteira garante que o próximo nó a ser explorado é sempre aquele que apresenta a melhor prioridade, calculada 
no momento da inserção.
"""
class FronteiraPrioridade(Fronteira):
    
    """
    (Método) Inicializa a fronteira recebendo uma instância de um Avaliador..
        
        @param avaliador: O objeto responsável por ditar como a prioridade de um nó é calculada.
    """
    def __init__(self, avaliador):
        super().iniciar() # Garante que a lista _nos da classe base é iniciada
        self.__avaliador = avaliador

    """
    (Método) Insere um novo nó na fronteira ordenando-o pela sua prioridade.
        Antes de inserir o nó na estrutura, recorre ao Avaliador para calcular e atribuir 
        o valor numérico da sua prioridade. Em seguida, usa a função 'heappush' para inserir o nó,
        que o coloca automaticamente na posição correta da árvore/fila de prioridade.
        
        @param no: O nó a ser inserido na fronteira.
    """
    def inserir(self, no):
        no.prioridade = self.__avaliador.prioridade(no) # atribui a prioridade do nó usando o avaliador
        heappush(self._nos, no) # insere o nó na fronteira usando a função de inserção da fila de prioridade

    """
    (Método) Remove e retorna o melhor nó da fronteira.
        Em vez de um simples pop(), utiliza a função 'heappop' que garante a remoção do elemento que está no topo da heap 
        (o nó com o menor valor na propriedade 'prioridade').
        
        @return: O próximo nó a ser expandido.
    """
    def remover(self):
        return heappop(self._nos) # remove o nó com menor prioridade 