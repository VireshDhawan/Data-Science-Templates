from DataPreprocessing.Preprocessing import DataPreprocess
import time


class Engine:
    # Problem Types => regression / classification / image classification / nlp /

    var_problemtype = 'classification'
    var_train_file_path = 'Data/Input/train.csv'
    var_test_file_path = 'Data/Input/test.csv'
    output_column_name = 'median_house_value'

    def initiate(self):
        # Step 1 - Read and Intelligently Preprocess Data
        dpp = DataPreprocess(self.var_train_file_path, self.output_column_name)
        self.train_data = dpp.read_and_preprocess_data()

        if (self.train_data == 404):
            return


if __name__ == "__main__":
    t0 = time.time()
    print('Initialising ---')

    Engine().initiate()
    print('Initialising done in : ' + str(time.time() - t0) + ' seconds')

    # Step 2 - Intelligently Show Relationships
    # 2.1 - Show Influencers
    # 2.2 - Show Data Corelation
    # 2.3 - Show 2D Graph of All Column vs Result

    # Step 3 - Show All Baseline Scores by Generic Algorithms

    # Step 4 - Show All Baseline
