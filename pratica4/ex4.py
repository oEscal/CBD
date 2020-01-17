from neo4j import GraphDatabase
import argparse

from utils import connect, query, save_file
from ex4_insert import insert



def query_1(graph):
   description = "Todas as reviews da Sophia"
   result = query(graph, 
                  """
                  match (u:User{name: "Sophia"})-[r:WROTE]->(rev:Review)
                  return rev.comments
                  """)

   return {description: [r for r in result]}

def query_2(graph):
   description = "A pessoa que escreveu a maior quantidade de reviews"
   result = query(graph, 
                  """
                  match (u:User)-[:WROTE]->(rev:Review)
                  with u as user, count(rev) as number
                  order by number desc
                  limit 1
                  return user, number
                  """)

   return {description: [r for r in result]}

def query_3(graph):
   description = "As informações de todas as marcações a que Paul deu review"
   result = query(graph, 
                  """
                  match (u:User{name: "Paul"})-[:WROTE]->(rev:Review)-[:REVIEWS]->(l:Listing)
                  return l as marcações
                  """)

   return {description: [r for r in result]}

def query_4(graph):
   description = "Os extras mais comuns dessas marcações ordenados por ordem decrescente"
   result = query(graph, 
                  """
                  match (u:User{name: "Paul"})-[:WROTE]->(Review)-[:REVIEWS]->(:Listing)-[:HAS]->(a:Amenity)
                  with a as amenity, count(*) as number
                  order by number desc
                  return amenity.name, number
                  """)

   return {description: [r for r in result]}

def query_5(graph):
   description = "Apresentar ao Paul hospedagens de acordo com as hospedagens já hospedadas por utilizadores" \
                  "que deram review ás mesmas que o Paul deu (os primeiros 20, para não ser uma pesquisa massiva)"
   result = query(graph, 
                  """
                  match (:User{name: "Paul"})-[:WROTE]->(:Review)-[:REVIEWS]->(l:Listing)
                  match (l)<-[:REVIEWS]-(:Review)<-[:WROTE]-(:User)-[:WROTE]->(:Review)-[:REVIEWS]->(:Listing)<-[:HOSTS]-(h:Host)
                  return h as hosts limit 20
                  """)

   return {description: [r for r in result]}

def query_6(graph):
   description = "Quais as vizinhanças onde há uma maior quantidade de hospedagens (apresentar as 10 primeiras)"
   result = query(graph, 
                  """
                  match (:Host)-[:HOSTS]->(:Listing)-[:IN_NEIGHBORHOOD]->(n:Neighborhood)
                  with n as neighborhood, count(n) as number
                  order by number desc
                  limit 10
                  return neighborhood, number
                  """)

   return {description: [r for r in result]}

def query_7(graph):
   description = "Apresentar o par de regalias que aparecem mais vezes em conjunto"
   result = query(graph, 
                  """
                  match (l:Listing)-[:HAS]->(a1:Amenity), (l:Listing)-[:HAS]->(a2:Amenity) 
                  with a1 as amenity1, a2 as amenity2, count(l) as number
                  order by number desc
                  limit 1
                  return amenity1, amenity2, number
                  """)

   return {description: [r for r in result]}

def query_8(graph):
   description = "Quantas hospedagens existem por cidade"
   result = query(graph, 
                  """
                  match (c:City)<-[:LOCATED_IN]-(:Neighborhood)<-[:IN_NEIGHBORHOOD]-(:Listing)<-[:HOSTS]-(h:Host)
                  with c as city, count(h) as number
                  order by number desc
                  return city, number
                  """)

   return {description: [r for r in result]}

def query_9(graph):
   description = "Os quartos em Sunset Valley cujo preço é menos de 20 (ordenados pelo preço (ordem crescente))"
   result = query(graph, 
                  """
                  match (:City{name: "Sunset Valley"})<-[:LOCATED_IN]-(:Neighborhood)<-[:IN_NEIGHBORHOOD]-(l:Listing)<-[:HOSTS]-(:Host)
                  where l.price < 20
                  return l as listing, l.price as price
                  order by l.price
                  """)

   return {description: [r for r in result]}

def query_10(graph):
   description = "As hospedagens em Sunset Valley onde o score por review médio é maior que 90 e que já receberam mais de 5 reviews"
   result = query(graph, 
                  """
                  match (:City{name: "Sunset Valley"})<-[:LOCATED_IN]-(:Neighborhood)<-[:IN_NEIGHBORHOOD]-(l:Listing)<-[:HOSTS]-(h:Host)
                  with h as host, avg(l.review_scores_rating) as score, count(l) as number
                  where score > 90 and number > 5
                  return host, score, number order by number desc
                  """)

   return {description: [r for r in result]}



def main(args):
   graph = connect()

   if args.insert:
      insert(graph)
   elif args.queries:
      result = {}
      result.update(query_1(graph))
      result.update(query_2(graph))
      result.update(query_3(graph))
      result.update(query_4(graph))
      result.update(query_5(graph))
      result.update(query_6(graph))
      result.update(query_7(graph))
      result.update(query_8(graph))
      result.update(query_9(graph))
      result.update(query_10(graph))

      save_file("CBD_L44c_output.txt", result)
      


if __name__ == "__main__":
   parser = argparse.ArgumentParser(description=f"Exercise 4 -> python script to insert data into graph and" 
                                                "make queries and save result to file")

   parser.add_argument('-i', "--insert", help="To insert data", action="store_true")
   parser.add_argument('-q', "--queries", help="To run queries and save result to file", action="store_true")
    
   args = parser.parse_args()
   main(args)
