from filterable import Filterable
from reportable import Reportable


class CityAdapter(Reportable, Filterable):
    file_name = 'store.csv'

    def filter(self, cities):
        self.df = self.df[self.df['city'].isin(cities)]
        return self
