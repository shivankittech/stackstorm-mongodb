import sys
import json
from pymongo import MongoClient
import dns

from st2common.runners.base_action import Action



# mongodb+srv://new_use:5TAnapiwTBJhkUf@cluster0.gaeaz.mongodb.net/register?retryWrites=true&w=majority

class MongoInsetAction(Action):
    def run(self, data, uri, collectionDatabase):

        database = uri.split("/")[3].split("?")[0]

        myclient = MongoClient(uri)
        db = myclient[database]
        collection_databse = db[collectionDatabase]

        
        collection_databse.insert_one(data)
        return (True, data)

