import os
import sys
from extract import read_datafile_to_datadict
from transform import transform_data
from load import load_data_to_file, load_data_to_database

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..'))
import tests.test as mytest

file_path = 'member-data.csv'

print("Current Working Directory:", os.getcwd())
if __name__ == '__main__':
    # Extract
    data = read_datafile_to_datadict(file_path)
    print("step1:   File read is completed")
    # Transform
    transformed_data = transform_data(data)
    print("step2:   Data Transform is completed")

    # Load
    load_data_to_file(transformed_data)
    print("step3.1:   Data written to json file")
    # load_data_to_database(transformed_data)
    print("step3.2:   Data written to mongo database")

    # trigger tests
    mytest.TestCSVImport().test1_positive_read_datafile_to_datadict()
    mytest.TestCSVImport().test2_negative_read_datafile_to_datadict()
    mytest.TestTransformData().test3_fullname_transformation()
    mytest.TestTransformData().test4_age_transformation()
    mytest.TestTransformData().test5_dateofbirth_transformation()
    mytest.TestTransformData().test6_salarybucket_transformation()
