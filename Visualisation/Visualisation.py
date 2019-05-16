import matplotlib.pyplot as plt
import seaborn as sns

from Visualisation.Artists import Artists


class Visualisation:
    ar = Artists()

    def __init__(self, x_train, y_train, output_col_name):
        self.x_train = x_train
        self.y_train = y_train
        self.output_col_name = output_col_name

    def draw_relationship_out_in(self):
        for column in self.x_train.columns:
            self.ar.draw_line_continuous(self.x_train[column], self.y_train, column, self.output_col_name)

    def show_variable_corelation(self):
        # Using Pearson Corelation
        plt.figure(figsize=(12, 10))
        cor = self.x_train.corr()
        sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
        plt.show()

