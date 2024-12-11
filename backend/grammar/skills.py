from grammar.nonterminal import Nonterminal
from grammar.terminal import Terminal
import latex_formats as lf
from grammar.rules import rules

class SkillsSection(Nonterminal):
    latex = lf.latex['Skills']
    def __init__(self):
        super().__init__(rules[str(self)], SkillsSection.latex)
        self.ordered = False
        
        
class ProgrammingLanguageSkills(Nonterminal):
    latex = lf.latex['ProgrammingLanguageSkills']
    def __init__(self):
        super().__init__(rules[str(self)], ProgrammingLanguageSkills.latex)
        self.ordered = True
    
    def to_latex(self):
        return self.latex % (", ".join(child.to_latex() for child in self.children),)
    

class WebTechnologySkills(Nonterminal):
    latex = lf.latex['WebTechnologySkills']
    def __init__(self):
        super().__init__(rules[str(self)], WebTechnologySkills.latex)
        self.ordered = True
    
    def to_latex(self):
        return self.latex % (", ".join(child.to_latex() for child in self.children),)
    

class DatabaseSystemSkills(Nonterminal):
    latex = lf.latex['DatabaseSystemSkills']
    def __init__(self):
        super().__init__(rules[str(self)], DatabaseSystemSkills.latex)
        self.ordered = True
    
    def to_latex(self):
        return self.latex % (", ".join(child.to_latex() for child in self.children),)
    

class DataScienceMLSkills(Nonterminal):
    latex = lf.latex['DataScienceMLSkills']
    def __init__(self):
        super().__init__(rules[str(self)], DataScienceMLSkills.latex)
        self.ordered = True
    
    def to_latex(self):
        return self.latex % (", ".join(child.to_latex() for child in self.children),)
    

class CloudSkills(Nonterminal):
    latex = lf.latex['CloudSkills']
    def __init__(self):
        super().__init__(rules[str(self)], CloudSkills.latex)
        self.ordered = True
    
    def to_latex(self):
        return self.latex % (", ".join(child.to_latex() for child in self.children),)


class DevOpsSkills(Nonterminal):
    latex = lf.latex['DevOpsSkills']
    def __init__(self):
        super().__init__(rules[str(self)], DevOpsSkills.latex)
        self.ordered = True
    
    def to_latex(self):
        return self.latex % (", ".join(child.to_latex() for child in self.children),)
    

class ProgrammingLanguage(Terminal):
    def __init__(self):
        self.value = None

    
class WebTechnology(Terminal):
    def __init__(self):
        self.value = None
    

class DatabaseSystem(Terminal):
    def __init__(self):
        self.value = None
    

class DataScienceML(Terminal):
    def __init__(self):
        self.value = None


class Cloud(Terminal):
    def __init__(self):
        self.value = None


class DevOps(Terminal):
    def __init__(self):
        self.value = None


class Other(Terminal):
    def __init__(self):
        self.value = None