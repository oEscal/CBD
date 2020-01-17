from connect import *
import argparse


def print_results(result):
    for r in result:
        print(r)

def query_1(session, video_id):
    print("\n\nOs últimos 3 comentários introduzidos para um vídeo")

    try:
        query = f"""
                SELECT * 
                FROM videos.comentario_per_video_per_data WHERE video_id = {video_id}
                ORDER BY data DESC
                LIMIT 3;
                """
        print_results(session.execute(query))
    except Exception as e:
        print(f"Error:\n{e}\n")

def query_2(session, video_id):
    print("\n\nLista das tags de determinado vídeo")

    try:
        query = f"""
                SELECT etiqueta_id
                FROM videos.video WHERE id = {video_id};
                """
        print_results(session.execute(query))
    except Exception as e:
        print(f"Error:\n{e}\n")

def query_3(session, tag_id):
    print("\n\nTodos os vídeos com a tag Aveiro")

    try:
        query = f"""
                SELECT *
                FROM videos.video WHERE etiqueta_id CONTAINS {tag_id};
                """
        print_results(session.execute(query))
    except Exception as e:
        print(f"Error:\n{e}\n")

def query_4(session, user_id, video_id):
    print("\n\nOs últimos 5 eventos de determinado vídeo realizados por um utilizador")

    try:
        query = f"""
                SELECT *
                FROM videos.evento_per_user WHERE user_id = {user_id} and video_id = {video_id}
                ORDER BY data DESC
                LIMIT 5;
                """
        print_results(session.execute(query))
    except Exception as e:
        print(f"Error:\n{e}\n")


def main(args):
    session = connect(args.keyspace, args.addr, args.port)

    query_1(session, input("Id do video: "))
    query_2(session, input("\n\nId do video: "))
    query_3(session, input("\n\nId da tag Aveiro: "))
    query_4(session, input("\n\nId do utilizador: "), input("Id do video: "))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("--port", help="Port", type=int, default=9042)
    parser.add_argument("--addr", help="IP Address", default="127.0.0.1")
    parser.add_argument("--keyspace", help="Keyspace name", default="videos")
    
    args = parser.parse_args()
    main(args)
