import sys
import json
from pymongo import MongoClient
import dns
from bson.objectid import ObjectId

from st2common.runners.base_action import Action





class MyEchoAction(Action):
    def run(self, id, uri, collectionDatabase):
        
        database = uri.split("/")[3].split("?")[0]
        
        myclient = MongoClient(uri)
        db = myclient[database]
        collection = db[collectionDatabase]

        collection.delete_one({'_id': ObjectId(id)})
        return (True, "deleted")

