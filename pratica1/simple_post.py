import argparse
import redis
from utils import connect

r = redis.Redis()

# key set for user's name
USERS = "users"

def save_user(all_users):
   r.sadd(USERS, *all_users)

def get_user():
   return r.smembers(USERS)

def get_all_keys():
   return r.keys("*")


def main(args):   
   connect("localhost")

   if args.add:
      # list some users
      users = {"Ana", "Pedro", "Maria", "Luis"}
      save_user(users)
   
      print("Utilizadores adicionados com sucesso!")

   if args.users:   
      print(f"Users: {get_user()}")

   if args.keys:   
      print(f"Keys: {get_all_keys()}")

if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument("-a", "--add", help="Add users to redis", action="store_true")
   parser.add_argument("-u", "--users", help="Get redis users", action="store_true")
   parser.add_argument("-k", "--keys", help="Get redis keys", action="store_true")
   args = parser.parse_args()

   main(args)


