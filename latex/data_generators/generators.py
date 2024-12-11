import random
import pandas as pd
import numpy as np
import json
from collections import Counter
from nltk.tokenize import word_tokenize

from grammar.terminal import Terminal
from llm import generate_text

from .data_generator import DataGenerator
from .experience_data_generator import ExperienceDataGenerator


class NameDataGenerator(DataGenerator):
    path_to_dir = "./name_distributions/"
    cp_r = (['white', 'black', 'api', 'latinx'], [0.589522, 0.008218, 0.15972, 0.24254])

    #source: year 2020 https://ir.calpoly.edu/2020-ceng-enrollment-ugrd-grad-profile
    cp_s = (['m', 'f'], [0.7390, 0.2610])

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



class HeadDataGenerator(DataGenerator):
    def __init__(self, zip_code):
        self.zip_code = int(zip_code)
   
    def generate(self, context):
        full_name = NameDataGenerator().generate(context["Title"])  
        names = full_name.split()

        #PhoneEmail
        email = names[0][0].lower() + names[1].lower() + "@calpoly.edu"


        
        print(f"ZIP_CODE: {self.zip_code}, TYPE: {type(self.zip_code)}")
        #area code lookup
        code_table = pd.read_csv("../data/zipcode/zipcode_areacode.csv")
        result = code_table[code_table['zip_code'] == self.zip_code]['area_code'].values
        if len(result) == 0:
            print("#########ONE")
            area_code = code_table['area_code'].sample(n=1).values[0]
        else:
            print("########TWO")
            area_code = result[0]
        # if isinstance(area_code, pd.Series):
        #     area_code = 
        print(f"AREA CODE: {area_code}, TYPE: {type(area_code)}")


        last_four = [random.randint(0, 9) for _ in range(4)]
        formats = ["({}) 555-{}", "{}-555-{}", "+1 {}-555-{}", "1-{}-555-{}"]
        #TODO: add format weights
        phone_number = random.choice(formats).format(area_code, "".join(str(num) for num in last_four))

        # Remaining fields
        context["PhoneEmail"]["Phone"].value = phone_number
        context["PhoneEmail"]["Email"].value = email

        context["LinkedInGitHub"]["GitHubField"]["GitHub"].value = names[0][0].lower() + names[1].lower()

        numbers = [random.randint(0,9) for _ in range(6)]
        letters = [chr(num) for num in [random.randint(ord('a'), ord('z')) for _ in range(2)]]
        context["LinkedInGitHub"]["LinkedInField"]["LinkedIn"].value = f"{names[0].lower()}-{names[1].lower()}-{letters[0]}{numbers[0]}{letters[1]}{''.join(str(num) for num in numbers[1:])}"

        context["GeographicalInfoField"]["GeographicalInfo"].value = "San Luis Obispo, CA"


class EducationDataGenerator(DataGenerator):
    zipCode = "93405"

    def _sample_courses(self, year, k):
        """Sample course data based on past enrollment.  k should not exceed 20."""
        enrollment = pd.read_csv("../data/enrollment/enrollment.csv", dtype={'code': str})
        with open("../data/enrollment/course_mapping.json", "r") as f:
            course_mapping = json.load(f)
        course_dist = {
            6: ([r"04\d\d", r"05\d\d"], [0.35, 0.65]), #2nd year grad students likely have taken more 500-level courses
            5: ([r"04\d\d", r"05\d\d"], [0.44, 0.56]), #every grad student takes 4 400's and 5 500's
            4: ([r"03\d\d", r"04\d\d", r"05\d\d"], [0.2, 0.7, 0.1]),
            3: ([r"02\d\d", r"03\d\d", r"04\d\d"], [0.15, 0.35, 0.5]),
            2: ([r"02\d\d", r"03\d\d"], [0.6, 0.4]),
            1: ([r"01\d\d", r"02\d\d"], [0.4, 0.6])
        }
        patterns, p = course_dist[year]
        sampled_patterns = random.choices(patterns, p, k=k)
        counts = Counter(sampled_patterns)

        #handle more than 3 100 courses or more than 5 200 courses
        if r"01\d\d" in counts and counts[r"01\d\d"] > 3:
            excess = counts[r"01\d\d"] - 3
            counts[r"01\d\d"] = 3
            if r"02\d\d" in counts:
                counts[r"02\d\d"] += excess
            else:
                counts[r"02\d\d"] = excess
        if r"02\d\d" in counts and counts[r"02\d\d"] > 5:
            excess = counts[r"02\d\d"] - 5
            counts[r"02\d\d"] = 5
            if r"03\d\d" in counts:
                counts[r"03\d\d"] += excess
            else:
                counts[r"03\d\d"] = excess
      
        courses = []
        for pattern, count in counts.items():
            df = enrollment[enrollment['code'].str.match(pattern, na=False)]
            # print(df)
            for course in np.random.choice(df['code'], p=(df['enrolled'] / df['enrolled'].sum()), size=count, replace=False):
                courses.append(course_mapping[course])
        return courses
    
    def _sample_year(self):
        #source: https://ir.calpoly.edu/2020-ceng-enrollment-ugrd-grad-profile (year 2020 data)
            
        # level = np.random.choice(a=["grad", "undergrad"], p=[0.0617, 0.9383])
        # if level == "grad":
        #     year = random.randint(5,6) #uniform
        # else:

        #undergrad only
        year = np.random.choice(a=[1,2,3,4], p=[0.1118, 0.1751, 0.1986, 0.5145])
        return year
        

    #Note: this context is ORDERED, i.e. a list
    def generate(self, context):
        self.year = self._sample_year()

        context[0]["EduInstitution"].value = "California Polytechnic State University San Luis Obispo"
        context[0]["EduGeographicalInfo"].value = "San Luis Obispo, CA"
        context[0]["EduDegreeName"].value = "B.S. Computer Science" 
        context[0]["EduDate"].value = random.choice(["December 2023", "December 2024", "June 2025", "March 2025"])

        #GPA
        fourscale = 4.0
        # source: https://www.sanluisobispo.com/news/local/education/cal-poly-university/article287319830.html
        gpa = random.normalvariate(3.41, 0.4)
        gpa = max(min(gpa, 4.0), 0.1)
        formats = "{}/{}"
        number = formats.format(str(round(gpa, 1)), str(fourscale))
        #We can insert GPA after the courses are stuck to it (see below)

        # FOR COURSES: These need to be tacked on to GPA (see below)
        
        selected_courses = self._sample_courses(self.year, random.randint(2,6))

        courses_str = "\n\\item Relevant Coursework: \\footnotesize{%s}" % (', '.join(selected_courses),)
        context[0]["EduGPA"].value = number + courses_str

        # Support Transfer students & High School Institutions
        if len(context) > 1:
            # 445 / 1173 = ratio of transfer
            # California (930), Washington (251), Colorado (94), Oregon (68), Texas (48)
            formerSchoolType = random.choices(["transfer", "direct"], weights=[445, 728], k=1)
            if formerSchoolType[0] == "transfer":
                feederSchools = [("Cuesta College", "San Luis Obispo, CA", "93407"), ("Allan Hancock College", "Santa Maria, CA", "93454"),
                                 ("Moorpark College", "Moorpark, CA", "93021"), ("De Anza Community College", "Cupertino, CA", "95014"),
                                 ("Santa Barbara City College", "Santa Barbara, CA", "93109"), ("Diablo Valley College", "Pleasant Hill, CA", "94523"),
                                 ("Foothill College", "Los Altos Hills, CA", "94022"), ("Santa Rosa Junior College", "Santa Rosa, CA", "95401"),
                                 ("Hartnell Community College", "Salinas, CA", "93901"), ("Santa Monica College", "Santa Monica, CA", "90405")]
                feederSchoolsWeights = [189, 168, 45, 43, 41, 34, 27, 26, 25, 25]
                randomFeeder = random.choices(feederSchools, weights=feederSchoolsWeights, k=1)

                context[1]["EduInstitution"].value = randomFeeder[0][0]
                context[1]["EduGeographicalInfo"].value = randomFeeder[0][1]
                context[1]["EduDegreeName"].value = "Computer Science"
                EducationDataGenerator.zipCode = randomFeeder[0][2]
            else:
                state = random.choices(["ca", "wa", "or", "tx"], weights=[930, 251, 68, 48], k=1)
                df = pd.read_csv(f"../data/HighSchools/{state[0]}Students.csv")
                index = random.randint(0, len(df)-1)
                schoolName = df.iloc[index, 0].replace("ELEMENTARY", "").replace("MIDDLE", "").title()
                location = df.iloc[index, 1].title() + ", " + df.iloc[index, 2]
                context[1]["EduInstitution"].value = schoolName
                context[1]["EduGeographicalInfo"].value = location
                context[1]["EduDegreeName"].value = "High School Student"
                EducationDataGenerator.zipCode = df.iloc[index, 3]

            dates = ["December 2021", "August 2021", "November 2022", "March 2022"]
            context[1]["EduDate"].value = random.choice(dates)
            #GPA
            fourscale = 4.0
            gpa = random.normalvariate(4.01, 0.4)
            if gpa < 3.0:
                gpa = 3.0
            elif gpa > 5.0:
                gpa = 5.0
            formats = "{}/{}"
            number = formats.format(str(round(gpa, 1)), str(fourscale))
            context[1]["EduGPA"].value = number


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
             "Hackathon",
             "Sewing Website"
             ]
    verb_phrases = [
        ["Used Socket API to send a simple HTTP request to a website.",
         "Implemented a TCP with simple data management and provided an interface application.",
         "Corruption is detected using boolean hashing."],

        ["Wrote a simple memory allocator in C, and adjusted allocated memory to align to a page boundary.",
         "Wrote a simplistic Unix shell in C.",
         "Extended to include a file system checker."],

        ["Used query selectors functions to perform transitions in between states.",
         "Implemented backtracking search with look-ahead prediction.",
         "Presented the validated game states in a UI for strategy analysis."],

        ["Used open API OpenWeatherMap to gather forecasted data on weather patterns based on users' geographic location.",
         "Implemented UI app to serve the forecasted weather data, with visualizations on compatible web hosted app.",
         "Past weather queries are stored in AWS RDS cloud to query against for history view."],

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
         "Used BeautifulSoup to serve and get data from IMDb pages",
         "Word processor extracts the top reviews and makes recommendations based on stored user keywords."],

        ["Incorporated algorithm and data structures into a game for mobile apps.",
         "Added customization features for the users' characters using random generation.",
         "Leaderboard mods available through the use of cookie tracking."],

        ["Implemented a live blog web app that supports social media feeds, videos, and calendars.",
         "Programmed widgets for readers to share blog posts or leave comments.",
         "Users may share 3 sponsored blog posts a month on an explore feed, implemented with graph connections."],

        ["Wrote an app that takes in 2 CSVs to perform linear regression and generate analytical insights based on user-selected variables.",
         "Insights are accompanied by optional confidence tests and variable interaction visualizations.",
         "Makes API calls to wordMarket for contextual specifications on the analysis."],

        ["Tuned a BERT model to take in 2 phrases as input and output a detected relation between the statements.",
         "Statements could be Complimentary, Opposition, Neutral.",
         "Model tested against Twitter scraped statements reported a 93 percent accuracy."],

        ["Created a program to predict housing prices based on aggregate data against multiple features of a home.",
         "Took multiple variables into account, including: boroughs, districts, housing type, school districts.",
         "Explored the use of KNN, Random Forests, Regression"],

        ["Created a Facial recognition app using OpenCV and a pre-trained Deep Learning face detector.",
         "Used Haar cascades for face detection in videos, using frame-by-frame movement vector sampling.",
         "Performs with a 89 percent accuracy over 100 trials."],

        ["Created an average face using aggregated facial image data from Kaggle.",
         "Used Facial feature detection with OpenCV to transform coordinates across image, calculating facial alignment.",
         "Performed face averaging across all samples from images returned from query."],

        ["Worked under a mentor during a 72 hour period to develop a password wallet.",
         "Retrieved encrypted password from Cloud database and hashed against a personal key.",
         "Wallet is kept personal as an automated decrypter on mobile devices."],

        ["Developed a Sewing Almanac for avid sewists in the San Luis Obispo country area.",
         "Completed with a social media forum for sharing results and tips on garment items.",
         "Users can trade garment cards through a central admin database."]

    ]
    tools = [["C, C++", "C, C++", "", "", "", "", ""],
             ["C, C++", "C, C++", "", "", "", "", ""],
             ["JavaScript, HTML, CSS", "JavaScript", "HTML, CSS", "", "", "", ""],
             ["JavaScript, HTML, CSS, AJAX", "JavaScript", "HTML, CSS, AJAX", "", "", "", ""],
             ["Javascript, React Native, Apollo, GraphQL", "", "Javascript, React Native", "", "Apollo, GraphQL", "", ""],
             ["Python, MySQL, HTML, CSS, Vite, Lit", "Python", "HTML, CSS, Vite, Lit", "MySQL", "", "", ""],
             ["Python, TweePy", "Python, TweePy", "", "", "", "", ""],
             ["HTML, Python, BeautifulSoup", "Python, BeautifulSoup", "HTML", "", "", "", ""],
             ["Python, React, Heroku", "Python", "React", "Heroku", "", "", ""],
             ["Javascript, Typescript, HTML, CSS", "Javascript", "Typescript, HMTL, CSS", "", "", "", ""],
             ["Python, R", "Python", "", "", "R", "", ""],
             ["Python, Tensorflow", "Python, Tensorflow", "", "", "", "", ""],
             ["Python, Pandas, Tensorflow", "Python, Pandas, Tensorflow", "", "", "", "", ""],
             ["Python, Haar", "Python", "", "", "Haar", "", ""],
             ["C++, Python", "C++, Python", "", "", "", "", ""],
             ["C, C++, GoLang", "C, C++, GoLang", "", "", "", "", ""],
             ["CSS, HTML, Typescript", "", "CSS, HTML, Typescript", "", "", "", ""]
            ]
    dates = ["December 2021", "August 2022", "November 2023", "March 2024", "October 2024"]
    unique_titles = set()
    # unique_programmingLang = set()
    # unique_webTech = set()
    # unique_db = set()
    # unique_DSML = set()
    # unique_Cloud = set()
    # unique_devOps = set()

    def generate(self, context):
        # print(f"context is here: {context[::-1]}")
        self.tools = set()
        for i, proj in enumerate(context[::-1]):
            description = random.choice(ProjectDataGenerator.title)
            while description in ProjectDataGenerator.unique_titles:
                description = random.choice(ProjectDataGenerator.title)
            ProjectDataGenerator.unique_titles.add(description)
            index = ProjectDataGenerator.title.index(description)
            proj["ProjectDescription"].value = description
            proj["ProjectTools"].value = ProjectDataGenerator.tools[index][0]
            # ProjectDataGenerator.unique_programmingLang.update(ProjectDataGenerator.tools[index][1].split(", "))
            # ProjectDataGenerator.unique_webTech.update(ProjectDataGenerator.tools[index][2].split(", "))
            # ProjectDataGenerator.unique_db.update(ProjectDataGenerator.tools[index][3].split(", "))
            # ProjectDataGenerator.unique_DSML.update(ProjectDataGenerator.tools[index][4].split(", "))
            # ProjectDataGenerator.unique_Cloud.update(ProjectDataGenerator.tools[index][5].split(", "))
            # ProjectDataGenerator.unique_devOps.update(ProjectDataGenerator.tools[index][6].split(", "))
            self.tools.update(item.strip() for item in proj["ProjectTools"].value.split(","))

            proj["ProjectDate"].value = ProjectDataGenerator.dates[i]
            achievements = ProjectDataGenerator.verb_phrases[index]
            for pa, achievement in zip(proj["ProjectAchievements"], achievements):
                pa.value = achievement


class SkillsDataGenerator(DataGenerator):
    def __init__(self, achievements, tools):
        self.achievements = achievements
        self.tools = {tool.strip().lower() for tool in tools}
        print(self.tools)

    def _read_skills(self):
        result = {}
        with open("../data/tech/database.json", "r") as f:
            db_json = json.load(f)
        result["db"] = set(db_json["2018"]["technologies"])
        with open("../data/tech/datascience.json", "r") as f:
            dsml_json = json.load(f)
        result["dsml"] = set(dsml_json["general"])
        with open("../data/tech/devops.json") as f:
            devops_json = json.load(f)
        result["devops"] = set(devops_json["all"])
        with open("../data/tech/web.json") as f:
            web_json = json.load(f)
        result["web"] = set()
        for data in web_json.values():
            result["web"].update(data["technologies"])
        result["cloud"] = {"AWS", "Google Cloud", "Azure"}
        pl = pd.read_csv("../data/tiobe/tiobe.csv")
        result["pl"] = set(pl['language'])
        return result

    def _collect_skills(self):
        all_skills = self._read_skills()
        found_skills = {skill_type:set() for skill_type in all_skills}

        tokenized_achievements = [set(word_tokenize(a.lower())) for a in self.achievements]

        for skill_type, skillset in all_skills.items():
            for skill in skillset:
                if skill.lower() in self.tools:
                    found_skills[skill_type].add(skill)
                    continue
                for tokens in tokenized_achievements:
                    if skill.lower() in tokens:
                        found_skills[skill_type].add(skill)
                    
        
        # found_skills["pl"] |= ProjectDataGenerator.unique_programmingLang
        # found_skills["web"] |= ProjectDataGenerator.unique_webTech
        # found_skills["db"] |= ProjectDataGenerator.unique_db
        # found_skills["dsml"] |= ProjectDataGenerator.unique_DSML
        # found_skills["cloud"] |= ProjectDataGenerator.unique_Cloud
        # found_skills["devops"] |= ProjectDataGenerator.unique_devOps

        return found_skills, all_skills


    def generate(self, context):
        found_skills, all_skills = self._collect_skills()
        skill_types = {
            "pl":"ProgrammingLanguageSkills",
            "web":"WebTechnologySkills",
            "db":"DatabaseSystemSkills",
            "dsml":"DataScienceMLSkills",
            "cloud":"CloudSkills",
            "devops":"DevOpsSkills",
        }
        for skill_type, skill_terminal_label in skill_types.items():
            skill_terminals = context.get(skill_terminal_label)
            if skill_terminals:
                k = len(skill_terminals)
                difference = k - len(found_skills[skill_type])
                if skill_type != "pl":
                    skills = list(all_skills[skill_type])
                    while difference > 0:
                        found_skills[skill_type].update(
                            np.random.choice(list(skills), size=difference)
                        )    
                        difference = k - len(found_skills[skill_type])
                else:
                    pls = pd.read_csv("../data/tiobe/tiobe.csv")
                    while difference > 0:
                        found_skills[skill_type].update(
                            pls['language'].sample(n=difference, weights=pls['fraction'])
                        )
                        difference = k - len(found_skills[skill_type])
            
                for term, skill in zip(skill_terminals, list(found_skills[skill_type])[:len(skill_terminals)]):
                    term.value = skill


class SelfSummaryDataGenerator(DataGenerator):
    # In case things go wrong
    DEFAULT_SELF_SUMMARIES = [
        "Aspiring software engineer with a strong foundation in computer science and a passion for creating impactful, user-friendly applications. Experienced in building scalable systems and contributing to cross-functional teams.",
        "Dedicated developer with expertise in full-stack web development, cloud computing, and database optimization. Excels in delivering innovative solutions to complex problems under tight deadlines.",
        "Creative problem-solver with experience in designing and implementing AI-driven applications. Passionate about advancing technology and driving efficiency in software systems.",
        "Motivated software engineer with a background in developing user-centric applications. Skilled in modern frameworks, APIs, and optimizing for performance at scale.",
        "Results-driven software developer with a proven ability to deliver clean, maintainable code. Passionate about collaborating with teams to solve challenging technical problems.",
        "Enthusiastic computer scientist skilled in Python, JavaScript, and modern web frameworks. Focused on creating reliable, scalable, and user-friendly solutions.",
        "Proactive engineer specializing in cloud-native architectures and DevOps practices. Eager to contribute to high-impact projects that push the boundaries of technology.",
        "Adaptable developer with experience in building secure, scalable applications for web and mobile platforms. Passionate about delivering value to users through innovative design.",
        "Detail-oriented software engineer with a strong background in algorithms, data structures, and distributed systems. Committed to building efficient and effective software solutions.",
        "Passionate programmer with experience in AI/ML applications, backend services, and database optimization. Enjoys solving challenging problems and driving impactful results."
    ]

    
    def generate(self, context):
        # TODO LLM magic
        jsn = self._get_expanded_json(context)
        prompt = f"{jsn}\n\nThe above json represents a CS student resume. Generate a self-summary/objective section for the resume. Output the result in a JSON format, with 'summary' as the key, e.g." + "{summary: <summary_goes_here>}. Do NOT output anything besides the final JSON."
        self_summary = generate_text(prompt)
        print(f"self_summary: {self_summary}")
        


        try:
            self_summary = json.loads(self_summary)
            while isinstance(self_summary, dict):
                if len(self_summary) == 1:
                    self_summary = list(self_summary.values())[0]
                elif len(self_summary) > 1:
                    for k,v in self_summary.items():
                        if "summary" in k.lower():
                            self_summary = v
                            break
        except:
            self_summary = random.choice(self.DEFAULT_SELF_SUMMARIES)
        context["SelfSummarySection"]["SelfSummary"].value = self_summary
        
        
    def _get_expanded_json(self, context):
        if isinstance(context, Terminal):
            try:
                return context.to_latex()
            except:
                return None
        elif isinstance(context, list):
            return [self._get_expanded_json(ctx) for ctx in context]
        return {
            k: self._get_expanded_json(v) for k, v in context.items()
        }


class BodyDataGenerator(DataGenerator):
    def generate(self, context):
        if "EducationSection" in context:
            EducationDataGenerator().generate(context["EducationSection"])
        achievements = []
        if "ExperienceSection" in context:
            edg = ExperienceDataGenerator()
            edg.generate(context["ExperienceSection"])
            achievements = edg.all_achievements
        tools = set()
        if "ProjectSection" in context:
            pdg = ProjectDataGenerator()
            pdg.generate(context["ProjectSection"])
            tools = pdg.tools
        if "SkillsSection" in context:
            SkillsDataGenerator(achievements, tools).generate(context["SkillsSection"])
        if "SelfSummarySection" in context:
            SelfSummaryDataGenerator().generate(context)


class ResumeDataGenerator(DataGenerator):
    def generate(self, context):
        BodyDataGenerator().generate(context["Body"])
        HeadDataGenerator(EducationDataGenerator.zipCode).generate(context["Head"])
