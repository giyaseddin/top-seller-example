from filterable import Filterable
from reportable import Reportable


class CityAdapter(Reportable, Filterable):
    file_name = 'store.csv'

    def get_top_seller_report(self, top):
        return self.df.head(top)

    def filter(self, cities):
        self.df = self.df[self.df['city'].isin(cities)]
        return self
