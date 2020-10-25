from filterable import Filterable
from reportable import Reportable


class CityAdapter(Reportable, Filterable):
    file_name = 'store.csv'

    def get_top_seller_report(self, top):
        tempDf = self.df.sort_values(["quantity", "city"], ascending=False)
        tmp = tempDf.groupby("quantity").count().sort_values(["quantity"], ascending=False).head(top).values
        new_top = 0
        new_top = sum([new_top + tmp[i][0] for i in range(top)])

        return tempDf.nlargest(new_top, "quantity")[["city", "quantity"]]

    def filter(self, cities):
        self.df = self.df[self.df['city'].isin(cities)]
        return self
