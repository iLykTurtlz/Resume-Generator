from grammar.nonterminal import Nonterminal
import latex_formats as lf



class Body(Nonterminal):
    rules = [
        #(("Education", "ExperienceSection"), 1.0)
        (("SelfSummarySection", "EducationSection", "ExperienceSection", "ProjectSection", "SkillsSection"), 1.0)
        # (("EducationSection",), 1.0)
    ]
    latex = lf.latex["Body"]

    def __init__(self):
        super().__init__(Body.rules, Body.latex)
        self.ordered = False

    def expand(self):
        super().expand()
        self.context = {}
        for child in self.children:
            self.context[str(child)] = child.context
        return self

