from abc import ABC, abstractmethod
import random

class DataFactory(ABC):
    # def __init__(self):
    #     pass

    @abstractmethod
    def generate(self, context):
        raise NotImplementedError("You must implement this method.")
        

class NameDataFactory(DataFactory):
    def generate(self, context):
        pass

class ProjectDataFactory(DataFactory):
    verb_phrases = [
        "Hopped on top of pop",
        "Cooked green eggs and ham",
        "Juggled on the ball",
        "Ran through the house",
        "Balanced fish on a dish",
        "Jumped on the bed with a hat",
        "Spoke to a Who in the snow",
        "Rode a bike with no wheels",
        "Climbed a tree with Thing One",
        "Played a tune with a spoon",
        "Ran a race with a fox",
        "Painted spots on a box",
        "Sailed a boat with a goat",
        "Sneezed bees into the breeze",
        "Sang a song to the moon",
        "Fed a mouse a house of cheese",
        "Danced with cats in striped hats",
        "Swam with a Zinn in a zinny pool",
        "Shook hands with a Wocket in a pocket",
        "Spoke for the trees",
    ]
    # def __init__(self):
    #     pass
    dates = ["May 2016", "September 2017", "May 2018", "October 2019", "Febuary 2021"]
    def generate(self, context):
        n = context["number_of_projects"]
        for i in range(n, 0):
            proj = context[f"Project_{i}"]
            proj["ProjectDescription"].value = {
                "ProjectDescription" : "This is the description of a project lorem ipsum lorem ipsum."
            }
            proj["ProjectTools"].value = {"ProjectTools" : "PyTorch, NLTK, SpaCy"}
            proj["ProjectDate"].value = {"ProjectDate" : ProjectDataFactory.dates[n - i]}
            achievements = random.choices(ProjectDataFactory.verb_phrases, replace=False, k=len(proj["ProjectAchievements"]))
            for pa, achievement in zip(proj["ProjectAchievements"], achievements):
                pa.value = {"ProjectAchievementItem" : achievement}
    




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
