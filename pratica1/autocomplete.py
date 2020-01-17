# perguntar ao stor porque é que com mset não dá quando damos import dum doc

import argparse
import redis
from utils import connect, bin_to_str_list
from autocomplete_utils import *

r = redis.Redis()

def search(first_part):
   return "\n".join(bin_to_str_list(r.zrangebylex(female_struct(), f"[{first_part}", f"[{first_part}z")))

def search_ordered(first_part):
   names = []
   for n in r.zscan_iter(portuguese_struct(), match=f"{first_part}*"):
      names.append(n)
   return "\n".join([f"{bytes.decode(n[0])}, {n[1]}" 
      for n in sorted(names, key=lambda x:-x[1])])

def insert_portuguese(file_name="nomes-registados-2018.csv"):
   file = open(file_name, "r")
   data = file.readlines()
   file.close()

   for p in data:
      current_p = p.split(",")
      r.zadd(portuguese_struct(), {current_p[0]: current_p[2].replace("\n", "")})
   print("Done")

def insert_female_names(file_name="female-names.txt"):
   file = open(file_name, "r")
   data = file.readlines()
   file.close()

   for p in data:
      r.zadd(female_struct(), {p.replace("\n", ""): 0})
   print("Done")

def main(args):
   connect("localhost")

   if args.insert_female_names:
      insert_female_names()

   if args.insert_portuguese:
      insert_portuguese()

   while True:
      search_str = input("Search for ('Enter' for quit): ")
      if len(search_str) == 0:
         break
      print(f"{search_ordered(search_str) if args.ordered else search(search_str)}\n")
      
      
   

if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   group = parser.add_mutually_exclusive_group(required=True)
   
   group.add_argument("-n", "--normal", help="Normal search just for female", action="store_true")
   group.add_argument("-o", "--ordered", help="Ordered search for all portuguese people", action="store_true")
   parser.add_argument("-i", "--insert_portuguese", help="Insert all portuguese names", action="store_true")
   parser.add_argument("-f", "--insert_female_names", help="Insert all female names", action="store_true")
   args = parser.parse_args()

   main(args)
