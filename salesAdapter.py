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
        ids = self.__get_store_ids()
        quantities = self.__get_store_quantities(ids)

        return StoreAdapter().filter(ids.index).set_quantities(quantities).df

    def __get_product_ids(self):
        return self.df[["product", "quantity"]].groupby(by="product").sum()

    def __get_store_ids(self):
        return self.df["store"].drop_duplicates()

    def __get_product_quantities(self, ids):
        return self.__get_related_quantities("product", ids)

    def __get_store_quantities(self, ids):
        return self.__get_related_quantities("store", ids)

    def __get_related_quantities(self, related, ids):
        quantities = ids.reset_index(level=0)
        return quantities.rename(columns={related: 'id'})
