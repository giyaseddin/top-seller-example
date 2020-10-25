from abc import abstractmethod
import pandas as ps


class Reportable:
    file_name = ""
    df: ps.DataFrame

    @abstractmethod
    def get_top_seller_report(self, top): raise NotImplementedError

    def __init__(self, df=None):
        if df is None:
            self.file_path = 'datasets/' + self.file_name
            self.df = ps.read_csv(self.file_path)
        else:
            self.df = df
