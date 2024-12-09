from grammar.terminal import Terminal
from grammar.nonterminal import Nonterminal
import random
import latex_formats as lf


class ExperienceSection(Nonterminal):
    rules = [(("Experience",) * i, 1 / 3) for i in range(1, 4)]
    latex = lf.latex["ExperienceSection"]
    
    def __init__(self):
        super().__init__(ExperienceSection.rules, ExperienceSection.latex)
        self.ordered = True
        
class Experience(Nonterminal):
    rules = [
        (("CompanyName", "JobTitle", "DateRange", "GeographicalInfo", "ExperienceTasks"), 1.0)
    ]
    latex = lf.latex["Experience"]
    
    def __init__(self):
        super().__init__(Experience.rules, Experience.latex)
        self.ordered = False
        
    def to_latex(self):
        if self.has_expanded():
            return self.latex % tuple(child.to_latex() for child in self.children)
        else:
            raise Exception(f"{self} must be expanded first")
        
class ExperienceTasks(Nonterminal):
    rules = [
        (("ExperienceTask", "ExperienceTask", "ExperienceTask"), 0.4),
        (("ExperienceTask", "ExperienceTask", "ExperienceTask", "ExperienceTask"), 0.5),
        (("ExperienceTask", "ExperienceTask", "ExperienceTask", "ExperienceTask", "ExperienceTask"), 0.1),
    ]
    latex = lf.latex["ExperienceTasks"]
    def __init__(self):
        super().__init__(ExperienceTasks.rules, ExperienceTasks.latex)
        self.ordered = True
        
    def to_latex(self):
        if self.has_expanded():
            return self.latex % ("\n".join(child.to_latex() for child in self.children),)
    

class ExperienceTask(Terminal):
    def __init__(self):
        self.value = None
        
    # def expand(self):
    #     super().expand()
    #     self.value = "Did a thing"
    #     return self
    
    def to_latex(self):
        return r'\item '+self.value


class CompanyName(Terminal):
    # COMPANY_MAP = {
    #     "Google": "https://www.google.com",
    #     "Apple, Inc.": "https://www.apple.com"
    # }
    
    def __init__(self):
        self.value = None
        
    # def expand(self):
    #     super().expand()
    #     company = random.choice(list(self.COMPANY_MAP.keys()))
    #     self.value = r'''%s [\href{%s}{\faIcon{globe}}]''' % (company, self.COMPANY_MAP[company])
    #     return self
    
class JobTitle(Terminal):
    def __init__(self):
        self.value = None
        
    # def expand(self):
    #     super().expand()
    #     self.value = "Software Engineer"
    #     return self
    
class DateRange(Terminal):
    def __init__(self):
        self.value = None
        
    # def expand(self):
    #     super().expand()
    #     self.value = "June 2022 - Present"
    #     return self