import csv


def read_datafile_to_datadict(file_path):
    data = []
    with open(file_path, 'r') as file:
        dataset = csv.reader(file, delimiter='|')
        for fields in dataset:
            data_dict = {
                'FirstName': fields[0] if fields[0] else None,
                'LastName': fields[1] if fields[1] else None,
                'Company': fields[2] if fields[2] else None,
                'BirthDate': int(fields[3]) if fields[3] else None,
                'Salary': float(fields[4]) if fields[4] else None,
                'Address': fields[5] if fields[5] else None,
                'Suburb': fields[6] if fields[6] else None,
                'State': fields[7] if fields[7] else None,
                'Post': int(fields[8]) if fields[8] else None,
                'Phone': int(fields[9]) if fields[9] else None,
                'Mobile': int(fields[10]) if fields[10] else None,
                'Email': fields[11] if fields[11] else None
            }
            data.append(data_dict)
    return data

# Printing the step1 result, each record separated by line

# for row in data:
#     print("\n")
#     for key, value in row.items():
#         print(f"{key}: {value}")
