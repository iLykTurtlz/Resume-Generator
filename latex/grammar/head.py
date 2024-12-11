
from grammar.nonterminal import Nonterminal
from grammar.terminal import Terminal
from grammar.rules import rules
import latex_formats as lf




class Head(Nonterminal):
    # rules = [
    #     (("Title", "PhoneEmail", "LinkedInGitHub", "GeographicalInfoField"), 1.0)
    # ]
    latex = lf.latex["Head"]
    def __init__(self):
        super().__init__(rules[str(self)], Head.latex)
        self.ordered = False


class Title(Nonterminal):
    # rules = [
    #     (("FullName",), 1.0)
    # ]
    latex = lf.latex["Title"]
    def __init__(self):
        super().__init__(rules[str(self)], Title.latex)
        self.ordered = False



class PhoneEmail(Nonterminal):
    # rules = [
    #    (("Phone", "Email"), 0.5),
    #    (("Email", "Phone"), 0.5),
    # ]
    latex = lf.latex["PhoneEmail"]
    def __init__(self):
        super().__init__(rules[str(self)], PhoneEmail.latex)
        self.ordered = False

    def to_latex(self):
        if self.has_expanded():
            assert(len(self.children) == 2)
            # print(f"type: {self}")
            # print(f"children: {self.children}")
            c1, c2 = self.children
            return self.latex % (c1.to_latex(), c2.to_latex())
        else:
            raise Exception(f"{self} must be expanded first")

   


class LinkedInGitHub(Nonterminal):
    # rules = [
    #     (("LinkedInField", "GitHubField"), 0.5),
    #     (("GitHubField", "LinkedInField"), 0.5),
    # ]
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
    # rules = [
    #     (("LinkedIn",), 1.0)
    # ]
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
    # rules = [
    #     (("GitHub",), 1.0)
    # ]
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
    # rules = [
    #     (("GeographicalInfo",), 1.0)
    # ]
    latex = lf.latex["GeographicalInfoField"]
    def __init__(self):
        super().__init__(rules[str(self)], GeographicalInfoField.latex)
        self.ordered = False

    

class FullName(Terminal):
    def __init__(self):
        self.value = None
        self.ordered = False

    # def expand(self):
    #     super().expand()
    #     self.value = FullName.data_factory.generate(None)
    #     return self

    # def expand(self):
    #     """TODO: Replace with name generator module"""
    #     letters = 'abcdefghijklmnopqrstuvwxyz'
    #     fn_length = random.randint(5,10)
    #     ln_length = random.randint(5,15)
    #     self.value = {
    #         "FullName" : "".join(random.choice(letters) for _ in range(fn_length)).capitalize() + " " + \
    #             "".join(random.choice(letters) for _ in range(ln_length)).capitalize()
              
    #     }
    #     return self

class GitHub(Terminal):
    def __init__(self):
        self.value = None

    # def expand(self):
    #     """TODO: 2 options
    #     1. replace each field with a call to an info generator
    #     2. register the class in a central DataFactory that generates the fields once it has ALL instances
    #     Option 2 is better for interdependent fields.
    #     """
    #     super().expand()
    #     self.value = "sweetDude"
    #     return self
        


class LinkedIn(Terminal):
    """TODO: generate LinkedIn fields in expand"""
    def __init__(self):
        self.value = None
    
    # def expand(self):
    #     super().expand()
    #     self.value = "anastasia-beaverhousen-a4a06969"
    #     return self
         
         


class Phone(Terminal):
    def __init__(self):
        self.value = None



class Email(Terminal):
    def __init__(self):
        self.value = None

    # def expand(self):
    #     super().expand()
    #     self.value = "sweetDude@calpoly.edu"
    #     return self
    


class GeographicalInfo(Terminal):
    def __init__(self):
        self.value = None

    # def expand(self):
    #     super().expand()
    #     """TODO: vary the info string formats"""
    #     self.value = "San Luis Obispo, CA"
    #     return self
