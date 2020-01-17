import redis 

def connect(url):
   connection = redis.Connection(url)
   print(f"{connection}\n\n\n")

def bin_to_str_list(l):
   return [el.decode("utf-8") for el in l]