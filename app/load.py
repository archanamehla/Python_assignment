import json

from pymongo import MongoClient


def load_data_to_file(processed_data):
    # write the transformed data into a json file
    output_file = 'transformed_data.json'
    with open(output_file, 'w') as json_file:
        json.dump(processed_data, json_file, indent=4)


def load_data_to_database(processed_data):
    client = MongoClient('mongo', 27017)
    db = client.assignment
    collection = db.assignment
    print("Connected to MongoDB database")
    # Delete data incase multiple execution
    # db.collection.delete_many({})
    # write the transformed data into mongoDb
    collection.insert_many(processed_data)
