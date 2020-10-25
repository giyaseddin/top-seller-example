from filterable import Filterable
from reportable import Reportable


class BrandAdapter(Reportable, Filterable):
    file_name = ''

    def get_top_seller_report(self, top):
        tempDf = self.df.sort_values(["quantity", "brand"], ascending=False)
        tmp = tempDf.groupby("quantity").count().sort_values(["quantity"], ascending=False).head(top).values
        new_top = 0
        new_top = sum([new_top + tmp[i][0] for i in range(top)])

        return tempDf.nlargest(new_top, "quantity")[["brand", "quantity"]]

    def filter(self, brands):
        self.df = self.df[self.df['brand'].isin(brands)]
        return self
