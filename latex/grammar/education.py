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

    def expand(self):
        self.value = {
            "EduInstitution": "Some Other Institution"
        }
        return self

class EduGeographicalInfo(Terminal):
    def __init__(self):
        self.value = None

    def expand(self):
        """TODO: vary the info string formats"""
        self.value = {"EduGeographicalInfo": "San Luis Obispo, CA"}
        return self


class EduDegreeName(Terminal):
    """TODO: generate DegreeName fields in expand"""
    def __init__(self):
        self.value = None

    def expand(self):
        self.value = {
            "EduDegreeName": "B.S."
        }
        return self


class EduDate(Terminal):
    def __init__(self):
        self.value = None

    def expand(self):
        month = random.choice(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
        year = random.randint(2017, 2024)
        date = " ".join(month, str(year))
        self.value = {"EduDate": date}
        return self

class EduGPA(Terminal):
    def __init__(self):
        self.value = None

    def expand(self):
        fourscale = 4.0
        gpa = random.uniform(0.0, 4.0)
        formats = "{}/{}"
        number = formats.format(str(round(gpa, 1)), str(fourscale))
        self.value = {"EduGPA": number}
        return self
