from grammar.nonterminal import Nonterminal
from grammar.terminal import Terminal
import latex_formats as lf
from grammar.rules import rules



class ProjectSection(Nonterminal):
    latex = lf.latex["ProjectSection"]
    def __init__(self):
        super().__init__(rules[str(self)], ProjectSection.latex)
        self.ordered = True


class Project(Nonterminal):
    latex = lf.latex["Project"]
    def __init__(self):
        super().__init__(rules[str(self)], Project.latex)
        self.ordered = False
    
    def to_latex(self):
        return self.latex % tuple(child.to_latex() for child in self.children)
        

class ProjectDescription(Terminal):
    def __init__(self):
        self.value = None

    
class ProjectTools(Terminal):
    def __init__(self):
        self.parent_id = None
        self.value = None
    

class ProjectDate(Terminal):
    def __init__(self):
        self.parent_id = None
        self.value = None
    

class ProjectAchievements(Nonterminal):
    latex = lf.latex["ProjectAchievements"]
    def __init__(self):
        super().__init__(rules[str(self)], ProjectAchievements.latex)
        self.value = None
        self.ordered = True
    

class ProjectAchievementItem(Terminal):
    def __init__(self):
        self.value = None
    
    def to_latex(self):
        return r"\item "+super().to_latex()