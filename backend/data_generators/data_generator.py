from abc import ABC, abstractmethod
import random
import pandas as pd
import numpy as np


class DataGenerator(ABC):
    # fill in the .value attribute of each Terminal within the context
    @abstractmethod
    def generate(self, context):
        raise NotImplementedError("You must implement this method.")