
/********************************* update *********************************/
// alterar a idade do utilizador com id = 1
update movielens.users set age=25 where id=1;

// adicionar mais um valor à lista de reviews do filme com id = 1
update movielens.movies set reviews = reviews + ['Hmmmm'] where id=1;

// alterar a 2ª review existente na lista de reviews (só dá se houver pelo menos duas reviews na lista)
update movielens.movies set reviews[1] = 'ola' where id=1;

// alterar o valor de Acting do mapa dos ratings per area para o filme com id 0 e para o utilizador com id 32
update movielens.ratings_by_movie set rating_per_area['Acting'] = 10 where movie_id = 0 and user_id = 32;

// alterar os dados no mapa rating_per_area de forma a que este tenha apenas a chave 'ola' com o valor 1
update movielens.ratings_by_movie set rating_per_area = {'ola': 1} where movie_id = 0 and user_id = 32;


/********************************* delete *********************************/
// eleminar a entrada cuja chave tem o valor 'Acting' do mapa rating_per_area
delete rating_per_area['Acting'] from movielens.ratings_by_movie where movie_id = 0 and user_id = 32;

// eliminar o segundo valor da lista de reviews do filme com id = 1
delete reviews[1] from movielens.movies where id=1;

// remover todas as entradas da lista de reviews cujo valor é igual a 'adeus'
update movielens.movies set reviews = reviews - ['adeus'] where id=1;

// eliminar o valor da coluna age do user com id = 1
delete age from movielens.users where id=1;

// uma das formas de elminar o set genres do movie com id = 20
update movielens.movies set genres = {} where id = 20;
