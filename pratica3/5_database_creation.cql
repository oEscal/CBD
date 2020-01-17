
// keyspace creation
create keyspace if not exists restaurants with replication = {
    'class':'SimpleStrategy', 
    'replication_factor' : 3
};


// tables creation
create table restaurants.localidade(
    id int primary key, 
    nome text
);

create table restaurants.gastronomia(
    id int primary key, 
    nome text
);

create table restaurants.grade(
    rest_id int primary key, 
    date timestamp,
    grade_val varchar,
    score int
);

create table restaurants.address(
    building int primary key,
    latitude double,
    longitude double,
    road text,
    zipcode int
);

create table restaurants.restaurant(
    id int primary key,
    address_id int,
    grades_ids list<int>,
    localidade_id int,
    gastronomia_id int,
    nome text
);
