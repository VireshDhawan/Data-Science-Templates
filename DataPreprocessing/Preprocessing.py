import pandas as pd


class DataPreprocess:
    input_file = ''

    def __init__(self, input_file):
        self.input_file = input_file

    def read_data(self):
        pd.read_csv(self.input_file)


