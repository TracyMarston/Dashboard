import pymongo
from pymongo import MongoClient 
from bson.objectid import ObjectId 
from datetime import datetime
import urllib.parse
from bson.objectid import ObjectId



       
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        #username = "aacuser"
        #password = "password"
        self.client = MongoClient('mongodb://%s:%s@localhost:45236/AAC' % (username, password))
        self.database = self.client['AAC']
        


    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary 
            print("True: Insert was Sucessful!")
           
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD.
    def read(self, query):
        if query is not None:
            results = self.database.animals.find(query, {"_id":False})
            return results
        
            
        
            
     #Create Method to implement the U in CRUD
    def update(self, find, replaceValues):
        if find is not None:
            self.database.animals.update_one(find, replaceValues)
            for x in self.database.animals.find():
                print(x)
           
        else:
            raise Exception("Nothing to update, because data parameter is empty") 
    
    #Creates Method to implement the D in CRUD
    def delete(self, deleteData):
        if deleteData is not None:
            self.database.animals.delete_one(deleteData)            
        else:
            raise Exception("Nothing to delete, because project parameter is None")
            