from abc import ABC

class ModeloPDM(ABC):

    def S(self):
        """returns a list of states"""

    def A(self, s):
        """returns a list of opertors"""

    def T(self, s, a, sn):
        """s is an a state, a is an operator, sn is a state and it returns a double"""

    def R(self, s, a, sn):
        """s is a state, a is an operator, sn is a state and it returns a double"""

    def suc(self, s, a):
        """s is a state, a is an operator and it returns a list of states"""