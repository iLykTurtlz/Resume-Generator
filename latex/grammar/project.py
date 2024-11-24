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
        self.context = {}

    def expand(self):
        super().expand()
        self.context["number_of_projects"] = len(self.children)
        ProjectSection.data_factory.generate(self.context)
        return self


class Project(Nonterminal):
    count = 0
    rules = [
        (("ProjectDescription", "Tools", "StartDate", "EndDate", "ProjectAchievements"), 0.5),
        (("ProjectDescription", "Tools", "EndDate", "ProjectAchievements"), 0.5),
    ]
    latex = lf.latex["Project"]
    def __init__(self):
        super().__init__(Project.rules, Project.latex)
        Project.count += 1
        self.id = f"{self}_{toRoman(Project.count)}"


    def expand(self):
        self.context[self.id] = {}
        super().expand()
        for child in self.children:
            child.add_to_context(self.context, self.id)
        return self

        
'''
Context is
{
    "number_of_projects":2,
    "Project_I": {
        "ProjectDescription": obj,
        "Tools": obj,
        "StartDate": obj,
        "EndDate": obj,
        "ProjectAchievements": obj
    },
    "Project_II": {
        ...
    },
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