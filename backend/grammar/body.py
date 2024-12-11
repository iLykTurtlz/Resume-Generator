from grammar.nonterminal import Nonterminal
import latex_formats as lf
from grammar.rules import rules



class Body(Nonterminal):
    latex = lf.latex["Body"]
    def __init__(self):
        super().__init__(rules[str(self)], Body.latex)
        self.ordered = False

    def expand(self):
        super().expand()
        self.context = {}
        for child in self.children:
            self.context[str(child)] = child.context
        return self