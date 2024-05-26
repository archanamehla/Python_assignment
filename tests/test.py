import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..'))
from app.extract import read_datafile_to_datadict
from app.transform import transform_data


class TestCSVImport(unittest.TestCase):

    def test1_positive_read_datafile_to_datadict(self):
        file_path = "./tests/test-data.csv"

        expected_data = [
            {
                'FirstName': 'Rebbecca',
                'LastName': 'Didio',
                'Company': 'Brandt, Jonathan F Esq',
                'BirthDate': 16031989,
                'Salary': 330949.2034,
                'Address': '171 E 24th St',
                'Suburb': 'Leith',
                'State': 'TAS',
                'Post': 7315,
                'Phone': 381749123,
                'Mobile': 458665290,
                'Email': 'rebbecca.didio@didio.com.au'
            },
        ]

        actual_data = read_datafile_to_datadict(file_path)
        self.assertEqual(actual_data, expected_data)
        print("Positive tests passed: test1 for data extraction")

    def test2_negative_read_datafile_to_datadict(self):
        file_path = "./tests/test-data.csv"

        expected_data = [
            {
                'FirstName': 'fname',
                'LastName': 'lname',
                'Company': 'Brandt, Jonathan F Esq',
                'BirthDate': 16031989,
                'Salary': 330949.2034,
                'Address': '171 E 24th St',
                'Suburb': 'Leith',
                'State': 'TAS',
                'Post': 75,
                'Phone': 381723,
                'Mobile': 58665290,
                'Email': 'rebbecca.didio@didio.com.au'
            },
        ]

        actual_data = read_datafile_to_datadict(file_path)
        self.assertNotEqual(actual_data, expected_data)
        print("Negative tests passed: test2 for data extraction")


class TestTransformData(unittest.TestCase):
    input_data = [
        {
            'FirstName': 'John ',
            'LastName': ' Doe ',
            'Company': 'Brandt, Jonathan F Esq',
            'BirthDate': 16031989,
            'Salary': 330949.2034,
            'Address': '171 E 24th St',
            'Suburb': 'Leith',
            'State': 'TAS',
            'Post': 7315,
            'Phone': 381749123,
            'Mobile': 458665290,
            'Email': 'rebbecca.didio@didio.com.au'
        },
    ]
    transformed_data = transform_data(input_data)

    def test3_fullname_transformation(self):
        expected_fullname = 'John Doe'
        actual_fullname = self.transformed_data[0]['FullName']
        self.assertEqual(actual_fullname, expected_fullname)
        print("Positive tests passed: test3_fullname_transformation")

    def test4_age_transformation(self):
        expected_age = 34
        actual_age = self.transformed_data[0]['Age']
        self.assertEqual(actual_age, expected_age)
        print("Positive tests passed: test4_age_transformation")

    def test5_dateofbirth_transformation(self):
        expected_birthDate = '16/03/1989'
        actual_birthDate = self.transformed_data[0]['BirthDate']
        self.assertEqual(actual_birthDate, expected_birthDate)
        print("Positive tests passed: test5_dateofbirth_transformation")

    def test6_salarybucket_transformation(self):
        expected_salarybucket = 'A'
        actual_salarybucket = self.transformed_data[0]['SalaryBucket']
        self.assertEqual(actual_salarybucket, expected_salarybucket)
        print("Positive tests passed: test6_salarybucket_transformation")


if __name__ == '__main__':
    unittest.main()
