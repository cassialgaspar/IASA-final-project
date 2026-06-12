from pee.prof.ProcuraProfundidade import ProcuraProfundidade
from pee.larg.ProcuraLargura import ProcuraLargura
from pee.prof.ProcuraProfIter import ProcuraProfIter
from pee.prof.ProcuraProfLim import ProcuraProfLim
from pee.melhor_prim.ProcuraCustoUnif import ProcuraCustoUnif
from pee.melhor_prim.ProcuraAA import ProcuraAA
from pee.melhor_prim.ProcuraSof import ProcuraSof
from pee.melhor_prim.ProcuraInformada import ProcuraInformada

from mod_prob.problema_contagem import ProblemaContagem
from mod_prob.heuristica_contagem import HeuristicaContagem





"""(Constante) Conjunto das instâncias de todos os mecanismos de procura concretos, em que cada um encapsula uma fronteira 
e uma estratégia de controlo específica (ex: LIFO para Profundidade, FIFO para Largura, Avaliadores para as Melhor-Primeiro).
"""

MECANISMOS_PROCURA = [
    ProcuraProfundidade(),
    ProcuraLargura(),
    ProcuraProfIter(),
    ProcuraCustoUnif(),
    ProcuraProfLim(),
    ProcuraAA(),
    ProcuraSof()
]


VALOR_INICIAL = 0 #corresponde ao estado inicial e à raíz da árvore de procura
VALOR_FINAL = 8 # condição do teste de objetivo
INCREMENTOS = [1,2,3]



"""
(Função) Teste 3 - a solução do problema de contagem usando os vários mecanismos de procura implementados.

    O mesmo problema, ao ser solucionado com diferentes estratégias automáticas, produz soluções 
    (percursos) variadas dependendo da implementação de cada um.
    
    @param valor_inicial: Estado inicial.
    @param valor_final: Objetivo.
    @param incrementos: Operadores que geram os estados sucessores.
    @param mecanismos_procura: Mecanismos a testar.
"""
def teste_contagem(valor_inicial, valor_final, incrementos, mecanismos_procura):
    print(f"Contagem de {valor_inicial} a {valor_final} com incrementos {incrementos}")

    # criação do problema (Instancia do problema com o estado inicial, o teste de objetivo e os incrementos)
    problema = ProblemaContagem(valor_inicial, valor_final, incrementos)

    for mec_proc in mecanismos_procura:
        
        
        # As procuras informadas (AA e Sof) necessitam de conhecimento do domínio, desse modo caso seja um destes mecanismos,
        #criamos e passamos a Heurística como parâmetro extra.
        if isinstance(mec_proc, ProcuraInformada):
            heuristica = HeuristicaContagem(valor_final)
            solucao = mec_proc.procurar(problema, heuristica)

        else:
            # Mecanismos de custo uniforme recebem apenas o problema
            # o método 'procurar()' começa o processo, definido na classe MecanismoProcura.
            solucao = mec_proc.procurar(problema)

        # Se a solução for != None, mostra os detalhes da solução.
        if solucao:
            print()
            # nome da classe do mecanismo que acabou de executar
            print(mec_proc.__class__.__name__)
            
            # Percorre a solução e extrai a sequência de ações que geraram as transições de estado do início até ao objetivo.
            print("Solução", [passo.operador.incremento for passo in solucao])
            
            # número de nós no percurso
            print("Dimensão ", solucao.dimensao)
            
            # custo total acumulado da solução encontrada
            print("Custo ", solucao.custo)
        
        else:
            print()
            print(mec_proc.__class__.__name__, "não encontrou solução")


if __name__ == "__main__":
    teste_contagem(VALOR_INICIAL, VALOR_FINAL, INCREMENTOS, MECANISMOS_PROCURA)