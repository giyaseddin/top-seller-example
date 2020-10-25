from filterable import Filterable
from reportable import Reportable


class BrandAdapter(Reportable, Filterable):
    file_name = ''

    def filter(self, brands):
        self.df = self.df[self.df['brand'].isin(brands)]
        return self
