from grammar.nonterminal import Nonterminal
from grammar.terminal import Terminal
from grammar.rules import rules
import latex_formats as lf

class SelfSummarySection(Nonterminal):
    latex = lf.latex["SelfSummarySection"]
    def __init__(self):
        super().__init__(rules[str(self)], SelfSummarySection.latex)
        self.ordered = False


class SelfSummary(Terminal):
    def __init__(self):
        self.value = None

