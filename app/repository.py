from bson.json_util import dumps
import json

class MongoCollectionRepository():
    def __init__(self, session, collection_name):
        self.collection = session[collection_name]

    def add(self, batch):
        return self.collection.insert_one(batch)

    def get(self, note_id):
        cursor = self.collection.find({'_id': note_id})
        ret = json.loads(dumps(cursor))[0]
        return ret
        
