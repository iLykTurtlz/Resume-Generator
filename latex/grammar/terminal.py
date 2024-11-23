from roman import toRoman, fromRoman
from grammar.symbol import Symbol, SymbolFactory
import random
from abc import ABC, abstractmethod

class Terminal(Symbol, ABC):
    @abstractmethod
    def expand(self):
        raise NotImplementedError("You must implement this method.")
    
    def has_expanded(self):
        return self.value is not None
    
    def to_latex(self):
        if self.has_expanded():
            return self.value[str(self)]
        else:
            raise Exception(f"{self} must be expanded first")
        
    def get(self):
        if self.has_expanded():
            return self.value
        else:
            raise Exception(f"{self} must be expanded first")

class FullName(Terminal):
    def __init__(self):
        self.value = None

    def expand(self):
        """TODO: Replace with name generator module"""
        letters = 'abcdefghijklmnopqrstuvwxyz'
        fn_length = random.randint(5,10)
        ln_length = random.randint(5,15)
        self.value = {
            "FullName" : "".join(random.choice(letters) for _ in range(fn_length)).capitalize() + " " + \
                "".join(random.choice(letters) for _ in range(ln_length)).capitalize()
              
        }
        return self

class GitHub(Terminal):
    def __init__(self):
        self.value = None

    def expand(self):
        """TODO: 2 options
        1. replace each field with a call to an info generator
        2. register the class in a central DataFactory that generates the fields once it has ALL instances
        Option 2 is better for interdependent fields.
        """
        self.value = {
            "href" : "https://github.com/iLykTurtlz",
            "GitHub" : "iLykTurtlz"
        }
        return self
        


class LinkedIn(Terminal):
    """TODO: generate LinkedIn fields in expand"""
    def __init__(self):
        self.value = None
    
    def expand(self):
        self.value = {
            "href" : "https://www.linkedin.com/in/paul-jarski-a4a04386/",
            "LinkedIn" : "paul-jarski-a4a04386"
        }
        return self
         
         


class Phone(Terminal):
    def __init__(self):
        self.value = None

    def expand(self):
        #TODO: make area code statistically representative, NOT all Bay Area
        area_code = [4,1,5]
        last_four = [random.randint(0,9) for _ in range(4)]
        formats = ["({}) 555-{}", "{}-555-{}", "+1 {}-555-{}", "1-{}-555-{}"]
        #TODO: add format weights
        number = random.choice(formats).format("".join(str(num) for num in area_code), "".join(str(num) for num in last_four))
        self.value = {"Phone" : number}
        return self


class Email(Terminal):
    def __init__(self):
        self.value = None

    def expand(self):
        self.value = {"Email" : "pjarski@calpoly.edu"}
        return self
    


class GeographicalInfo(Terminal):
    def __init__(self):
        self.value = None

    def expand(self):
        """TODO: vary the info string formats"""
        self.value = {"GeographicalInfo": "San Luis Obispo, CA"}
        return self




