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
        return self.df.sort_values(by="quantity", ascending=False).head(top)
