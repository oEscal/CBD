
// keyspace creation
create keyspace if not exists videos with replication = {
    'class':'SimpleStrategy', 
    'replication_factor' : 3
};


// tables creation
create table videos.utilizador(
    id int primary key,
    username text,
    nome text,
    email text,
    data_registo timestamp
);

create table videos.video(
    id int,
    nome text,
    descricao text,
    data_upload timestamp,
    
    user_id int,
    followers_ids set<int>,
    ratings_sum int,
    ratings_len int,
    ratings_avg float,
    etiqueta_id set<int>,

    primary key (id, data_upload)
) with clustering order by (data_upload DESC);
CREATE INDEX ON videos.video (etiqueta_id);

create table videos.comentario(
    id int primary key,
    conteudo text,
    data timestamp,

    video_id int,
    user_id int
);

create table videos.tipo_evento(
    id int primary key,
    nome text
);

create table videos.evento(
    id int primary key,
    data timestamp,
    tempo_video int,

    video_id int,
    user_id int,
    event_type_id int
);

create table videos.etiqueta(
    id int primary key,
    nome text
);


// pesquisa de todos os videos de determinado autor
create table videos.video_per_author(
    id int,
    nome text,
    descricao text,
    data_upload timestamp,
    
    user_id int,
    followers_ids set<int>,
    ratings_sum int,
    ratings_len int,
    ratings_avg float,
    etiqueta_id set<int>,

    primary key(user_id, id)
);

// permitir a pesquisa de comentários por utilizador, ordenado inversamente pela data
create table videos.comentario_per_author_per_data(
    id int,
    conteudo text,
    data timestamp,

    video_id int,
    user_id int,

    primary key(user_id, data, id)
) with clustering order by (data DESC);

// Permitir a pesquisa de comentários por vídeos, ordenado inversamente pela data
create table videos.comentario_per_video_per_data(
    id int,
    conteudo text,
    data timestamp,

    video_id int,
    user_id int,

    primary key(video_id, data, id)
) with clustering order by (data DESC);

// Permitir a pesquisa do rating médio de um vídeo e quantas vezes foi votado
create table videos.video_per_rating(
    id int,
    nome text,
    descricao text,
    data_upload timestamp,
    
    user_id int,
    followers_ids set<int>,
    ratings_sum int,
    ratings_len int,
    ratings_avg float,
    etiqueta_id set<int>,

    primary key(ratings_avg, ratings_len, id)
);

// d) 4
create table videos.evento_per_user(
    id int,
    data timestamp,
    tempo_video int,

    video_id int,
    user_id int,
    event_type_id int,

    primary key ((user_id, video_id), data, id)
) with clustering order by (data DESC);
