import csv
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

# Carregar variáveis do .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

CSV_FILE = "inserts_empresas.csv"

def inserir_empresas():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()

        with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    cursor.execute("""
                        INSERT INTO empresas (nome, cnpj, email, telefone, senha_hash)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (cnpj) DO NOTHING
                    """, (
                        row['nome'],
                        row['cnpj'],
                        row['email'],
                        row['telefone'],
                        row['senha_hash']
                    ))
                except Exception as e:
                    print(f"Erro ao inserir empresa {row['nome']}: {e}")

        conn.commit()
        print("Inserção concluída.")
    except Exception as e:
        print("Erro na conexão ou inserção:", e)
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

if __name__ == "__main__":
    inserir_empresas()
