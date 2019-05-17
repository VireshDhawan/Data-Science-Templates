from keras.models import Sequential
from keras.layers import Add, Dense


class ANN:

    def __init__(self, x_train, y_train, problemtype='regression', cv=5):
        self.x_train = x_train
        self.y_train = y_train
        self.cv = cv

        if (problemtype == 'regression'):
            self.clf = "cross_entropy"
        else:
            self.clf = "softmax"


    def show_cross_val_score(self):
        # cv_score = cross_val_score(estimator=self.clf, X=self.x_train, y=self.y_train, cv=self.cv, n_jobs=-1)
        print('Random Forest Cross Validated Score...')
        # print(cv_score)
        print('\n')

    def optimise(self):
        pass
