# from __future__ import annotations
import random
from roman import toRoman, fromRoman
from grammar.symbol import Symbol, SymbolFactory
import latex_formats as lf
# from collections import ChainMap


class Nonterminal(Symbol):
    def __init__(self, rules, latex):
        self.rules = rules
        self.latex = latex
        self.children = None

    def expand(self):
        # print(f"rules: {self.rules}")
        child_types = random.choices(*zip(*self.rules))[0]
        self.children = [child.expand() for child in SymbolFactory.create_instances(child_types)]
        return self

    def has_expanded(self):
        return self.children is not None
    
    def to_latex(self):
        if self.has_expanded():
            return self.latex % ("\n".join(child.to_latex() for child in self.children),)
        else:
            raise Exception(f"{self} must be expanded first")
    


class S(Nonterminal):
    rules = [
        # (("Head", "Body"), 1.0),
        # (("Head", "Body", "Footer"), 0.0)
        (("Head",), 1.0)
    ]
    latex = lf.latex["S"]

    def __init__(self):
        # instance attributes
        super().__init__(S.rules, S.latex)
    
    


class Body(Nonterminal):
    rules = [
        (("Experience"), 1.0)
    ]
    def __init__(self):
        super().__init__(Body.rules)


    #sequence of subheadings

class Experience(Nonterminal):
    rules = []
    latex = '''
        \\section{\\textbf{Experience}}
        \\vspace{-0.4mm}
        \resumeSubHeadingListStart
            %s
        \resumeSubHeadingListEnd
        \vspace{-6mm}
    '''
    # ExperienceSubHeadings
    #latex % expsubheading.to_latex()
    def __init__(self):
        super().__init__(Experience.rules)


class ExperienceSubheading(Nonterminal):
    count = 0
    rules = [
        (("ExperienceDetails", "ExperienceItemList"), 1.0)
    ]

    #ExpSub -> JobDeets(Term) JobAchievements(Nonterm)
    #JobAchievements -> item *

    latex = '''
         \resumeSubheading
            {{Company A}}{City, Country}
            {Job Title A}{Month Year - Month Year}
            \resumeItemListStart
                \item Developed [specific achievement] achieving [specific metric] in [specific area]
                \item Implemented [technology/method], enhancing [specific aspect] by [specific percentage]
                \item Conducted analysis on [specific data], identifying [key findings]
                \item Presented findings at [specific event], receiving [specific recognition]
            \resumeItemListEnd 
    '''
    
    def __init__(self):
        ExperienceSubheading.count += 1
        self.id = ExperienceSubheading.count

    #f"company{toRoman(self.id)}"
        

    




class Footer(Nonterminal):
    pass




        
    