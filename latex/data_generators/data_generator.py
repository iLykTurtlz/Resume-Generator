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

    def sample_ln(self, r: str) -> str:
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
        self.zip_code = None  #random.choice
        self.area_code = None  #lookup


class HeadDataGenerator(DataGenerator):
    def generate(self, context):
        #Title - FullName
        full_name = NameDataGenerator().generate(context["Title"])  #already filled in!
        names = full_name.split()

        #PhoneEmail
        email = names[0][0].lower() + names[1].lower() + "@calpoly.edu"

        #TODO: make area code statistically representative, NOT all Bay Area
        area_code = [4, 1, 5]
        last_four = [random.randint(0, 9) for _ in range(4)]
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
        #We can insert GPA after the courses are stuck to it (see below)

        # FOR COURSES: These need to be tacked on to GPA (see below)
        # TODO: Use the data from Dr. Clements instead
        courses = [
            "Algorithms",
            "Data Structures",
            "Speech and Language Processing",
            "Knowledge Discovery from Data",
            "Advanced Data Mining",
            "Linear Algebra",
            "Probability Theory",
            "Operating Systems",
            "Software Engineering",
            "Functional Programming",
            "Database Management Systems",
            "Stochastic Processes",
            "Advanced Algorithm Analysis and Design",
            "Advanced Artificial Intelligence",
            "Advanced Deep Learning",
        ]
        nb_courses = random.randint(2, 6)
        assert len(courses) >= nb_courses, "Population size is smaller than sample size!"

        selected_courses = np.random.choice(courses, size=nb_courses, replace=False)  #kwarg p for a proba distribution

        courses_str = "\n\\item Relevant Coursework: \\footnotesize{%s}" % (', '.join(selected_courses),)
        context[0]["EduGPA"].value = number + courses_str

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
    title = ["TCP/IP Server",
             "Memory Allocator in C",
             "Tic Tac Toe Game using JavaScript",
             "Weather App",
             "ToDo App",
             "Full-Stack Chore App",
             "Twitter Data Mining",
             "Movie Picker",
             "Gaming App",
             "Blog Web App",
             "Linear Regression App",
             "Sentiment Analysis Detector",
             "Housing Pricing Analysis in NYC",
             "Facial Recognition",
             "Average Face Generator",
             "Hackathon"
             ]
    verb_phrases = [
        ["Used Socket API to send a simple HTTP request to a website.",
         "Implemented a TCP with simple data management and provided an interface application."],

        ["Wrote a simple memory allocator in C, and adjusted allocated memory to align to a page boundary.",
         "Wrote a simplistic Unix shell in C."],

        ["Used query selectors functions to perform transitions in between states.",
         "Implemented backtracking search with look-ahead prediction.",
         "Presented the validated game states in a UI for strategy analysis."],

        ["Used open API OpenWeatherMap to gather forecasted data on weather patterns based on users' geographic location.",
         "Implemented UI app to serve the forecasted weather data, with visualizations on compatible web hosted app."],

        ["Built a Full-Stack React Native to-do app with Apollo’s new Query and Mutation components.",
         "App has functionality to add tasks, view them, mark/unmark them as complete and delete them.",
         "Utilized GraphQL backend to store the state of the app."],

        ["Used Python and SQL to build a web app for tracking chores within households.",
         "Created multiple views within a screen to serve all steps of chore tracking, with a point incentivization system.",
         "Provided users with challenge analysis breakdown with a regression of responsibility by commitment."],

        ["Created an app that interacts with the Twitter API.",
         "Connected with Twitter REST APIs with TweePy to provie authorization and provide interacing with explore feed.",
         "Application returns a JSON file with the 50 top trending topics of the last day."],

        ["Scraped a list of top 50 popular movies for each year from 1898–present as listed on IMDb",
         "Used BeautifulSoup to serve and get data from IMDb site."],

        ["Incorporated algorithm and data structures into a game for mobile apps.",
         "Added customization features for the users' characters using random generation."],

        ["Implemented a live blog web app that supports social media feeds, videos, and calendars.",
         "Programmed widgets for readers to share blog posts or leave comments."],

        ["Wrote an app that takes in 2 CSVs to perform linear regression and generate analytical insights based on user-selected variables.",
         "Insights are accompanied by optional confidence tests and variable interaction visualizations."],

        ["Tuned a BERT model to take in 2 phrases as input and output a detected relation between the statements.",
         "Statements could be Complimentary, Opposition, Neutral.",
         "Model tested against Twitter scraped statements reported a 93% accuracy."],

        ["Created a program to predict housing prices based on aggregate data against multiple features of a home.",
         "Took multiple variables into account, including: boroughs, districts, housing type, school districts.",
         "Explored the use of KNN, Random Forests, Regression"],

        ["Created a Facial recognition app using OpenCV and a pre-trained Deep Learning face detector.",
         "Used Haar cascades for face detection in videos, using frame-by-frame movement vector sampling."],

        ["Create an average face using OpenCV",
         "Used Facial feature detection with OpenCV to transform coordinates across image, calculating facial alighnment.",
         "Performed face averaging across all samples from images returned from query."],

        ["Worked under a mentor during a 72 hour period to develop a password wallet.",
         "Retrieved encrypted password from Cloud database and hashed against a personal key.",
         "Wallet is kept personal as an automated decrypter on mobile devices."]

    ]
    tools = ["C, C++",
             "C, C++",
             "JavaScript, HTML, CSS",
             "JavaScript, HTML, CSS, AJAX",
             "Javascript, React Native, Apollo, GraphQL",
             "Python, MySQL, HTML, CSS, Vite, Lit",
             "Python, TweePy",
             "HTML, Python, BeautifulSoup",
             "Python, React, Heroku",
             "Javascript, Typescript, HMTL, CSS",
             "Python, R",
             "Python, Tensorflow",
             "Python, Pandas, Tensorflow",
             "Python, Haar",
             "C++, Python",
             "C, C++, GoLang"

             ]
    dates = ["May 2016", "September 2017", "May 2018", "October 2019", "April 2020", "February 2021", "December 2021"]
    unique_titles = set()

    def generate(self, context):
        for i, proj in enumerate(context[::-1]):
            description = random.choice(ProjectDataGenerator.title)
            while description in ProjectDataGenerator.unique_titles:
                description = random.choice(ProjectDataGenerator.title)
            ProjectDataGenerator.unique_titles.add(description)
            index = ProjectDataGenerator.title.index(description)
            proj["ProjectDescription"].value = description
            proj["ProjectTools"].value = ProjectDataGenerator.tools[index]
            proj["ProjectDate"].value = ProjectDataGenerator.dates[i]
            achievements = ProjectDataGenerator.verb_phrases[index]
            for pa, achievement in zip(proj["ProjectAchievements"], achievements):
                pa.value = achievement


class SkillsDataGenerator(DataGenerator):
    def generate(self, context):
        skill_types = {
            "ProgrammingLanguageSkills": ["C", "C++", "Ada", "Pascal", "Zig", "Golang", "Rust", "Fortran", "OCaml", "Coq", "Haskell", "Standard ML", "Java", "Python", "PL/SQL", "SQL", "Matlab", "R", "HTML/CSS", "JavaScript", "TypeScript", "Racket", "Prolog"],
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
                skillz = np.random.choice(skill_list, size=k, replace=False)  #p for a proba dist.
                for term, skill in zip(skill_terminals, skillz):
                    term.value = skill


class SelfSummaryDataGenerator(DataGenerator):
    def generate(self, context):
        # TODO LLM magic
        context["SelfSummary"].value = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"


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
        if "SelfSummarySection" in context:
            SelfSummaryDataGenerator().generate(context["SelfSummarySection"])


class ResumeDataGenerator(DataGenerator):
    def generate(self, context):
        # We might need some global states like this.
        year_in_school = random.choice([1, 2, 3, 4, 5, 6])

        # might be better to sample wherever they previously went to school
        # then this becomes hometown = SampledLocation()
        hometown = random.choice(["Los Angeles", "San Jose"])

        HeadDataGenerator().generate(context["Head"])
        BodyDataGenerator().generate(context["Body"])
