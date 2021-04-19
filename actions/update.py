import sys
import json
from pymongo import MongoClient
import dns
from bson.objectid import ObjectId

from st2common.runners.base_action import Action




class MyEchoAction(Action):
    def run(self, data, id, uri):

        myclient = MongoClient(uri)
        db = myclient["stackstorm"]
        collection = db["sensorData"]
                
        collection.find_one_and_update(
            {"_id" : ObjectId(id)},
                {"$set":data},
                upsert=True
            )

        return (True, data)

