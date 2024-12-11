from grammar.terminal import Terminal
from grammar.nonterminal import Nonterminal
import latex_formats as lf
from grammar.rules import rules


class EducationSection(Nonterminal):
    latex = lf.latex["EducationSection"]

    def __init__(self):
        super().__init__(rules[str(self)], EducationSection.latex)
        self.ordered = True


class Education(Nonterminal):
    latex = lf.latex["Education"]

    def __init__(self):
        super().__init__(rules[str(self)], Education.latex)
        self.ordered = False

    def to_latex(self):
        if self.has_expanded():
            return self.latex % tuple(child.to_latex() for child in self.children)
        else:
            raise Exception(f"{self} must be expanded first")


class CalPoly(Terminal):
    def __init__(self):
        self.value = None


class EduInstitution(Terminal):
    def __init__(self):
        self.value = None


class EduGeographicalInfo(Terminal):
    def __init__(self):
        self.value = None


class CalPolyEduGeographicalInfo(Terminal):
    def __init__(self):
        self.value = None


class EduDegreeName(Terminal):
    def __init__(self):
        self.value = None


class EduDate(Terminal):
    def __init__(self):
        self.value = None


class EduGPA(Terminal):
    def __init__(self):
        self.value = None

 
