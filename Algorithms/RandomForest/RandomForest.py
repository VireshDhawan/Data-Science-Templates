from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score


class RandomForest:

    def __init__(self, x_train, y_train, x_test, y_test):
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
        self.clf = RandomForestClassifier()
        self.rgs = RandomForestRegressor()
        self.cv = 5

    def classify(self):
        self.clf.fit(self.x_train, self.y_train)
        cross_val_score(estimator=self.clf, X=self.x_train, y=self.y_train, cv=self.cv, n_jobs=-1)

    def regress(self):
        pass

    def show_cross_val_score(self):
        cross_val_score(estimator=self.clf, X=self.x_train, y=self.y_train, cv=self.cv, n_jobs=-1)

    def optimise(self):
        pass
