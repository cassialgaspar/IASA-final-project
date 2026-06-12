from ecr.Estimulo import Estimulo


"""(Classe) Representa o estímulo de um obstáculo que tem uma intensidade associada 

"""
class EstimuloObst(Estimulo):
    INTENS_OBST = 1

    def detectar(self, percepcao):
        return self.INTENS_OBST if percepcao.contacto_obst() else 0