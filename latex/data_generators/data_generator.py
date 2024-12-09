from abc import ABC, abstractmethod


class DataGenerator(ABC):
    # fill in the .value attribute of each Terminal within the context
    @abstractmethod
    def generate(self, context):
        raise NotImplementedError("You must implement this method.")