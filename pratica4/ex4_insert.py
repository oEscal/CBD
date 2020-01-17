from utils import query


def insert(graph):
   with open("ex4_data/import.cyp") as file:
      statements = file.read()

   for statement in statements.split(';'):
      if statement:
         if not query(graph, statement):
            return

   print("All data inserted with success")
