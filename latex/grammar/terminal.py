# from roman import toRoman, fromRoman
from grammar.symbol import Symbol, SymbolFactory
from abc import ABC, abstractmethod

class Terminal(Symbol, ABC):
    @abstractmethod
    def expand(self):
        raise NotImplementedError("You must implement this method.")
    
    def has_expanded(self):
        return self.value is not None
    
    def to_latex(self):
        return self.value
 
        
    # def get(self):
    #     if self.has_expanded():
    #         return self.value
    #     else:
    #         raise Exception(f"{self} must be expanded first")






