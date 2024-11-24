from abc import ABC, abstractmethod

class DataFactory:
    def __init__(self):
        pass

    @abstractmethod
    def generate(self, context):
        raise NotImplementedError("You must implement this method.")
        

class NameDataFactory(DataFactory):
    def generate(self, context):
        pass

class ProjectDataFactory(DataFactory):
    def __init__(self):
        pass

    def generate(self, context):
        