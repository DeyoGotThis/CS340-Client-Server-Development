# CRUD python module 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'deyocs340' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals'
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

            
    # Method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            result = self.database.animals.insert_one(data)  # data should be dictionary 
            return True
        else: 
            raise Exception("Nothing to save, because data parameter is empty")

    # Method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            result = list(self.database.animals.find(query)) # query returns list saved to variable
            return result
        return []
    
    # Method to implement the U in CRUD.
    def update(self, query, data):
        if data is not None:
            result = self.database.animals.update_many(query, data) # updates all docs with new data based on query
            print(result.matched_count)
            print(result.modified_count)
        else:
            raise Exception("Could not update records")
            
    # Method to implement the D in CRUD
    def delete(self, query):
        if query is not None:
            result = self.database.animals.delete_many(query) # deletes all docs based on query
            print(result.deleted_count)