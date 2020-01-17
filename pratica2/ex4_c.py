import argparse
import pymongo as mongo
from bson import json_util

from connect import connect
from crud import *
from utils import *


def countLocalidades(collection):
    result = aggregate(collection, [
        {
            "$group": {
                "_id": "null", 
                "loc": {
                    "$addToSet": "$localidade"
                }
            }
        }, 
        {
            "$unwind": "$loc"
        }, 
        {
            "$group": {
                "_id": "null", "count": {
                    "$sum": 1
                    }
            }
        }
    ])

    return dump_result(result)[0]['count']

def countRestByLocalidade(collection):
   result = aggregate(collection, [
      {
         "$group": {
            "_id": "$localidade", 
            "number": {
               "$sum": 1
            }
         }
      }
   ])

   return {r['_id']: r['number'] for r in dump_result(result)}

def countRestByLocalidadeByGastronomia(collection):
   result = aggregate(collection, [
      {
         "$group": {
            "_id": {
               "localidade": "$localidade", 
               "gastronomia": "$gastronomia"
            }, 
            "number": {
               "$sum": 1
            }
         }
      }
   ])

   return {f"{r['_id']['localidade']} | {r['_id']['gastronomia']}": r['number'] for r in dump_result(result)}

def getRestWithNameCloserTo(collection, name):
   result = find(collection, {"nome": {"$regex": f".*{name}.*"}}, {"nome": 1})
   return [r["nome"] for r in result]


def main(args):
   # connect
   db = connect(args.addr, args.port, args.database)
   collection = db[args.collection]

   if args.localidades:
      print(f"Número de localidades distintas: {countLocalidades(collection)}")
   elif args.rest_local:
      print_map("Numero de restaurantes por localidade:", countRestByLocalidade(collection))
   elif args.rest_local_gast:
      print_map("Numero de restaurantes por localidade e gastronomia:", countRestByLocalidadeByGastronomia(collection))
   elif args.search_rest:
      search_str = input("Search: ")
      
      print(f"Nome de restaurantes contendo '{search_str}' no nome: ")
      for restaurant in getRestWithNameCloserTo(collection, search_str):
         print(f" -> {restaurant}")


if __name__ == "__main__":
   parser = argparse.ArgumentParser()

   parser.add_argument("--port", help="Port", type=int, default=27017)
   parser.add_argument("--addr", help="IP Address", default="128.0.0.1")
   parser.add_argument("--database", help="Database name", default="test")
   parser.add_argument("--collection", help="Collection name", default="test_collection")
   
   parser.add_argument("-l", "--localidades", help="Number of distinct localities", action="store_true")
   parser.add_argument("-r", "--rest_local", help="Number of restaurants per locality", action="store_true")
   parser.add_argument("-g", "--rest_local_gast", help="Number of restaurant per locality per gastronomy", action="store_true")
   parser.add_argument("-s", "--search_rest", help="Search restaurant by name", action="store_true")
   
   args = parser.parse_args()
   main(args)
