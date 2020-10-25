from filterable import Filterable
from reportable import Reportable
import pandas as ps


class ProductAdapter(Reportable, Filterable):
    file_name = 'product.csv'

    def get_top_seller_report(self, top):
        return self.df.head(top)

    def filter(self, ids):
        self.df = self.df[self.df['id'].isin(ids)]
        return self

    def set_quantities(self, quantities):
        self.df = ps.merge(quantities, self.df, on="id")
        return self
