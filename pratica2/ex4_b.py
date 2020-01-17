import argparse
import pymongo as mongo
import time

from connect import connect
from crud import *
from utils import *


def find_query_time(collection, query):
    init_time = time.time()
    find(collection, query, {})
    print(f" -> Total time: {time.time() - init_time}s")
    

def main(args):
   # connect
   db = connect(args.addr, args.port, args.database)
   collection = db[args.collection]

   if args.locality:
      query = {"localidade": "Bronx"}

      print("Without indices:")
      find_query_time(collection, query)

      print("With indices:")
      collection.create_index([("localidade", mongo.DESCENDING)])
      find_query_time(collection, query)
   elif args.gastronomy:
      query = {"gastronomia": "Bakery"}

      print("Without indices:")
      find_query_time(collection, query)

      print("With indices:")
      collection.create_index([("gastronomia", mongo.DESCENDING)])
      find_query_time(collection, query)
   elif args.name:
      query = {"nome": "Chopstix Restaurant"}

      print("Without indices:")
      find_query_time(collection, query)

      print("With indices:")
      collection.create_index([("nome", mongo.TEXT)])
      find_query_time(collection, query)


if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   
   parser.add_argument("--port", help="Port", type=int, default=27017)
   parser.add_argument("--addr", help="IP Address", default="128.0.0.1")
   parser.add_argument("--database", help="Database name", default="test")
   parser.add_argument("--collection", help="Collection name", default="test_collection")

   parser.add_argument("-l", "--locality", help="Test locality indices", action="store_true")
   parser.add_argument("-g", "--gastronomy", help="Test gastronomy indices", action="store_true")
   parser.add_argument("-n", "--name", help="Test name indices", action="store_true")
   
   args = parser.parse_args()
   main(args)
