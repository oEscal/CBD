
// keyspace creation
create keyspace if not exists movielens with replication = {
    'class':'SimpleStrategy', 
    'replication_factor' : 3
};


CREATE TABLE movielens.movies (
    id int PRIMARY KEY,
    avg_rating float,
    genres set<text>,
    name text,
    release_date date,
    url text,
    reviews list<text>
);
CREATE INDEX movies_genres ON movielens.movies (genres);

CREATE TABLE movielens.users (
    id int PRIMARY KEY,
    address text,
    age int,
    city text,
    gender text,
    name text,
    occupation text,
    zip text
);
CREATE CUSTOM INDEX user_zip ON movielens.users (zip) 
USING 'org.apache.cassandra.index.sasi.SASIIndex';
CREATE INDEX user_gender ON movielens.users (gender);
CREATE INDEX user_city ON movielens.users (city);

CREATE TABLE movielens.ratings_by_user (  
    user_id int,
    movie_id int,
    name text,
    rating int,
    rating_per_area map<text, int>,
    PRIMARY KEY (user_id, movie_id)
) WITH CLUSTERING ORDER BY (movie_id ASC);
CREATE INDEX rating_a ON movielens.ratings_by_user (KEYS (rating_per_area));
CREATE INDEX rating_user ON movielens.ratings_by_user (rating);

CREATE TABLE movielens.ratings_by_movie (
    movie_id int,
    user_id int,
    rating int,
    rating_per_area map<text, int>,
    PRIMARY KEY (movie_id, user_id)
) WITH CLUSTERING ORDER BY (user_id ASC);
CREATE INDEX rating_movie ON movielens.ratings_by_movie (rating);

CREATE TABLE movielens.movies_per_rating_per_date (
    id int,
    avg_rating float,
    genres set<text>,
    name text,
    release_date date,
    url text,
    reviews list<text>,

    PRIMARY KEY (avg_rating, release_date, id)
) WITH CLUSTERING ORDER BY (release_date ASC);
