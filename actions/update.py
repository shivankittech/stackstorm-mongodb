import sys
import json
from pymongo import MongoClient
import dns
from bson.objectid import ObjectId

from st2common.runners.base_action import Action




class MongoUpdateAction(Action):
    def run(self, data, databaseId, uri, collectionDatabase):

        database = uri.split("/")[3].split("?")[0]
        
        myclient = MongoClient(uri)
        db = myclient[database]
        collection = db[collectionDatabase]
                
        collection.find_one_and_update(
            {"_id" : ObjectId(databaseId)},
                {"$set":data},
                upsert=True
            )

        return (True, uri)

