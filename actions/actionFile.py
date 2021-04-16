



# # Making Connection



# # database


# # Created or Switched to collection
# # names: GeeksForGeeks
# Collection = db["sensorData"]


# def insert(data):

#     # Inserting the loaded data in the Collection
#     # if JSON contains data more than one entry
#     # insert_many is used else inser_one is used
#     # if isinstance(data, list):
#     #     Collection.insert_many(data)
#     # else:
    


import sys
import json
from pymongo import MongoClient
import dns

from st2common.runners.base_action import Action


uri = 'mongodb+srv://new_use:5TAnapiwTBJhkUf@cluster0.gaeaz.mongodb.net/register?retryWrites=true&w=majority'


class MyEchoAction(Action):
    def run(self, data):
        return(data)
        # myclient = MongoClient(uri)
        # db = myclient["stackstorm"]
        # Collection = db["sensorData"]

        
        # Collection.insert_one(data)
        # return (False, "No Data")

