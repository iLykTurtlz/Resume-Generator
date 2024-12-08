from grammar.terminal import Terminal
from grammar.nonterminal import Nonterminal
import random
import latex_formats as lf


class EducationSection(Nonterminal):
    rules = [
        (("Education",), 0.5),
        (("Education", "Education"), 0.5)
    ]
    latex = lf.latex["EducationSection"]

    def __init__(self):
        super().__init__(EducationSection.rules, EducationSection.latex)
        self.ordered = True

    # def expand(self):
    #     super().expand()
    #     self.context = {}
    #     for child in self.children:
    #         self.context[str(child)] = child.context
    #     return self


class CalPolyEducation(Nonterminal):
    rules = [
        (("CalPoly", "CalPolyEduGeographicalInfo", "EduDegreeName", "EduDate", "EduGPA"), 1.0)
    ]
    latex = lf.latex["Education"]

    def __init__(self):
        super().__init__(CalPolyEducation.rules, CalPolyEducation.latex)
        self.ordered = False

    def to_latex(self):
        if self.has_expanded():
            return self.latex % tuple(child.to_latex() for child in self.children)
        else:
            raise Exception(f"{self} must be expanded first")

class Education(Nonterminal):
    rules = [
        (("EduInstitution", "EduGeographicalInfo", "EduDegreeName", "EduDate", "EduGPA"), 1.0)
    ]
    latex = lf.latex["Education"]

    def __init__(self):
        super().__init__(Education.rules, Education.latex)
        self.ordered = False

    def to_latex(self):
        if self.has_expanded():
            return self.latex % tuple(child.to_latex() for child in self.children)
        else:
            raise Exception(f"{self} must be expanded first")



class CalPoly(Terminal):
    def __init__(self):
        self.value = None

    def expand(self):
        super().expand()
        self.value = "California Polytechnic State University, San Luis Obispo"
        return self

class EduInstitution(Terminal):
    def __init__(self):
        self.value = None
    # TODO: add other institutions
    def expand(self):
        super().expand()
        inst = random.choice(["Cuesta College"])
        self.value = inst
        return self


class EduGeographicalInfo(Terminal):
    def __init__(self):
        self.value = None

    def expand(self):
        """TODO: vary the info string formats"""
        super().expand()
        inst = random.choice(["Champaign, IL", "Paris, France", "Palo Alto, CA", "Berkeley, CA"])
        self.value = inst
        return self

class CalPolyEduGeographicalInfo(Terminal):
    def __init__(self):
        self.value = None

    def expand(self):
        """TODO: vary the info string formats"""
        super().expand()
        self.value = "San Luis Obispo, CA"
        return self


class EduDegreeName(Terminal):
    def __init__(self):
        self.value = None

    # def expand(self):
    #     super().expand()
    #     degree = random.choice(["B.S. Computer Science", "M.S. Computer Science"])
    #     self.value = degree
    #     return self


class EduDate(Terminal):
    def __init__(self):
        self.value = None

    # def expand(self):
    #     super().expand()
    #     month = random.choice(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    #     year = random.randint(2017, 2024)
    #     date = month + " " + str(year)
    #     self.value = date
    #     return self

class EduGPA(Terminal):
    def __init__(self):
        self.value = None

 
