from abc import ABC, abstractmethod
import random
import pandas as pd
import numpy as np

class DataGenerator(ABC):
    # fill in the .value attribute of each Terminal within the context
    @abstractmethod
    def generate(self, context):
        raise NotImplementedError("You must implement this method.")
    



class NameDataGenerator(DataGenerator):
    path_to_dir = "./name_distributions/"
    cp_r = (['white', 'black', 'api', 'latinx'], [0.589522, 0.008218, 0.15972, 0.24254])
    cp_s = (['m', 'f'], [0.7, 0.3])

    def __init__(self):
        self.f = pd.read_csv(NameDataGenerator.path_to_dir + "female_names.csv")
        self.m = pd.read_csv(NameDataGenerator.path_to_dir + "male_names.csv")
        self.l = pd.read_csv(NameDataGenerator.path_to_dir + "last_names.csv")

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
        rs, ps = NameDataGenerator.cp_r
        r = np.random.choice(a=rs, p=ps)
        ss, ps = NameDataGenerator.cp_s
        s = np.random.choice(a=ss, p=ps)
        full_name = self.sample_full_name(r, s)
        context["FullName"].value = full_name
        return full_name
    


# Question: COULD THINGS LIKE THIS BE USEFUL???
class SampledHometown:
    #TODO: generate this based on real CalPoly data, then use it in HeadDataGenerator
    def __init__(self):
        self.zip_code = None #random.choice
        self.area_code = None #lookup




class HeadDataGenerator(DataGenerator):
    def generate(self, context):
        #Title - FullName
        full_name = NameDataGenerator().generate(context["Title"]) #already filled in!
        names = full_name.split()

        #PhoneEmail
        email = names[0][0].lower() + names[1].lower() + "@calpoly.edu"
    
        #TODO: make area code statistically representative, NOT all Bay Area
        area_code = [4,1,5]
        last_four = [random.randint(0,9) for _ in range(4)]
        formats = ["({}) 555-{}", "{}-555-{}", "+1 {}-555-{}", "1-{}-555-{}"]
        #TODO: add format weights
        phone_number = random.choice(formats).format("".join(str(num) for num in area_code), "".join(str(num) for num in last_four))
        
        # Remaining fields
        context["PhoneEmail"]["Phone"].value = phone_number
        context["PhoneEmail"]["Email"].value = email

        context["LinkedInGitHub"]["GitHubField"]["GitHub"].value = "sweetDude"
        context["LinkedInGitHub"]["LinkedInField"]["LinkedIn"].value = "anastasia-beaverhousen-a4a06969"

        context["GeographicalInfoField"]["GeographicalInfo"].value = "San Luis Obispo, CA"



class EducationDataGenerator(DataGenerator):
    #Note: this context is ORDERED, i.e. a list
    def generate(self, context):
        context[0]["EduInstitution"].value = "California Polytechnic State University San Luis Obispo"
        context[0]["EduGeographicalInfo"].value = "San Luis Obispo, CA"
        context[0]["EduDegreeName"].value = "B.S. Computer Science"
        context[0]["EduDate"].value = "December 2020"
        
        #GPA
        fourscale = 4.0
        gpa = random.normalvariate(3.0, 0.5)
        formats = "{}/{}"
        number = formats.format(str(round(gpa, 1)), str(fourscale))
        context[0]["EduGPA"].value = number

        # TODO support more than two institutions?  Or different kinds, like HS?
        if len(context) > 1:
            context[1]["EduInstitution"].value = "Cuesta College"
            context[1]["EduGeographicalInfo"].value = "San Luis Obispo, CA"
            context[1]["EduDegreeName"].value = "N/A"
            context[1]["EduDate"].value = "June 2018"
             #GPA
            fourscale = 4.0
            gpa = random.normalvariate(3.0, 0.5)
            formats = "{}/{}"
            number = formats.format(str(round(gpa, 1)), str(fourscale))
            context[1]["EduGPA"].value = number

            


class ExperienceDataGenerator(DataGenerator):
    # Note: this context is ORDERED, i.e. a list
    def generate(self, context):
        COMPANY_MAP = {
            "Google": "https://www.google.com",
            "Apple, Inc.": "https://www.apple.com"
        }
        for experience in context:
            company = random.choice(list(COMPANY_MAP.keys()))
            value = r'''%s [\href{%s}{\faIcon{globe}}]''' % (company, COMPANY_MAP[company])
            experience["CompanyName"].value = value
            experience["JobTitle"].value = "Software Engineer"
            experience["DateRange"].value = "June 2022 - Present"
            experience["GeographicalInfo"].value = "San Luis Obispo, CA"
            for task in experience["ExperienceTasks"]:
                task.value = "Did a thing"


        
class ProjectDataGenerator(DataGenerator):
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
    dates = ["May 2016", "September 2017", "May 2018", "October 2019", "Febuary 2021"]
    def generate(self, context):
        for i, proj in enumerate(context[::-1]):
            proj["ProjectDescription"].value = "This is the description of a project lorem ipsum lorem ipsum."
            proj["ProjectTools"].value = "PyTorch, NLTK, SpaCy"
            proj["ProjectDate"].value = ProjectDataGenerator.dates[i]
            achievements = random.choices(ProjectDataGenerator.verb_phrases, k=len(proj["ProjectAchievements"]))
            for pa, achievement in zip(proj["ProjectAchievements"], achievements):
                pa.value = achievement


class SkillsDataGenerator(DataGenerator):
    def generate(self, context):
        skill_types = {
            "ProgrammingLanguageSkills": ["C", "C++", "Ada", "Rust", "Fortran", "OCaml", "Coq", "Haskell", "Standard ML", "Java", "Python", "PL/SQL", "SQL", "Matlab", "R", "HTML/CSS", "JavaScript", "TypeScript", "Racket", "Prolog"],
            "WebTechnologySkills": ["React", "Angular", "Node.js", "Django"],
            "DatabaseSystemSkills": ["MariaDB", "PostgreSQL", "MySQL", "Microsoft SQL Server", "Redis", "MongoDB", "ElasticSearch"],
            "DataScienceMLSkills": ["Scikit-Learn", "PyTorch", "TensorFlow", "NLTK", "SpaCy", "Pandas", "Matplotlib", "Numpy"],
            "CloudSkills": ["AWS", "Google Cloud", "Azure"],
            "DevOpsSkills": ["Git", "Jenkins", "Selenium", "Docker", "Kubernetes", "Puppet", "Chef", "Ansible", "Nagios"],
            "OtherSkills": ["Linear Programming", "Linux", "FPGA's", "CUDA", "Embedded Systems"]
        }
        for skill_type, skill_list in skill_types.items():
            skill_terminals = context.get(skill_type)
            if skill_terminals:
                k = len(skill_terminals)
                skillz = np.random.choice(skill_list, size=k, replace=False) #p for a proba dist.
                for term, skill in zip(skill_terminals, skillz):
                    term.value = skill



        




class BodyDataGenerator(DataGenerator):
    def generate(self, context):
        if "EducationSection" in context:
            EducationDataGenerator().generate(context["EducationSection"])
        if "ExperienceSection" in context:
            ExperienceDataGenerator().generate(context["ExperienceSection"])
        if "ProjectSection" in context:
            ProjectDataGenerator().generate(context["ProjectSection"])
        if "SkillsSection" in context:
            SkillsDataGenerator().generate(context["SkillsSection"])


    
    
class ResumeDataGenerator(DataGenerator):
    def generate(self, context):
        # We might need some global states like this.
        year_in_school = random.choice([1,2,3,4,5,6])

        # might be better to sample wherever they previously went to school
        # then this becomes hometown = SampledLocation()
        hometown = random.choice(["Los Angeles", "San Jose"])

        HeadDataGenerator().generate(context["Head"])
        BodyDataGenerator().generate(context["Body"])
        