
// 1
match (a:Person)-[:ACTED_IN]->(b:Movie), (a)-[:DIRECTED]->(b) 
with a as actor, b as movie 
return actor['name'], movie['title'];

// 2
match (a:Person)-[:ACTED_IN]->(m:Movie)
where m.released > 2005
return m.title, a.name;

// 3
match (a)-[r]->(b)
with a as entity_a, b as entity_b, count(r) as number_rel
where number_rel > 1
return [entity_a, entity_b];

// 4
match (p:Person)-[:REVIEWED]->(m:Movie), (p1:Person)-[:REVIEWED]->(m)
with p as person_a, p1 as person_b, m as movie
return [person_a.name, person_b.name, movie.title];

// 5
match (p:Person)-[:ACTED_IN]->(m:Movie), (p1:Person)-[:ACTED_IN]->(m)
with p as person_a, p1 as person_b, count(m) as number_movies
where number_movies > 1
return [person_a.name, person_b.name, number_movies];

// 6
match (p:Person)-[:ACTED_IN]->(m:Movie)
where m.title =~ 'Apollo 13'
return avg(m.released - p.born);

// 7
match (p:Person)-[:ACTED_IN]->(m:Movie)
with m as movie, avg(m.released - p.born) as avg_age
order by avg_age desc
limit 10
return movie, avg_age;

// 8
match (p:Person)-[:ACTED_IN]->(m:Movie)
with m as movie, avg(m.released - p.born) as avg_age
order by avg_age
limit 1
match (p1)-[a:ACTED_IN]->(movie)
return a;

// 9
match (a:Person {name: 'John Cusack'}), (b:Person {name: 'Demi Moore'}), p = shortestPath((a)-[*]-(b))
with p
return p;

// 10
match (a:Person {name: 'Keanu Reeves'}), (b:Person {name: 'Tom Cruise'}), p = shortestPath((a)-[*]-(b))
with p
return length(p);

// 11
match (a) match (b)
where a.name =~ '.*Jim.*' and b.name =~ '.*Kevin.*'
match p = shortestPath((a)-[*]-(b))
with min(length(p)) as min_len
return min_len;

// 12
match (a:Person)-[*2]-(:Person{name: 'Jim Cash'})
return a;

// 13
match (a:Person) match (b:Person {name: 'Kevin Bacon'})
where a.name <> b.name
match p = shortestPath((a)-[*]-(b))
with length(p) as len_path
order by len_path desc
limit 1
return len_path;

// 14
match (a:Person) match (b:Person)
where a.name <> b.name
match p = shortestPath((a)-[*]-(b))
with length(p) as len_path
order by len_path desc
limit 1
return len_path;

// 15
match (a:Person) match (b:Person)
where a.name <> b.name
match p = shortestPath((a)-[*]-(b))
with length(p) as len_path, count(length(p)) as count_len
order by count_len desc
return len_path, count_len;

// 16
match (a:Person) match (b:Person)
where a.name <> b.name
match p = shortestPath((a)-[:ACTED_IN*]-(b))
with length(p) as len_path, a as first, b as second
order by len_path
limit 10
return first, second, len_path;
