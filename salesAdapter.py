from productAdapter import ProductAdapter
from reportable import Reportable
from storeAdapter import StoreAdapter


class SalesAdapter(Reportable):
    file_name = 'sales.csv'

    def get_top_seller_report(self, top):
        return self.df.head(top)

    def between(self, min_date, max_date):
        self.df = self.df[(self.df['date'] >= min_date) & (self.df['date'] <= max_date)]

        return self

    def get_products(self):
        ids = self.__get_product_ids()
        quantities = self.__get_product_quantities(ids)

        return ProductAdapter().filter(ids.index).set_quantities(quantities).df

    def get_stores(self):
        return StoreAdapter().filter(self.__get_store_ids()).df

    def __get_product_ids(self):
        return self.df[["product", "quantity"]].groupby(by="product").sum()

    def __get_store_ids(self):
        return self.df["store"].drop_duplicates()

    def __get_product_quantities(self, ids):
        quantities = ids.reset_index(level=0)
        quantities = quantities.rename(columns={"product": 'id'})
        return quantities
