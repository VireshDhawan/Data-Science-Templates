import pandas as pd
from Utils.database import Database

db = Database()
import os

class DataPreprocess:

    def __init__(self, input_file, output_column_name):
        self.input_file = input_file
        self.output_column_name = output_column_name

    def insert_data_into_sql(self):

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
        base_path = os.getcwd().replace('\\','/') + '/'
        load_command = "LOAD DATA LOCAL INFILE '" + base_path + self.input_file + \
                       "' INTO TABLE train FIELDS TERMINATED BY ',' " \
                       "LINES TERMINATED BY '\\n' " \
                       "IGNORE 1 LINES (" + collist

        db.execute_query_with_params(load_command, {})
        return

    def read_and_preprocess_data(self):
        # Read File
        print(self.input_file)
        try:
            self.df = pd.read_csv(self.input_file)
        except FileNotFoundError:
            print('Error: File Not Found')
            return 404

        # Insert Into SQL
        self.insert_data_into_sql()

        # Break Down Input and Output Columns
        self.traincols = []
        for column in self.df.columns:
            if (column != self.output_column_name):
                self.traincols.append(column)
        self.x_train = self.df[self.traincols]
        self.y_train = self.df[self.output_column_name]

        # Start Preprocessing
        self.preprocess_data()

    def preprocess_data(self):
        # Step 1 - Detect Column Types

        # Step 2 - Null Value Impute

        return self.df
