from grammar.nonterminal import Nonterminal
from grammar.terminal import Terminal
import latex_formats as lf

class SkillsSection(Nonterminal):
    rules = ()
    latex = lf.latex['Skills']
    def __init__(self):
        super().__init__(SkillsSection.rules, SkillsSection.latex)
        self.context = {}
    #default expand, to_latex
        
        
class ProgrammingLanguageSkills(Nonterminal):
    rules = [
        (("ProgrammingLanguage",), 0.1),
        (("ProgrammingLanguage", "ProgrammingLanguage"), 0.2),
        (("ProgrammingLanguage", "ProgrammingLanguage", "ProgrammingLanguage"), 0.3),
        (("ProgrammingLanguage", "ProgrammingLanguage", "ProgrammingLanguage", "ProgrammingLanguage"), 0.4)
    ]
    latex = lf.latex['ProgrammingLanguageSkills']
    def __init__(self):
        super().__init__(ProgrammingLanguageSkills.rules, ProgrammingLanguageSkills.latex)
    
    def to_latex(self):
        return self.latex % (", ".join(child.to_latex() for child in self.children),)
    

class WebTechnologySkills(Nonterminal):
    rules = [
        (("WebTechnology",), 0.1),
        (("WebTechnology", "WebTechnology"), 0.2),
        (("WebTechnology", "WebTechnology", "WebTechnology"), 0.3),
        (("WebTechnology", "WebTechnology", "WebTechnology", "WebTechnology"), 0.4)
    ]
    latex = lf.latex['WebTechnologySkills']
    def __init__(self):
        super().__init__(WebTechnologySkills.rules, WebTechnologySkills.latex)
    
    def to_latex(self):
        return self.latex % (", ".join(child.to_latex() for child in self.children),)
    

class DatabaseSystemSkills(Nonterminal):
    rules = [
        (("DatabaseSystem",), 0.1),
        (("DatabaseSystem", "DatabaseSystem"), 0.2),
        (("DatabaseSystem", "DatabaseSystem", "DatabaseSystem"), 0.3),
        (("DatabaseSystem", "DatabaseSystem", "DatabaseSystem", "DatabaseSystem"), 0.4)
    ]
    latex = lf.latex['DatabaseSystemSkills']
    def __init__(self):
        super().__init__(DatabaseSystemSkills.rules, DatabaseSystemSkills.latex)
    
    def to_latex(self):
        return self.latex % (", ".join(child.to_latex() for child in self.children),)
    

class DataScienceMLSkills(Nonterminal):
    rules = [
        (("DataScienceML",), 0.1),
        (("DataScienceML", "DataScienceML"), 0.2),
        (("DataScienceML", "DataScienceML", "DataScienceML"), 0.3),
        (("DataScienceML", "DataScienceML", "DataScienceML", "DataScienceML"), 0.4)
    ]
    latex = lf.latex['DataScienceMLSkills']
    def __init__(self):
        super().__init__(DataScienceMLSkills.rules, DataScienceMLSkills.latex)
    
    def to_latex(self):
        return self.latex % (", ".join(child.to_latex() for child in self.children),)
    

class CloudSkills(Nonterminal):
    rules = [
        (("Cloud",), 0.1),
        (("Cloud", "Cloud"), 0.2),
        (("Cloud", "Cloud", "Cloud"), 0.3),
        (("Cloud", "Cloud", "Cloud", "Cloud"), 0.4)
    ]
    latex = lf.latex['CloudSkills']
    def __init__(self):
        super().__init__(CloudSkills.rules, CloudSkills.latex)
    
    def to_latex(self):
        return self.latex % (", ".join(child.to_latex() for child in self.children),)


class DevOpsSkills(Nonterminal):
    rules = [
        (("DevOps",), 0.1),
        (("DevOps", "DevOps"), 0.2),
        (("DevOps", "DevOps", "DevOps"), 0.3),
        (("DevOps", "DevOps", "DevOps", "DevOps"), 0.4)
    ]
    latex = lf.latex['DevOpsSkills']
    def __init__(self):
        super().__init__(DevOpsSkills.rules, DevOpsSkills.latex)
    
    def to_latex(self):
        return self.latex % (", ".join(child.to_latex() for child in self.children),)
    

class OtherSkills(Nonterminal):
    rules = [
        (("Other",), 0.1),
        (("Other", "Other"), 0.2),
        (("Other", "Other", "Other"), 0.3),
        (("Other", "Other", "Other", "Other"), 0.4)
    ]
    latex = lf.latex['OtherSkills']
    def __init__(self):
        super().__init__(OtherSkills.rules, OtherSkills.latex)
    
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
    





    