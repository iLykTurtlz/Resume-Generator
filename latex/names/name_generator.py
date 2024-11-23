import pandas as pd
import os
import numpy as np
import random



class NameGenerator:
    dir_path = "../name_distributions/"
    def __init__(self):
        self.male_names = pd.read_csv(NameGenerator.dir_path+"male_names.csv")
        self.female_names = pd.read_csv(NameGenerator.dir_path+"female_names.csv")
        self.last_names = pd.read_csv(NameGenerator.dir_path+"last_names.csv")

    def sample_first_name(self, race, sex):
        """sex in {'m', 'f'}"""
        if sex.lower() == 'm':
            return np.random.choice(self.male_names["Child's First Name"], p=self.male_names['P']).title()
        elif sex.lower() == 'f':
            return np.random.choice(self.female_names["Child's First Name"], p=self.female_names['P']).title()
        else:
            raise Exception("Only m/f are supported")



    