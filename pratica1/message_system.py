import redis
import argparse
from utils import connect, bin_to_str_list
from message_utils import *

r = redis.Redis()

def print_list(list_users):
   for u in list_users:
      print(f" - {u}")

def user_exists(name):
   return r.sismember(name_struct(), name)

def new_user(name):
   if user_exists(name):
      return False

   # add new user to users's list
   r.sadd(name_struct(), name)
   return True

def get_all_users():
   return r.smembers(name_struct())

def subscribe(user, target):
   if not user_exists(user):
      return False, "Error!\nUser does not exist"
   if not user_exists(target):
      return False, "Error!\nTarget does not exist"

   r.sadd(subscriptions_struct(user), target)
   return True, "Success"

def store_msg(user, msg):
   if not user_exists(user):
      return False, "Error!\nUser does not exist"
   
   r.sadd(message_struct(), msg)
   return True, "Message stored with success"

def subscriptions(user):
   if not user_exists(user):
      return False, "Error!\nUser does not exist"
   
   return True, r.smembers(subscriptions_struct(user))

def get_messages_from(user):
   if not user_exists(user):
      return False, "Error!\nUser does not exist"

   return True, r.smembers(message_struct())

def list_subscribed_messages(user):
   if not user_exists(user):
      return False, "Error!\nUser does not exist"
   
   result = {}
   subs = subscriptions(user)
   for u in bin_to_str_list(subs[1]):
      result[u] = bin_to_str_list(get_messages_from(u)[1])
   
   return True, result


def main(args):   
   connect("localhost")

   if args.new_user:
      if new_user(input("User name: ")):
         print("Success")
      else:
         print("Error!\nThere are already a user with that name!")
   if args.all_users:
      print("List of users:")
      print_list(bin_to_str_list(get_all_users()))
   if args.subscribe:
      print(f"\n\n\n{subscribe(input('Your name: '), input('Target name: '))[1]}")
   if args.store_message:
      print(f"\n\n\n{store_msg(input('Your name: '), input('Message: '))[1]}")
   if args.who_ami_following:
      subs = subscriptions(input('Your name: '))
      if subs[0]:
         print("\n\n\nYour subscriptions:")
         print_list(bin_to_str_list(subs[1]))
      else:
         print(f"\n\n\n{subs[1]}")
   if args.get_my_messages:
      mess = get_messages_from(input('Your name: '))
      if mess[0]:
         print("\n\n\nYour messages:")
         print_list(bin_to_str_list(mess[1]))
      else:
         print(f"\n\n\n{mess[1]}")
   if args.list_subscribed_messages:
      mess = list_subscribed_messages(input('Your name: '))
      if mess[0]:
         print("\n\n\nYour inbox:")
         for u in mess[1]:
            print(f"\tMessages from {u}:")
            for m in mess[1][u]:
               print(f"\t\t- {m}")
      else:
         print(f"\n\n\n{mess[1]}")
   

if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   
   parser.add_argument("-n", "--new_user", help="Create new user", action="store_true")
   parser.add_argument("-a", "--all_users", help="Get all users", action="store_true")
   parser.add_argument("-s", "--subscribe", help="Subscribe to a user", action="store_true")
   parser.add_argument("-m", "--store_message", help="Store new message", action="store_true")
   parser.add_argument("-w", "--who_ami_following", help="Get a list of the users to which I am subscribed", action="store_true")
   parser.add_argument("-g", "--get_my_messages", help="Get a list of the messages that I stored", action="store_true")
   parser.add_argument("-l", "--list_subscribed_messages", help="Get a list of the messages stored by the users which I am subscribed to", action="store_true")
   args = parser.parse_args()

   main(args)
