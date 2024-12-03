from grammar.nonterminal import Nonterminal
from grammar.terminal import Terminal
import latex_formats as lf

class SelfSummarySection(Nonterminal):
    rules = [
        (("SelfSummary",), 1.0)
    ]
    latex = lf.latex["SelfSummarySection"]
    def __init__(self):
        super().__init__(SelfSummarySection.rules, SelfSummarySection.latex)
        self.ordered = False

class SelfSummary(Terminal):
    def __init__(self):
        self.value = None

