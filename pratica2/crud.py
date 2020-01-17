import pymongo as mongo

def insert_many(collection, docs_list):
    return collection.insert_many(docs_list)

def update_many(collection, query, values):
    return collection.update_many(query, values)

def find(collection, query, projection):
    return collection.find(query, projection)

def aggregate(collection, pipeline):
    return collection.aggregate(pipeline)

def clear_all(collection):
    return collection.delete_many({}) 