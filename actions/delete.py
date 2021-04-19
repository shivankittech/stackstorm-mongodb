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

        collection.delete_one({'_id': ObjectId(id)})
        return (True, "deleted")

