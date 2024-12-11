from grammar.terminal import Terminal
from grammar.nonterminal import Nonterminal
import latex_formats as lf
from grammar.rules import rules


class ExperienceSection(Nonterminal):
    latex = lf.latex["ExperienceSection"]
    def __init__(self):
        super().__init__(rules[str(self)], ExperienceSection.latex)
        self.ordered = True

        
class Experience(Nonterminal):
    latex = lf.latex["Experience"]
    def __init__(self):
        super().__init__(rules[str(self)], Experience.latex)
        self.ordered = False
        
    def to_latex(self):
        if self.has_expanded():
            return self.latex % tuple(child.to_latex() for child in self.children)
        

class ExperienceTasks(Nonterminal):
    latex = lf.latex["ExperienceTasks"]
    def __init__(self):
        super().__init__(rules[str(self)], ExperienceTasks.latex)
        self.ordered = True
        
    def to_latex(self):
        if self.has_expanded():
            return self.latex % ("\n".join(child.to_latex() for child in self.children),)
    

class ExperienceTask(Terminal):
    def __init__(self):
        self.value = None
        
    def to_latex(self):
        return r'\item '+self.value


class CompanyName(Terminal):
    def __init__(self):
        self.value = None

    
class JobTitle(Terminal):
    def __init__(self):
        self.value = None

    
class DateRange(Terminal):
    def __init__(self):
        self.value = None