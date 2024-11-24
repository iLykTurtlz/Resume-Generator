from grammar.terminal import Terminal
import random

class CalPoly(Terminal):
    def __init__(self):
        self.value = None

    def expand(self):
        self.value = {
            "CalPoly": "California Polytechnic State University, San Luis Obispo"
        }
        return self
class EduInstitution(Terminal):
    def __init__(self):
        self.value = None
    # TODO: add other institutions
    def expand(self):
        inst = random.choice(["Cuesta College"])
        self.value = {
            "EduInstitution": inst
        }
        return self


class EduGeographicalInfo(Terminal):
    def __init__(self):
        self.value = None

    def expand(self):
        """TODO: vary the info string formats"""
        inst = random.choice(["Champaign, IL", "Paris, France", "Palo Alto, CA", "Berkeley, CA"])
        self.value = {"EduGeographicalInfo": inst}
        return self

class CalPolyEduGeographicalInfo(Terminal):
    def __init__(self):
        self.value = None

    def expand(self):
        """TODO: vary the info string formats"""
        self.value = {"CalPolyEduGeographicalInfo": "San Luis Obispo, CA"}
        return self


class EduDegreeName(Terminal):
    def __init__(self):
        self.value = None

    def expand(self):
        degree = random.choice(["B.S. Computer Science", "M.S. Computer Science"])
        self.value = {
            "EduDegreeName": degree
        }
        return self


class EduDate(Terminal):
    def __init__(self):
        self.value = None

    def expand(self):
        month = random.choice(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
        year = random.randint(2017, 2024)
        date = month + " " + str(year)
        self.value = {"EduDate": date}
        return self

class EduGPA(Terminal):
    def __init__(self):
        self.value = None

    def expand(self):
        fourscale = 4.0
        gpa = random.normalvariate(3.0, 0.5)
        formats = "{}/{}"
        number = formats.format(str(round(gpa, 1)), str(fourscale))
        self.value = {"EduGPA": number}
        return self
