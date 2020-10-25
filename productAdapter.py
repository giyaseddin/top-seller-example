from filterable import Filterable
from reportable import Reportable


class ProductAdapter(Reportable, Filterable):
    file_name = 'product.csv'

    def get_top_seller_report(self, top):
        return self.df.head(top)

    def filter(self, ids):
        self.df = self.df[self.df['id'].isin(ids)]
        return self
