from abc import abstractmethod


class Filterable:
    @abstractmethod
    def filter(self, *args): raise NotImplementedError
