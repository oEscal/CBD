// load projects
load csv with headers from 'file:///git_projects.csv' as row
with toInteger(row.num) as num, row.organization as organization, row.project_name as project_name
merge (p:Project{name: project_name})
set p.organization = organization
return count(p);

// load persons
load csv with headers from 'file:///git_persons.csv' as row
with row.svn_id as svn_id, row.real_name as real_name
merge (p:Person{id: svn_id})
set p.name = real_name
return count(p);

// load relations
load csv with headers from 'file:///git_relations.csv' as row
with toInteger(row.num) as num, row.project_name as pr_name, row.svn_id as pers, row.role_on_project as role_on_project
match (pr:Project{name:pr_name})
match (per:Person{id:pers})
merge (per)-[rel:PARTICIPATE{id: num, role: role_on_project}]->(pr)
return count(rel);


// 1
match(p:Person)
return p

// 2
match(p:Person)
return p.name

// 3
match (:Person)-[:PARTICIPATE]->(p:Project)
return p

// 4
match(p:Person)-[:PARTICIPATE]->(pr:Project)
with p as person, count(pr) as number_pr
return person.name, number_pr

// 5
match(p:Person)-[:PARTICIPATE]->(pr:Project)
with p as person, count(pr) as number_pr
order by number_pr desc
return person.name, number_pr

// 6
match(p:Person)-[:PARTICIPATE]->(pr:Project)
with pr as project, count(p) as number_persons
return project, number_persons

// 7
match(:Person)-[r:PARTICIPATE{role: "Committer"}]->(pr:Project)
with pr as project, count(r) as number
return project, number

// 8
match (p:Person{id: "atm"})-[:PARTICIPATE]->(pr:Project), (p2:Person)-[:PARTICIPATE]->(pr)
return p.name as atm, p2.name as person_2, pr.name as project

// 9
match (p:Person{id: "atm"})-[:PARTICIPATE{role: "PMC"}]->(pr:Project), (p2:Person)-[:PARTICIPATE{role: "Committer"}]->(pr)
return p2
