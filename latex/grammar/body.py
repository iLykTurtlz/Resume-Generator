from grammar.nonterminal import Nonterminal
import latex_formats as lf
from collections import ChainMap


class Body(Nonterminal):
    rules = [
        (("Education",), 1.0)
    ]
    latex = lf.latex["Body"]

    def __init__(self):
        super().__init__(Body.rules, Body.latex)


class Education(Nonterminal):
    rules = [
        (("Institution", "GeographicalInfoField", "DegreeName", "MMYYYY_Date", "GPA"), 1.0)
    ]
    latex = lf.latex["Education"]

    def __init__(self):
        super().__init__(Education.rules, Education.latex)


class Institution(Nonterminal):
    rules = [
        (("CalPoly",), 0.8),
        (("EduInstitution",), 0.2)
    ]
    latex = lf.latex["Institution"]
    def __init__(self):
        super().__init__(Institution.rules, Institution.latex)

class GeographicalInfoField(Nonterminal):
    rules = [
        (("EduGeographicalInfoField",), 1.0)
    ]
    latex = lf.latex["GeographicalInfoField"]
    def __init__(self):
        super().__init__(GeographicalInfoField.rules, GeographicalInfoField.latex)


class DegreeName(Nonterminal):
    rules = [
        (("EduDegreeName",), 1.0)
    ]
    latex = lf.latex["DegreeName"]
    def __init__(self):
        super().__init__(DegreeName.rules, DegreeName.latex)


class MMYYYY_Date(Nonterminal):
    rules = [
        (("EduDate",), 1.0)
    ]
    latex = lf.latex["MMYYYY_Date"]
    def __init__(self):
        super().__init__(MMYYYY_Date.rules, MMYYYY_Date.latex)


class GPA(Nonterminal):
    rules = [
        (("EduGPA",), 1.0)
    ]
    latex = lf.latex["GPA"]
    def __init__(self):
        super().__init__(GPA.rules, GPA.latex)


# class PhoneEmail(Nonterminal):
#     rules = [
#         (("Phone", "Email"), 0.5),
#         (("Email", "Phone"), 0.5),
#     ]
#     latex = lf.latex["PhoneEmail"]
#
#     def __init__(self):
#         super().__init__(PhoneEmail.rules, PhoneEmail.latex)
#
#     def to_latex(self):
#         if self.has_expanded():
#             assert (len(self.children) == 2)
#             # print(f"type: {self}")
#             # print(f"children: {self.children}")
#             c1, c2 = self.children
#             values = ChainMap(c1.get(), c2.get())
#             return self.latex % (values[str(c1)], values[str(c2)])
#         else:
#             raise Exception(f"{self} must be expanded first")

