from grammar.nonterminal import Nonterminal
from grammar.terminal import Terminal
import latex_formats as lf



class ProjectSection(Nonterminal):
    rules = [
        (("Project",), 0.1),
        (("Project", "Project"), 0.2),
        (("Project", "Project", "Project"), 0.4),
        (("Project", "Project", "Project", "Project"), 0.3),
    ]
    latex = lf.latex["ProjectSection"]
    def __init__(self):
        super().__init__(ProjectSection.rules, ProjectSection.latex)
        self.ordered = True
        # self.context[str(self)] = {}
        
    # def expand(self):
    #     super().expand()
    #     ProjectSection.data_factory.generate(self.context)
    #     return self


    # def expand(self):
    #     super().expand()
    #     self.context = [child.context for child in self.children]
    #     # for child in self.children:
    #     #     if isinstance(child, Nonterminal):
    #     #         self.context[child.id] = child.context
    #     #     else:
    #     #         self.context[child.id] = child
    #         # ctx = {}
    #         # self.context[child.id] = child.context
    #         # child.context = ctx
    #     ProjectSection.data_factory.generate(self.context)
    #     # print(self.context)
    #     # self.debug()
    #     return self
    
    
    # def debug(self):
    #     def dfs(d):
    #         if isinstance(d, Terminal):
    #             print(f"{d}: {d.value}")
    #         elif isinstance(d, dict):
    #             for e in d.values():
    #                 dfs(e)
    #         elif isinstance(d, list):
    #             for e in d:
    #                 dfs(e)

    #     dfs(self.context)


class Project(Nonterminal):
    # count = 0
    rules = [
        (("ProjectDescription", "ProjectTools", "ProjectDate", "ProjectAchievements"), 1.0),
        
    ]
    latex = lf.latex["Project"]
    def __init__(self):
        super().__init__(Project.rules, Project.latex)
        self.ordered = False
        # Project.count += 1
        # self.id = f"{self}_{Project.count}"


    # def expand(self):
    #     super().expand()
    #     self.context = {}
    #     for child in self.children:
    #         if isinstance(child, Nonterminal):
    #             self.context[str(child)] = child.context
    #         else:
    #             self.context[str(child)] = child
    #     return self
    
    def to_latex(self):
        # print(tuple(child.to_latex() for child in self.children))
        return self.latex % tuple(child.to_latex() for child in self.children)

        
'''
Context is
{

    "Experiences" : [
        
    ]

    "Projects" : {
        "number_of_projects":2,
        "Project_I": {
            "ProjectDescription": obj,
            "ProjectTools": obj,
            "ProjectDate": obj,
            "ProjectAchievements": [obj]
        },
        "Project_II": {
            ...
        },
    }

}
'''    
        
    

class ProjectDescription(Terminal):
    # count = 0
    def __init__(self):
        # ProjectDescription.count += 1
        # self.id = f"{self}_{toRoman(ProjectDescription.count)}"
        # self.parent_id = None
        self.value = None

    # def add_to_context(self, parent_id):
    #     self.parent_id = parent_id
    #     self.context[self.parent_id][str(self)] = self #adding self allows self.value to be updated by the DataFactory

    # def expand(self):
    #     return self
    
class ProjectTools(Terminal):
    def __init__(self):
        self.parent_id = None
        self.value = None
    
    # def add_to_context(self, parent_id):
    #     self.parent_id = parent_id
    #     self.context[self.parent_id][str(self)] = self

    # def expand(self):
    #     return self

class ProjectDate(Terminal):
    def __init__(self):
        self.parent_id = None
        self.value = None
    
    # def add_to_context(self, parent_id):
    #     self.parent_id = parent_id
    #     self.context[self.parent_id][str(self)] = self

    # def expand(self):
    #     return self
    

    
class ProjectAchievements(Nonterminal):
    rules = [
        (("ProjectAchievementItem",), 0.2),
        (("ProjectAchievementItem","ProjectAchievementItem"), 0.5),
        (("ProjectAchievementItem","ProjectAchievementItem","ProjectAchievementItem"), 0.3),
    ]
    latex = lf.latex["ProjectAchievements"]
    def __init__(self):
        self.value = None
        self.ordered = True
    
    # def expand(self):
    #     super().expand()
    #     self.context = [child for child in self.children]
    #     return self
        
    # def to_latex(self):
    #     if self.has_expanded():
    #         return self.latex % ("\n".join(r"\item "+child.to_latex() for child in self.children),)
    #     else:
    #         raise Exception(f"{self} must be expanded first")


    #.expand is default
    
class ProjectAchievementItem(Terminal):
    def __init__(self):
        self.value = None
    
    # def expand(self):
    #     return self
    
    def to_latex(self):
        return r"\item "+super().to_latex()





'''
\resumeProject
  {Project A: [Brief Description]}
  {Tools: [List of tools and technologies used]}
  {Month Year - Month Year}
  %%{{}[\href{https://github.com/your-username/project-a}{\textcolor{darkblue}{\faGithub}}]}
\resumeItemListStart
  \item Developed [specific feature/system] for [specific purpose]
  \item Implemented [specific technology] for [specific goal], achieving [specific result]
  \item Created [specific component], ensuring [specific benefit]
  \item Applied [specific method] to analyze [specific aspect]
\resumeItemListEnd
'''