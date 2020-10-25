from filterable import Filterable
from reportable import Reportable


class BrandAdapter(Reportable, Filterable):
    file_name = ''

    def get_top_seller_report(self, top):
        return self.df.head(top)

    def filter(self, brands):
        self.df = self.df[self.df['brand'].isin(brands)]
        return self
