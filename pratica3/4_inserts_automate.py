import random


NUMBER_MOVIES = 300
NUMBER_USERS = 50

RATING_TABLES = ["ratings_by_user", "ratings_by_movie"]
MOVIES_TABLES = ["movies", "movies_per_rating_per_date"]

REVIEWS = ["bom", "muito bom", "mau", "péssimo", "depois disto, considero sinceramente o suicídio", "deveras interessante"]
GENRES = ["Action", "Thriller", "Drama", "Comedy", "Science fiction", "History", "Biography"]
AREAS = ["Acting", "Subject", "Clothes", "Special Effects", "Music"]


def insert_movie(number, avg_rating, genres, release_date, reviews):
    result = ""
    for t_name in MOVIES_TABLES:
        result += f"insert into movielens.{t_name} (id, avg_rating, genres, name, release_date, url, reviews)" \
                    f" values({number}, {avg_rating}, {str(genres) if len(genres) > 0 else '{}'}, 'ola{number}', '{release_date}', 'www.ola{number}.com', {reviews});\n"
    return result

def insert_user(number, age, gender, zip_code):
    return f"insert into movielens.users (id, address, age, city, gender, name, occupation, zip)" \
            f" values({number}, 'Aqui, nº {number}', {age}, 'Unknown {number}', '{gender}', 'Pessoa {number}', 'Engenheiro de obras feitas', '{zip_code}');\n"

def insert_rating(movie_id, user_id, rating, rating_per_area):
    result = ""
    for t_name in RATING_TABLES:
        result += f"insert into movielens.{t_name} (movie_id, user_id, rating, rating_per_area)" \
            f" values({movie_id}, {user_id}, {rating}, {str(rating_per_area)});\n"
    return result


def main():
    result = ""
    for n in range(NUMBER_MOVIES):
        result += insert_movie(
            n, 
            random.randrange(0, 10), 
            {GENRES[random.randint(0, len(GENRES) - 1)] for i in range(random.randint(0, len(GENRES)))},
            f"{random.randint(1920, 2019)}-{random.randrange(1, 12)}-{random.randrange(1, 28)}",
            [GENRES[random.randint(0, len(REVIEWS) - 1)] for i in range(random.randint(0, len(REVIEWS)))]
        ) + insert_rating(
            n, 
            random.randint(0, NUMBER_USERS - 1),
            random.randint(0, 10), 
            {AREAS[random.randint(0, len(AREAS) - 1)]: random.randint(0, 10) for i in range(random.randint(0, len(AREAS) - 1))}
        )
    for n in range(NUMBER_USERS):
        result += insert_user(
            n, 
            random.randint(16, 100), 
            random.choice(['M', 'F']),
            f"{random.randint(1000, 9999)}-{random.randint(100, 999)}"
        )

    with open("4_database_insert.cql", 'w') as file:
        file.write(result)
    print("DONE")


if __name__ == '__main__':
    main()
