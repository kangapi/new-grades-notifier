# Get the database using the method we defined in pymongo_test_insert file
import os

from pymongo import MongoClient
from pandas import DataFrame

class DB:
    def __init__(self, dbname, collection_name):
        self.url = os.getenv('MONGO_URL')
        self.dbname = dbname
        self.db = self.get_database()
        self.collection = self.db[collection_name]
        self.grades = self.pull_grades()

    def get_database(self):
        # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
        client = MongoClient(self.url)

        # Create the database for our example (we will use the same database throughout the tutorial
        return client['pronote']

    def pull_grades(self):
        return DataFrame(list(self.collection.find()))

    def get_grades(self):
        return self.grades

    def insert_grades(self, grades):
        self.collection.insert_many(grades)