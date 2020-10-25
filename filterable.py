from abc import abstractmethod
import pandas as ps


class Filterable:
    @abstractmethod
    def filter(self, *args): raise NotImplementedError

    def set_quantities(self, quantities, on="id"):
        self.df = ps.merge(quantities, self.df, on=on)
        return self
