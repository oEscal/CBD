from neo4j import GraphDatabase

url = "bolt://localhost:7687"
username = "neo4j"
password = "olaadeus"


def connect():
   return GraphDatabase.driver(url, auth=(username, password))

def query(graph, statement):
   try:
      with graph.session() as graph_session:
         return graph_session.run(statement)
   except Exception as e:
      print(f"Error running statement: {e}")
      return False

def save_file(file_name, result):
   try:
      with open(file_name, 'w') as file:
         number = 1
         for key in result:
            file.write(f"// {number} - {key}\n")
            file.write(f"{result[key]}\n\n\n")
            number += 1
   except Exception as e:
      print(f"Error saving results to file: {e}")
      return 

   print("Results saved with success")
