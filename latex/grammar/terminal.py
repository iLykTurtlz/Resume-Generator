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




