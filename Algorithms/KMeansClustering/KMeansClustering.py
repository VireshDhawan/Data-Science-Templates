from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import numpy as np


class KMeansClustering:

    def __init__(self, x_train, y_train, problemtype = 'regression', cv = 5):
        self.x_train = x_train
        self.y_train = y_train
        self.cv = cv

        if problemtype == 'regression':
            self.clf = KNeighborsRegressor()
        elif problemtype == 'classification':
            self.clf = KNeighborsClassifier()


    def classify(self):
        self.clf.fit(self.x_train, self.y_train)

    def regress(self):
        self.clf.fit(self.x_train, self.y_train)


    def show_cross_val_score(self):
        cv_score = cross_val_score(estimator=self.clf, X=self.x_train, y=self.y_train, cv=self.cv, n_jobs=-1)
        print('KMeans Cross Validated Score...')
        print(np.mean(cv_score))
        print('\n')

    def optimise(self):
        pass
