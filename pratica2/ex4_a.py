import argparse
import pymongo as mongo

from connect import connect
from crud import *
from utils import *


def main(args):
   # connect
   db = connect(args.addr, args.port, args.database)
   collection = db[args.collection]

   if args.insert:
      if not args.file1:
         print("Error!\nYou must specify the json file where to read the inserts!")    
         exit()
         
      data = read_doc_bson(args.file1)
      verify_messages(insert_many(collection, data))
   elif args.clear_all:
      verify_messages(clear_all(collection))
   elif args.update:
      if not args.file1 or not args.file2:
         print("Error!\nYou must specify the json file where is the query (file1) and the json file where are the values to update (file2)!")    
         exit()

      data_query = read_doc_bson(args.file1)[0]
      data_values = read_doc_bson(args.file2)[0]

      verify_messages(update_many(collection, data_query, data_values))
   elif args.search:
      # in file, the first line is the query document and the second line is the projection document
      if not args.file1:
         print("Error!\nYou must specify the json file where to read the find query and projection!")    
         exit()

      data = read_doc_bson(args.file1)
      for result in find(collection, data[0], data[1]):
         print(result)


if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   
   parser.add_argument("--port", help="Port", type=int, default=27017)
   parser.add_argument("--addr", help="IP Address", default="128.0.0.1")
   parser.add_argument("--database", help="Database name", default="test")
   parser.add_argument("--collection", help="Collection name", default="test_collection")

   parser.add_argument("--file2", help="File 1")
   parser.add_argument("--file1", help="File 2")

   parser.add_argument("-i", "--insert", help="Insert from file", action="store_true")
   parser.add_argument("-u", "--update", help="Update from files", action="store_true")
   parser.add_argument("-s", "--search", help="Search from file", action="store_true")
   parser.add_argument("-c", "--clear_all", help="Clear all docs on a collection", action="store_true")
   
   args = parser.parse_args()
   main(args)
