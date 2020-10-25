from abc import abstractmethod
import pandas as ps


class Reportable:
    file_name = ""
    df = None

    @abstractmethod
    def get_top_seller_report(self, top): raise NotImplementedError

    def __init__(self):
        self.file_path = 'datasets/' + self.file_name
        self.df = ps.read_csv(self.file_path)
