import os

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer as Imputer
from sklearn.preprocessing import RobustScaler as scaler
from Utils.database import Database
from sklearn.model_selection import train_test_split


class DataPreprocess:

    def __init__(self, input_file, output_column_name, is_load_into_sql):
        self.input_file = input_file
        self.output_column_name = output_column_name
        self.is_load_into_sql = is_load_into_sql

    def insert_data_into_sql(self):
        db = Database()

        # Create the Train Table
        create_command = 'create table if not exists train (trainid INT AUTO_INCREMENT,'
        collist = ''
        for column in self.df.columns:
            create_command += column + ' TEXT,'
            collist += column + ','
        collist = collist[:-1] + ");"

        create_command += 'primary key (trainid));'
        db.execute_query_with_params(create_command, {})

        # Load the Training File
        base_path = os.getcwd().replace('\\', '/') + '/'
        load_command = "LOAD DATA LOCAL INFILE '" + base_path + self.input_file + \
                       "' INTO TABLE train FIELDS TERMINATED BY ',' " \
                       "LINES TERMINATED BY '\\n' " \
                       "IGNORE 1 LINES (" + collist

        db.execute_query_with_params(load_command, {})
        return

    def read_and_preprocess_data(self):

        # Read File
        self.df = pd.read_csv(self.input_file)
        print('Step 1 - File Read Complete ...')

        # if (self.is_load_into_sql):
        #     self.insert_data_into_sql()

        # Get All training Columns
        self.get_training_columns(self.df)

        # Break Down Input and Output Columns
        self.x_train = self.df[self.traincols]
        self.y_train = self.df[self.output_column_name]

        # Start Preprocessing
        return self.preprocess_data()

    def preprocess_data(self):

        # Step 1 - One Hot Encode
        self.get_categorical_columns()
        print('Step 2 - Categorical Column Identification Complete ...')

        self.x_train = pd.get_dummies(self.x_train, columns=self.categorical_columns, prefix='one_hot_encoded_')
        self.get_training_columns(self.x_train)
        # Hotfix for XGBoost
        for column in self.traincols:
            if ("<" in column):
                self.x_train.rename(index=str, columns={column: column.replace("<", "")}, inplace=True)
        self.get_training_columns(self.x_train)
        encoded_columns = [i for i in self.traincols if "one_hot_encoded_" in i][:-1]
        not_encoded_columns = [i for i in self.traincols if "one_hot_encoded_" not in i]
        self.x_train = self.x_train[self.union(encoded_columns, not_encoded_columns)]
        self.get_training_columns(self.x_train)
        print('Step 3 - One Hot Encoding Complete ...')

        # Step 2 - Null Value Impute
        imputer = Imputer(strategy='mean', copy=False)
        self.x_train = pd.DataFrame(data=imputer.fit_transform(self.x_train), columns=self.traincols)
        print('Step 4 - Null Value Imputation Complete ...')

        # Step 3 - Feature Scaling
        sc_X = scaler(copy=False)
        self.x_train[not_encoded_columns] = sc_X.fit_transform(self.x_train[not_encoded_columns])
        print('Step 5 - Standardisation Complete ...')

        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.x_train, self.y_train, test_size=0.2, random_state=1)
        print('Step 5 - Train Test Splitting Complete ...')

        print('Shape:' + str(self.x_train.shape))

        return self.df, self.x_train, self.y_train, self.x_test, self.y_test, self.traincols, self.categorical_columns

    def union(self, lst1, lst2):
        final_list = list(set(lst1) | set(lst2))
        return final_list

    def diff(self, first, second):
        second = set(second)
        return [item for item in first if item not in second]

    def get_training_columns(self, dataframe):

        # Get list of all training columns
        self.traincols = []
        for column in dataframe.columns:
            if (column != self.output_column_name):
                self.traincols.append(column)

    def get_categorical_columns(self):

        # Check DType and Reverse
        self.categorical_columns = []
        for column in self.df.columns:
            if (self.df[column].dtype != np.float64 and self.df[column].dtype != np.int64 and self.df[column].dtype != np.int32 and self.df[column].dtype != np.float32):
                self.categorical_columns.append(column)
