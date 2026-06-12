from sae import Elemento

"""
(Classe) Mecanismo de Deliberação do agente autónomo que decidir "o que fazer" baseando-se no Modelo do Mundo, 
gerando e selecionando os objetivos que o agente deve tentar atingir.
"""
class MecDelib():
    
    """
    (Método)Inicializa a deliberação recebendo a representação interna do ambiente.
        
        @param modelo_mundo: O modelo do mundo que contém os estados e as posições dos elementos.
    """
    def __init__(self, modelo_mundo):
        self.__modelo_mundo = modelo_mundo
        
    """
    (Método) Gera todos os estados objetivos(têm objeto alvo) e seleciona-os. 
             Caso hajam opções válidas, submete essa lista ao processo de seleção interna para determinar qual o alvo que deve ser perseguido de imediato.

             
        @return: Uma lista de objetivos (List<EstadoAgente>) com 1 ou mais objetivos selecionados, 
                 ou uma lista vazia caso não haja alvos.
    """
    def deliberar(self):

        objectivos = self.__gerar_objectivos()  # gerar os objetivos
        if objectivos: 
            return self.__seleccionar_objectivos(objectivos) #verificação de existencia de objetivos

    """
    (Método privado) Vê todos os estados conhecidos pelo modelo do mundo e filtra aqueles 
        onde se encontra um elemento da classe 'ALVO'.
        
        @return: Uma lista de estados (List<EstadoAgente>) que representam os alvos disponíveis.
    """
    def __gerar_objectivos(self): # (Nota: Escrito com 'c' para espelhar perfeitamente o UML)
        return [estado for estado in self.__modelo_mundo.obter_estados() if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]
    
    """
    (Método privado) Seleciona o melhor objetivo de entre as opções disponíveis.
        Recebe os objetivos válidos e ordena-os. Usa 'distancia' do modelo do mundo para dar 
        prioridade aos alvos mais próximos.
        
        @param objectivos: A lista de estados que podem ser o objetivo.
        @return: Uma lista com apenas o estado selecionado (o primeiro da lista ordenada).
    """
    def __seleccionar_objectivos(self, objectivos):
        # Ordena a lista in-place utilizando a distância a partir da posição atual do agente
        objectivos.sort(key = self.__modelo_mundo.distancia)
        # Retorna apenas o primeiro elemento (o de menor distância) numa nova lista
        return objectivos[:1] 