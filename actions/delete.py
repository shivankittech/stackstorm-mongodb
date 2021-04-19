import sys
import json
from pymongo import MongoClient
import dns
from bson.objectid import ObjectId

from st2common.runners.base_action import Action


uri = 'mongodb+srv://new_use:5TAnapiwTBJhkUf@cluster0.gaeaz.mongodb.net/register?retryWrites=true&w=majority'


class MyEchoAction(Action):
    def run(self, data, id):

        myclient = MongoClient(uri)
        db = myclient["stackstorm"]
        collection = db["sensorData"]

        collection.delete_one({'_id': ObjectId(id)})
        return (True, "deleted")

