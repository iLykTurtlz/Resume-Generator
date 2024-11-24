from grammar.nonterminal import Nonterminal
from grammar.terminal import Terminal
import latex_formats as lf
from roman import toRoman, fromRoman
from data_factory import ProjectDataFactory

class ProjectSection(Nonterminal):
    data_factory = ProjectDataFactory()
    rules = [
        (("Project",), 0.1),
        (("Project", "Project"), 0.2),
        (("Project", "Project", "Project"), 0.4),
        (("Project", "Project", "Project", "Project"), 0.3),
    ]
    latex = lf.latex["ProjectSection"]
    def __init__(self):
        super().__init__(ProjectSection.rules, ProjectSection.latex)
        #self.context = {}
        self.context[str(self)] = {}
        

    def expand(self):
        super().expand()
        self.context["number_of_projects"] = len(self.children)
        ProjectSection.data_factory.generate(self.context)
        return self


class Project(Nonterminal):
    count = 0
    rules = [
        (("ProjectDescription", "ProjectTools", "ProjectDate", "ProjectAchievements"), 0.5),
        
    ]
    latex = lf.latex["Project"]
    def __init__(self):
        super().__init__(Project.rules, Project.latex)
        Project.count += 1
        self.id = f"{self}_{Project.count}"

    def expand(self):
        self.context[self.id] = {}
        super().expand()
        for child in self.children:
            child.add_to_context(self.context, self.id)
        return self

        
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
        ProjectDescription.count += 1
        # self.id = f"{self}_{toRoman(ProjectDescription.count)}"
        self.parent_id = None
        self.value = None

    def add_to_context(self, parent_id):
        self.parent_id = parent_id
        self.context[self.parent_id][str(self)] = self #adding self allows self.value to be updated by the DataFactory

    def expand(self):
        return self
    
class ProjectTools(Terminal):
    def __init__(self):
        self.parent_id = None
        self.value = None
    
    def add_to_context(self, parent_id):
        self.parent_id = parent_id
        self.context[self.parent_id][str(self)] = self

    def expand(self):
        return self

class ProjectDate(Terminal):
    def __init__(self):
        self.parent_id = None
        self.value = None
    
    def add_to_context(self, parent_id):
        self.parent_id = parent_id
        self.context[self.parent_id][str(self)] = self

    def expand(self):
        return self
    

    
class ProjectAchievements(Nonterminal):
    rules = [
        (("ProjectAchievementItem",), 0.2),
        (("ProjectAchievementItem","ProjectAchievementItem"), 0.5),
        (("ProjectAchievementItem","ProjectAchievementItem","ProjectAchievementItem"), 0.3),
    ]
    latex = lf.latex["ProjectAchievements"]
    def __init__(self):
        self.parent_id = None
        self.value = None
    
    def add_to_context(self, parent_id):
        if self.has_expanded():
            self.parent_id = parent_id
            self.context[self.parent_id][str(self)] = [child for child in self.children]
        else:
            raise Exception(f"{self} must be expanded before it can be added to context")
        
    # def to_latex(self):
    #     if self.has_expanded():
    #         return self.latex % ("\n".join(r"\item "+child.to_latex() for child in self.children),)
    #     else:
    #         raise Exception(f"{self} must be expanded first")


    #.expand is default
    
class ProjectAchievementItem(Terminal):
    def __init__(self):
        self.value = None
    
    def expand(self):
        return self
    
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