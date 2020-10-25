from cityAdapter import CityAdapter
from filterable import Filterable
from reportable import Reportable


class StoreAdapter(Reportable, Filterable):
    file_name = 'store.csv'

    def get_top_seller_report(self, top):
        return self.df[["name", "quantity"]].sort_values(by="quantity", ascending=False).head(top)

    def filter(self, ids):
        self.df = self.df[self.df['id'].isin(ids)]
        return self

    def get_cities(self):
        quantities = self.__get_city_quantities()

        return CityAdapter(quantities).df

    def __get_city_quantities(self):
        ids = self.df[["city", "quantity"]].groupby(by="city").sum()
        return ids.reset_index(level=0)