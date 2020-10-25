from abc import abstractmethod
import pandas as ps


class Filterable:
    @abstractmethod
    def filter(self, *args): raise NotImplementedError

    def set_quantities(self, quantities):
        self.df = ps.merge(quantities, self.df, on="id")
        return self
