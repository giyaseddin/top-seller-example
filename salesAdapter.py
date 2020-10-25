from productAdapter import ProductAdapter
from reportable import Reportable


class SalesAdapter(Reportable):
    file_name = 'sales.csv'

    def get_top_seller_report(self, top):
        return self.df.head(top)

    def between(self, min_date, max_date):
        self.df = self.df[(self.df['date'] >= min_date) & (self.df['date'] <= max_date)]

        return self

    def get_products(self):
        return ProductAdapter().filter(self.__get_product_ids()).df

    def get_stores(self):
        pass

    def __get_product_ids(self):
        return self.df['product'].drop_duplicates()
