
from grammar.nonterminal import Nonterminal
import latex_formats as lf
from collections import ChainMap

class Head(Nonterminal):
    rules = [
        (("Title", "PhoneEmail", "LinkedInGitHub", "GeographicalInfoField"), 1.0)
    ]
    latex = lf.latex["Head"]
    def __init__(self):
        super().__init__(Head.rules, Head.latex)

class Title(Nonterminal):
    rules = [
        (("FullName",), 1.0)
    ]
    latex = lf.latex["Title"]
    def __init__(self):
        super().__init__(Title.rules, Title.latex)



class PhoneEmail(Nonterminal):
    rules = [
       (("Phone", "Email"), 0.5),
       (("Email", "Phone"), 0.5),
    ]
    latex = lf.latex["PhoneEmail"]
    def __init__(self):
        super().__init__(PhoneEmail.rules, PhoneEmail.latex)

    def to_latex(self):
        if self.has_expanded():
            assert(len(self.children) == 2)
            # print(f"type: {self}")
            # print(f"children: {self.children}")
            c1, c2 = self.children
            values = ChainMap(c1.get(), c2.get())
            return self.latex % (values[str(c1)], values[str(c2)])
        else:
            raise Exception(f"{self} must be expanded first")

   


class LinkedInGitHub(Nonterminal):
    rules = [
        (("LinkedInField", "GitHubField"), 0.5),
        (("GitHubField", "LinkedInField"), 0.5),
    ]
    latex = lf.latex["LinkedInGitHub"]
    def __init__(self):
        super().__init__(LinkedInGitHub.rules, LinkedInGitHub.latex)

    def to_latex(self):
        if self.has_expanded():
            assert(len(self.children) == 2)
            return self.latex % (self.children[0].to_latex(), self.children[1].to_latex())
        else:
            raise Exception(f"{self} must be expanded first")


class LinkedInField(Nonterminal):
    rules = [
        (("LinkedIn",), 1.0)
    ]
    latex = lf.latex["LinkedInField"]
    def __init__(self):
        super().__init__(LinkedInField.rules, LinkedInField.latex)

    def to_latex(self):
        if self.has_expanded():
            values = self.children[0].value
            return self.latex % (values["href"], values[str(self.children[0])])
        else:
            raise Exception(f"{self} must be expanded first")


class GitHubField(Nonterminal):
    rules = [
        (("GitHub",), 1.0)
    ]
    latex = lf.latex["GitHubField"]
    def __init__(self):
        super().__init__(GitHubField.rules, GitHubField.latex)

    def to_latex(self):
        if self.has_expanded():
            assert(len(self.children) == 1)
            c = self.children[0]
            values = c.get()
            return self.latex % (values["href"], values[str(c)])
        else:
            raise Exception(f"{self} must be expanded first")

class GeographicalInfoField(Nonterminal):
    rules = [
        (("GeographicalInfo",), 1.0)
    ]
    latex = lf.latex["GeographicalInfoField"]
    def __init__(self):
        super().__init__(GeographicalInfoField.rules, GeographicalInfoField.latex)

    
