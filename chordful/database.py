import pymongo
from bson import ObjectId

class MongoDatabase:
    def __init__(self, address):
        client = pymongo.MongoClient(address)
        self.db = client.chordful

    def get_piece(self, pieceid):
        try:
            objid = ObjectId(pieceid)
            return self.db.pieces.find_one({"_id": objid})
        except Exception:
            return None

    def get_pieces(self, maxentries, startfrom=None):
        if not startfrom:
            q = self.db.pieces.find().limit(maxentries)
        else:
            q = self.db.pieces.find().skip(startfrom).limit(maxentries)

        if not q:
            return None

        ret = list(q)

        if len(ret) == 0:
            return None

        return ret

    def store_piece(self, piece):
        pieceid = self.db.pieces.insert_one(piece).inserted_id
        return pieceid

def initdb(config):
    dbconfig = config["database"]

    if dbconfig["type"] != "mongo":
        raise NotImplementedError

    return MongoDatabase(dbconfig["address"])
