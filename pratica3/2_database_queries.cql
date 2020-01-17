/********************** c) **********************/
// c) - 7
SELECT *
FROM videos.video_per_author WHERE user_id = 0;

// c) - 8
SELECT *
FROM videos.comentario_per_author_per_data WHERE user_id = 2
ORDER BY data DESC;

// c) - 9
SELECT *
FROM videos.comentario_per_video_per_data WHERE video_id = 3
ORDER BY data DESC;

// c) - 10

SELECT *
FROM videos.video_per_rating WHERE ratings_avg > 3 and ratings_len > 3
allow filtering;


/********************** d) **********************/
// d) - 1
SELECT * 
FROM videos.comentario_per_video_per_data WHERE video_id = 23
ORDER BY data DESC
LIMIT 3;

// d) - 2
// da forma como desenhei a base de dados, só é possível obter os ids das tags. Caso tivesse
// permitido que as tags fossem adicionadas diretamente ao set na tabela dos videos, seria
// possível obter diretamente o nome destas (seria a mesma query mostrada abaixo)
SELECT etiqueta_id
FROM videos.video WHERE id = 1;

// d) - 3
// Como explicado acima, no meu desenho não dá, a não ser que se possua o id da tag Aveiro.
// Supondo então que o id de Aveiro é 1:
SELECT *
FROM videos.video WHERE etiqueta_id CONTAINS 1;

// d) - 4
SELECT *
FROM videos.evento_per_user WHERE user_id = 8 and video_id = 15
ORDER BY data DESC
LIMIT 5;

// d) - 5
// Dá, se possuir o id do utilizador
SELECT * 
FROM videos.video_per_author 
WHERE user_id = 0 and data_upload > '2019-12-01' and data_upload < '2019-12-24'
ALLOW FILTERING;

// d) - 6
// é impossivel, já que tem de haver uma clausula where com a partition key para se poder ordenar os resultados
// duma query. sendo que nesta query não pedem nenhuma seleção dos dados, mas sim só os dados ordenados, é impossivel
// realizar a query.

// d) - 7
// Como tenho desenhada a bd, só dá para obter os ids dos utilizadores
SELECT followers_ids
FROM videos.video WHERE id = 0;

// d) - 8
// da forma como tenho desenhada a base de dados é impossivel (seria necessário um join, algo que não é 
// suportado por cassandra). para ser possivel, teriam de se ter os comentários na tabela dos videos

// d) - 9
// é impossivel, já que tem de haver uma clausula where com a partition key para se poder ordenar os resultados
// duma query. sendo que nesta query não pedem nenhuma seleção dos dados, mas sim só os dados ordenados, é impossivel
// realizar a query.

// d) - 10
// com esta query é possivel observar que, para um mesmo mesmo valor de ratings_avg, 
// os ratings_len se encontram ordenador por ordem crescente e, para um mesmo valor 
// de ratings_len, os valores de id se econtram ordenados por ordem crescente
SELECT *
FROM videos.video_per_rating;

// d) - 11
// é impossivel, seria necessário fazer um join, ou criar uma tabela com todas as informações dos videos e dos tags
