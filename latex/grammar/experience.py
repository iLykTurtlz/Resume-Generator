from grammar.terminal import Terminal
from grammar.nonterminal import Nonterminal
import random
import latex_formats as lf


class ExperienceSection(Nonterminal):
    rules = [(("Experience",) * i, 1 / 3) for i in range(1, 4)]
    latex = lf.latex["ExperienceSection"]
    
    def __init__(self):
        super().__init__(ExperienceSection.rules, ExperienceSection.latex)
        
class Experience(Nonterminal):
    rules = [
        (("CompanyName", "JobTitle", "DateRange", "GeographicalInfo", "ExperienceTasks"), 1.0)
    ]
    latex = lf.latex["Experience"]
    
    def __init__(self):
        super().__init__(Experience.rules, Experience.latex)
        
    def to_latex(self):
        if self.has_expanded(): 
            return self.latex % tuple([child.to_latex() for child in self.children])
        else:
            raise Exception(f"{self} must be expanded first")
        
class ExperienceTasks(Nonterminal):
    def __init__(self):
        super().__init__(
            [(('ExperienceTask',) * j, 0.2) for j in range(1, 5)], r'%s'
        )
        
    def to_latex(self):
        if self.has_expanded():
            return "\n".join([f"\\item {child.to_latex()}" for child in self.children])
    
class ExperienceTask(Terminal):
    def __init__(self):
        self.value = None
        
    def expand(self):
        self.value = "Did a thing"
        return self

class CompanyName(Terminal):
    COMPANY_MAP = {
        "Google": "https://www.google.com",
        "Apple, Inc.": "https://www.apple.com"
    }
    
    def __init__(self):
        self.value = None
        
    def expand(self):
        company = random.choice(list(self.COMPANY_MAP.keys()))
        self.value = r'''%s [\href{%s}{\faIcon{globe}}]''' % (company, self.COMPANY_MAP[company])
        return self
    
class JobTitle(Terminal):
    def __init__(self):
        self.value = None
        
    def expand(self):
        self.value = "Software Engineer"
        return self
    
class DateRange(Terminal):
    def __init__(self):
        self.value = None
        
    def expand(self):
        self.value = "June 2022 - Present"
        return self