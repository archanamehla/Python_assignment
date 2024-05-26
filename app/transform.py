from datetime import datetime


class Address:
    def __init__(self, street, suburb, state, postal_code):
        self.street = street
        self.suburb = suburb
        self.state = state
        self.postal_code = postal_code


def transform_data(data):
    transformed_data = []

    for row in data:
        # Cleaning and merging FirstName and LastName
        row['FirstName'] = row['FirstName'].strip()
        row['LastName'] = row['LastName'].strip()
        row['FullName'] = row['FirstName'] + ' ' + row['LastName']

        # member.csv has null birthdate for some records, transform data if DOB exists else age is none
        if row['BirthDate']:
            birth_date = str(row['BirthDate'])
            formatted_birth_date = f"{birth_date[-8:-6]}/{birth_date[-6:-4]}/{birth_date[-4:]}"
            row['BirthDate'] = formatted_birth_date
            birth_date = datetime.strptime(row['BirthDate'], '%d/%m/%Y')
            reference_date = datetime.strptime('01/03/2024', '%d/%m/%Y')
            age = reference_date.year - birth_date.year - (
                    (reference_date.month, reference_date.day) < (birth_date.month, birth_date.day))
            row['Age'] = age
        else:
            row['Age'] = None

        # categorize SalaryBucket
        if int(row['Salary']) < 500000:
            row['SalaryBucket'] = 'A'
        elif 500000 <= int(row['Salary']) < 1000000:
            row['SalaryBucket'] = 'B'
        else:
            row['SalaryBucket'] = 'C'

        row['Salary'] = "${:,.2f}".format(row['Salary'])

        # Drop FirstName and LastName columns
        del row['FirstName']
        del row['LastName']

        # Create Address object
        address_obj = Address(row['Address'], row['Suburb'], row['State'], row['Post'])
        row['Address'] = address_obj.__dict__  # Address to dictionary

        transformed_data.append(row)

    return transformed_data
