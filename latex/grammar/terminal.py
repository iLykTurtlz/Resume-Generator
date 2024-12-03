# from roman import toRoman, fromRoman
from grammar.symbol import Symbol, SymbolFactory
from abc import ABC

class Terminal(Symbol, ABC):
    def expand(self):
        self.context = self
        return self
    
    def has_expanded(self):
        return True #the Terminal should be expanded at time of creation
    
    def to_latex(self):
        if self.value is not None:
            return self.value
        else:
            raise Exception(f"{self} needs to be assigned a value.")
        
    # def get(self):
    #     if self.has_expanded():
    #         return self.value
    #     else:
    #         raise Exception(f"{self} must be expanded first")






