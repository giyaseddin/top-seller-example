import pandas as ps


class Reportable:
    file_name = ""
    df: ps.DataFrame

    def __init__(self, df=None):
        if df is None and (self.file_name is not None and self.file_name is not ""):
            try:
                self.file_path = 'datasets/' + self.file_name
                self.df = ps.read_csv(self.file_path)
            except:
                raise ValueError("File not found")
        else:
            self.df = df

    def get_top_seller_report(self, top):
        tempDf = self.df.sort_values(["quantity", "name"], ascending=[False, True])
        tmp = tempDf.groupby("quantity").count().sort_values(["quantity"], ascending=False).head(top).values
        new_top = 0
        new_top = sum([new_top + tmp[i][0] for i in range(top)])

        return tempDf.nlargest(new_top, "quantity")[["name", "quantity"]]
