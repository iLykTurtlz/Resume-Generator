from abc import ABC, abstractmethod
import random
import pandas as pd
import numpy as np

class DataFactory(ABC):
    # def __init__(self):
    #     pass

    @abstractmethod
    def generate(self, context):
        raise NotImplementedError("You must implement this method.")
        
class NameDataFactory(DataFactory):
    path_to_dir = "./name_distributions/"
    cp_r = (['white', 'black', 'api', 'latinx'], [0.589522, 0.008218, 0.15972, 0.24254])
    cp_s = (['m', 'f'], [0.7, 0.3])

    def __init__(self):
        self.f = pd.read_csv(NameDataFactory.path_to_dir + "female_names.csv")
        self.m = pd.read_csv(NameDataFactory.path_to_dir + "male_names.csv")
        self.l = pd.read_csv(NameDataFactory.path_to_dir + "last_names.csv")

    def sample_fn(self, r: str, sex: str) -> str:
        """sex in {'m', 'f'}"""
        if sex.lower() == 'm':
            fn_m = self.m[self.m['Ethnicity'] == r]
            return np.random.choice(fn_m["Child's First Name"], p=fn_m['P'] / fn_m['P'].sum()).title()
        elif sex.lower() == 'f':
            fn_f = self.f[self.f['Ethnicity'] == r]
            return np.random.choice(fn_f["Child's First Name"], p=fn_f['P'] / fn_f['P'].sum()).title()
        else:
            raise Exception("sex in {'m','f'}")
        
    def sample_ln(self, r : str) -> str:
        return np.random.choice(self.l['name'], p=self.l[r]).title()

    def sample_full_name(self, r: str, sex: str) -> str:
        return self.sample_fn(r, sex) + " " + self.sample_ln(r)

    def generate(self, context):
        rs, ps = NameDataFactory.cp_r
        r = np.random.choice(a=rs, p=ps)
        ss, ps = NameDataFactory.cp_s
        s = np.random.choice(a=ss, p=ps)
        return self.sample_full_name(r, s)





    



        



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
        # print(f"n: {n}")
        for i in range(n, 0, -1):
            # print(f"i: {i}")
            proj = context[f"Project_{i}"]
            proj["ProjectDescription"].value = {
                "ProjectDescription" : "This is the description of a project lorem ipsum lorem ipsum."
            }
            # print(f"DESCRIPTION: {proj['ProjectDescription'].value}")
            proj["ProjectTools"].value = {"ProjectTools" : "PyTorch, NLTK, SpaCy"}
            proj["ProjectDate"].value = {"ProjectDate" : ProjectDataFactory.dates[n - i]}
            achievements = random.choices(ProjectDataFactory.verb_phrases, k=len(proj["ProjectAchievements"]))
            for pa, achievement in zip(proj["ProjectAchievements"], achievements):
                pa.value = {"ProjectAchievementItem" : achievement}
                # print(f"ACHIEVEMENT: {pa.value}")
        # print("FILLED IN VALUES")





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
