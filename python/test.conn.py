import os
from psycopg import connect, OperationalError
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def test_connection():
    conn = None
    try:
        conn = connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        print("Conexão com o banco de dados bem-sucedida!")
    except OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    finally:
        if conn is not None:
            conn.close()
            print("Conexão fechada.")

if __name__ == "__main__":
    test_connection()