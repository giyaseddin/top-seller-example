from brandAdapter import BrandAdapter
from filterable import Filterable
from reportable import Reportable
import pandas as ps


class ProductAdapter(Reportable, Filterable):
    file_name = "product.csv"

    def filter(self, ids):
        self.df = self.df[self.df["id"].isin(ids)]
        return self

    def get_brands(self):
        quantities = self.__get_brand_quantities()

        return BrandAdapter(quantities).df

    def __get_brand_quantities(self):
        ids = self.df[["brand", "quantity"]].groupby(by="brand").sum()
        return ids.reset_index(level=0)
