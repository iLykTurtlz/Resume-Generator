import random
from grammar.symbol import Symbol, SymbolFactory
from grammar.rules import rules
import latex_formats as lf
from abc import ABC



class Nonterminal(Symbol, ABC):
    def __init__(self, rules, latex):
        self.rules = rules
        self.latex = latex
        self.children = None

    def expand(self):
        child_types = random.choices(*zip(*self.rules))[0]
        self.children = [child.expand() for child in SymbolFactory.create_instances(child_types)]
        try:
            if self.ordered:
                self.context = [child.context for child in self.children]
            else:
                self.context = {str(child): child.context for child in self.children}
        except AttributeError as e:
            print(f"{self} does not have a self.ordered attribute.")
            raise e
        return self

    def has_expanded(self):
        return self.children is not None
    
    #sometimes need to override this
    def to_latex(self):
        print(f"{self}")
        if self.has_expanded():
            return self.latex % ("\n".join(child.to_latex() for child in self.children),)
        else:
            raise Exception(f"{self} must be expanded first")
    


class S(Nonterminal):
    latex = lf.latex["S"]
    def __init__(self):
        super().__init__(rules[str(self)], S.latex)
        self.ordered = False