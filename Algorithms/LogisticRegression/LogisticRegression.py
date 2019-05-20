from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import cross_val_score
import numpy as np
import statsmodels.formula.api as sm


class LgRegression:

    def __init__(self, x_train, y_train, problemtype='regression', cv=5):
        self.x_train = x_train
        self.y_train = y_train
        self.cv = cv

        if (problemtype == 'regression'):
            self.clf = LinearRegression()
        else:
            self.clf = LogisticRegression()

    def backwardElimination(self, x, SL):
        regressor_OLS = sm.OLS(endog=self.y_train, exog=x).fit()

        numVars = len(x[0])
        temp = np.zeros((50, 6)).astype(int)
        for i in range(0, numVars):
            regressor_OLS = sm.OLS(self.y_train, x).fit()
            maxVar = max(regressor_OLS.pvalues).astype(float)
            adjR_before = regressor_OLS.rsquared_adj.astype(float)
            if maxVar > SL:
                for j in range(0, numVars - i):
                    if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                        temp[:, j] = x[:, j]
                        x = np.delete(x, j, 1)
                        tmp_regressor = sm.OLS(self.y_train, x).fit()
                        adjR_after = tmp_regressor.rsquared_adj.astype(float)
                        if (adjR_before >= adjR_after):
                            x_rollback = np.hstack((x, temp[:, [0, j]]))
                            x_rollback = np.delete(x_rollback, j, 1)
                            return x_rollback
                        else:
                            continue
        print(regressor_OLS.summary())
        return x

    def classify(self):
        self.clf.fit(self.x_train, self.y_train)

    def regress(self):
        self.x_train = self.x_train.values
        self.y_train = self.y_train.values
        x_opt = self.x_train[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]

        SL = 0.05
        self.x_train = self.backwardElimination(x_opt, SL)
        return self.x_train

        # self.clf.fit(self.x_train, self.y_train)

    def show_cross_val_score(self):
        cv_score = cross_val_score(estimator=self.clf, X=self.x_train, y=self.y_train, cv=self.cv, n_jobs=-1)
        print('Random Forest Cross Validated Score...')
        print(np.mean(cv_score))
        print('\n')

    def optimise(self):
        pass
