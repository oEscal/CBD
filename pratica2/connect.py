import pymongo

def connect(address, port, database):
   return pymongo.MongoClient(f"mongodb://{address}:{port}/")[database]
