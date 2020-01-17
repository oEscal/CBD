import random


NUMBER_USERS = 10
NUMBER_VIDEOS = 30
NUMBER_COMENTARIOS = 30
TIPO_EVENTO = ["PLAY", "PAUSE", "STOP"]
NUMBER_EVENTO = 30
NUMBER_TAGS = 10

VIDEO_TABLES = ["video", "video_per_author", "video_per_rating"]
COMMENT_TABLES = ["comentario", "comentario_per_author_per_data", "comentario_per_video_per_data"]
EVENT_TABLES = ["evento", "evento_per_user"]


def insert_utilizador(number):
    return f"insert into videos.utilizador (id, username, nome, email, data_registo)" \
            f" values({number}, 'ola{number}', 'ola adeus{number}', 'ola{number}@adeus.com', dateof(now()));\n"

def insert_video(number, user_id, followers, ratings, tag):
    result = ""
    for t_name in VIDEO_TABLES:
        result += f"insert into videos.{t_name}(id, nome, descricao, data_upload, user_id, followers_ids, ratings_sum, ratings_len, ratings_avg, etiqueta_id) " \
                    f"values ({number}, 'era uma vez {number}', 'uma história sobre algo {number}', dateof(now()), {user_id}, {followers}, {sum(ratings)}, {len(ratings)}, {sum(ratings)/len(ratings)}, {tag});\n"
    return result

def insert_comentario(number, video_id, user_id):
    result = ""
    for t_name in COMMENT_TABLES:
        result += f"insert into videos.{t_name}(id, conteudo, data, video_id, user_id) " \
                    f"values({number}, 'bueda fixe oh manu {number}', dateof(now()), {video_id}, {user_id});\n"
    return result

def insert_tipo_evento(number, tipo):
    return f"insert into videos.tipo_evento(id, nome) values({number}, '{tipo}');\n"

def insert_evento(number, time_video, video_id, user_id, event_type_id):
    result = ""
    for t_name in EVENT_TABLES:
        result += f"insert into videos.{t_name}(id, data, tempo_video, video_id, user_id, event_type_id) " \
                    f"values({number}, dateof(now()), {time_video}, {video_id}, {user_id}, {event_type_id});\n"
    return result

def insert_tag(number):
    return f"insert into videos.etiqueta(id, nome) values({number}, 'hmmm{number}');\n"


def main():
    result = ""
    for n in range(NUMBER_USERS):
        result += insert_utilizador(n)
    for n in range(NUMBER_VIDEOS):
        result += insert_video(
            n, 
            random.randint(0, NUMBER_USERS - 1), 
            str({random.randint(0, NUMBER_USERS - 1) for i in range(random.randint(1, NUMBER_USERS - 1))}), 
            [random.randint(0, 5) for i in range(random.randint(1, 10))],
            str({random.randint(0, NUMBER_TAGS - 1) for i in range(random.randint(1, NUMBER_TAGS))})
        )
    for n in range(NUMBER_COMENTARIOS):
        result += insert_comentario(
            n, 
            random.randint(0, NUMBER_VIDEOS - 1), 
            random.randint(0, NUMBER_USERS - 1)
        )
    for n in range(len(TIPO_EVENTO)):
        result += insert_tipo_evento(n, TIPO_EVENTO[n])
    for n in range(NUMBER_EVENTO):
        result += insert_evento(
            n, 
            random.randint(0, 100000), 
            random.randint(0, NUMBER_VIDEOS - 1), 
            random.randint(0, NUMBER_USERS - 1), 
            random.randint(0, len(TIPO_EVENTO) - 1)
        )
    for n in range(NUMBER_TAGS):
        result += insert_tag(n)

    with open("2_database_insert.cql", 'w') as file:
        file.write(result)
    print("DONE")


if __name__ == '__main__':
    main()
