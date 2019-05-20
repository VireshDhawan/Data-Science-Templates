# Critical Variables Declaration

problemtype = 'regression'
train_file_path = 'Data/Input/train.csv'
test_file_path = 'Data/Input/test.csv'
target_column_name = 'median_house_value'
is_load_into_sql = False

from DataPreprocessing.Preprocessing import DataPreprocess

dpp = DataPreprocess(train_file_path, target_column_name, is_load_into_sql)
df, x_train, y_train, x_test, y_test, columns, categorical_columns = dpp.read_and_preprocess_data()


from Algorithms.LogisticRegression.LogisticRegression import LgRegression
x_train.insert(0, 'constant',1.00)

lg = LgRegression(x_train, y_train)
x_train = lg.regress()
