from connect import *
import argparse


def insert_user(session, id, username, nome, email):
    try:
        insert_query = f"""
                        INSERT INTO utilizador (id, username, nome, email, data_registo)
                        VALUES ({id}, '{username}', '{nome}', '{email}', dateof(now()))
                        """
        session.execute(insert_query)
        print("\nSuccess")
    except Exception as e:
        print(f"Error:\n{e}\n")

def update_user(session, id, username, nome, email):
    try:
        update_query = f"""
                        UPDATE utilizador set username='{username}', nome='{nome}', email='{email}', data_registo=dateof(now())
                        WHERE id={id}
                        """
        session.execute(update_query)
        print("\nSuccess")
    except Exception as e:
        print(f"Error:\n{e}\n")

def search_table(session):
    try:
        print("Filmes na base de dados")
        rows = session.execute('SELECT * FROM video')
        for row in rows:
            print(row.nome)
    except Exception as e:
        print(f"Error:\n{e}\n")

def main(args):
    session = connect(args.keyspace, args.addr, args.port)

    if args.insert:
        print("Query para inserir um novo utilizador.\n\nDados do novo utilizador:")
        insert_user(
            session,
            input("id: "),
            input("username: "),
            input("nome: "),
            input("email: ")
        )
    elif args.edit:
        print("Query para editar um utilizador.\n\nDados:")
        update_user(
            session,
            input("id do utilizador a editar: "),
            input("novo username: "),
            input("novo nome: "),
            input("novo email: ")
        )
    elif args.search:
        search_table(session)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("--port", help="Port", type=int, default=9042)
    parser.add_argument("--addr", help="IP Address", default="127.0.0.1")
    parser.add_argument("--keyspace", help="Keyspace name", default="videos")
    
    parser.add_argument("-i", "--insert", help="Insert demonstration", action="store_true")
    parser.add_argument("-e", "--edit", help="Edit demonstration", action="store_true")
    parser.add_argument("-s", "--search", help="Search demonstration", action="store_true")

    args = parser.parse_args()
    main(args)
