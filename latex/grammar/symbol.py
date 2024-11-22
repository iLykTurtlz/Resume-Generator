from abc import ABC, abstractmethod
import sys

class SymbolFactory:
    @staticmethod
    def create_instances(class_names):
        ns = sys.modules["grammar"]
        return [getattr(ns, name)() for name in class_names]


class Symbol(ABC):
    @abstractmethod
    def expand(self):
        raise NotImplementedError("You must implement this method.")