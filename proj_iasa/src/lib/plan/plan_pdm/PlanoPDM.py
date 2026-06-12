from plan.Plano import Plano

"""(Classe) Representa a solução planeada criada por um Processo de Decisão de Markov.
    Em sistemas não determinísticos, como é o caso, a solução planeada não é um simples percurso entre 
    situações, mas sim um modelo de decisão que usa a política ótima (a ação a realizar) com a utilidade 
    a longo prazo calculada para todo o espaço de estados. Deste modo, especifica a interface 'Plano', 
    permitindo que o Agente atue sem ter de saber as probabilidades relacionadas com a decisão que foi tomada.
    """
class PlanoPDM(Plano):

    """
    (Método) Construtor. Encapsula a utilidade e política em atributos privados.
        
        @param utilidade: Dicionário que associa cada Estado ao seu valor em longo prazo.
        @param politica: Dicionário que associa cada Estado à respectiva Accao óptima a tomar.
    """
    def __init__(self,utilidade, politica):
        self.__politica = politica
        self.__utilidade = utilidade

        """
    (Método) Devolve a próxima ação a executar perante um dado estado.
        Faz o comportamento do agente ao verificar a política ótima 
        A escolha de uso do .get do dicionário (política) deve-se ao facto que há garantia, se 
        o estado não existir no mapeamento, a função devolve 'None', em vez de criar um erro, 
        o que é essencial para o funcionamento contínuo do agente.
        
        @param estado: O estado actual em que o agente se encontra.
        @return: O operador (ação) a executar (ou Nulo).
    """
    def obter_accao(self, estado):
        """returns an operator"""
        return self.__politica.get(estado)
    

    """
    (Método) Mostra a informação definida do plano ao utilizador através de uma interface gráfica.
        Permite visualizar as setas direcionais da política e os valores de utilidade) da simulação.
        Aplica o método items() do Python para extrair de forma iterativa e imediata os pares chave-valor dos dicionários.
        
        @param vista: A componente que renderiza o ambiente.
    """
    def mostrar(self, vista):
        
        if self.__politica: # validação para garantir que existe uma política calculada
            
            # itera sobre os pares (estado, valor de utilidade)
            for estado, valor in self.__utilidade.items():
                vista.mostrar_valor_posicao(estado.posicao, valor)
        
            # itera sobre os pares (estado, ação óptima)
            for estado, accao in self.__politica.items():
                vista.mostrar_vector(estado.posicao, accao.ang) # vetor com angulo correspondente à ação