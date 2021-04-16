import json
from pymongo import MongoClient
import dns

# Making Connection
uri = 'mongodb+srv://new_use:5TAnapiwTBJhkUf@cluster0.gaeaz.mongodb.net/register?retryWrites=true&w=majority'
myclient = MongoClient(uri)

# database
db = myclient["stackstorm"]

# Created or Switched to collection
# names: GeeksForGeeks
Collection = db["sensorData"]


def insert(data):

    # Inserting the loaded data in the Collection
    # if JSON contains data more than one entry
    # insert_many is used else inser_one is used
    # if isinstance(data, list):
    #     Collection.insert_many(data)
    # else:
    Collection.insert_one(data)
