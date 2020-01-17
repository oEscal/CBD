
// Todos os utilizadores do sexo masculino
SELECT *
FROM movielens.users WHERE gender = 'M';

// O nome dos filmes de drama
SELECT name
FROM movielens.movies WHERE genres CONTAINS 'Drama';

// Utilizadores cujo código postal começa em 7
SELECT * 
FROM movielens.users WHERE zip LIKE '7%';

// Os ultimos 5 filmes com avaliação média de 4 ordenados em ordem decrescente pela data de saida
SELECT * 
FROM movielens.movies_per_rating_per_date 
WHERE avg_rating = 4
ORDER BY release_date DESC
LIMIT 5;

// Todos os filmes avaliados pelo utilizador com id 0
SELECT movie_id
FROM movielens.ratings_by_user WHERE user_id = 0;

// Todos os utilizadores que avaliaram o filme com id 0
SELECT user_id
FROM movielens.ratings_by_movie WHERE movie_id = 0;

// Todos as avaliações à Música dos filmes do utilizador com id 10
SELECT *
FROM movielens.ratings_by_user WHERE user_id = 10 and rating_per_area CONTAINS KEY 'Music';

// Todas as avaliações de 8
SELECT *
FROM movielens.ratings_by_user WHERE rating = 8;

// Filmes lançados em 2019
SELECT *
FROM movielens WHERE release_date > '2019-1-1' and release_date < '2019-12-21'
ALLOW FILTERING;

// Pessoas cuja cidade é Unknown 3
SELECT * 
FROM movielens.users WHERE city = 'Unknown 3';
