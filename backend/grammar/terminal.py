from grammar.symbol import Symbol
from abc import ABC

class Terminal(Symbol, ABC):
    def expand(self):
        self.context = self
        return self
    
    def has_expanded(self):
        return True
    
    def to_latex(self):
        if self.value is not None:
            return self.value
        else:
            raise Exception(f"{self} needs to be assigned a value.")




