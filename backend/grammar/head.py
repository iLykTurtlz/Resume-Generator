
from grammar.nonterminal import Nonterminal
from grammar.terminal import Terminal
from grammar.rules import rules
import latex_formats as lf




class Head(Nonterminal):
    latex = lf.latex["Head"]
    def __init__(self):
        super().__init__(rules[str(self)], Head.latex)
        self.ordered = False


class Title(Nonterminal):
    latex = lf.latex["Title"]
    def __init__(self):
        super().__init__(rules[str(self)], Title.latex)
        self.ordered = False


class PhoneEmail(Nonterminal):
    latex = lf.latex["PhoneEmail"]
    def __init__(self):
        super().__init__(rules[str(self)], PhoneEmail.latex)
        self.ordered = False

    def to_latex(self):
        if self.has_expanded():
            assert(len(self.children) == 2)
            c1, c2 = self.children
            return self.latex % (c1.to_latex(), c2.to_latex())
        else:
            raise Exception(f"{self} must be expanded first")

   


class LinkedInGitHub(Nonterminal):
    latex = lf.latex["LinkedInGitHub"]
    def __init__(self):
        super().__init__(rules[str(self)], LinkedInGitHub.latex)
        self.ordered = False

    def to_latex(self):
        if self.has_expanded():
            assert(len(self.children) == 2)
            return self.latex % (self.children[0].to_latex(), self.children[1].to_latex())
        else:
            raise Exception(f"{self} must be expanded first")


class LinkedInField(Nonterminal):
    latex = lf.latex["LinkedInField"]
    def __init__(self):
        super().__init__(rules[str(self)], LinkedInField.latex)
        self.ordered = False

    def to_latex(self):
        if self.has_expanded():
            assert(len(self.children) == 1)
            c = self.children[0]
            return self.latex % (c.to_latex(),)
        else:
            raise Exception(f"{self} must be expanded first")



class GitHubField(Nonterminal):
    latex = lf.latex["GitHubField"]
    def __init__(self):
        super().__init__(rules[str(self)], GitHubField.latex)
        self.ordered = False

    def to_latex(self):
        if self.has_expanded():
            assert(len(self.children) == 1)
            c = self.children[0]
            return self.latex % (c.to_latex(),)
        else:
            raise Exception(f"{self} must be expanded first")



class GeographicalInfoField(Nonterminal):
    latex = lf.latex["GeographicalInfoField"]
    def __init__(self):
        super().__init__(rules[str(self)], GeographicalInfoField.latex)
        self.ordered = False

    

class FullName(Terminal):
    def __init__(self):
        self.value = None
        self.ordered = False


class GitHub(Terminal):
    def __init__(self):
        self.value = None
        


class LinkedIn(Terminal):
    """TODO: generate LinkedIn fields in expand"""
    def __init__(self):
        self.value = None
    

class Phone(Terminal):
    def __init__(self):
        self.value = None


class Email(Terminal):
    def __init__(self):
        self.value = None


class GeographicalInfo(Terminal):
    def __init__(self):
        self.value = None