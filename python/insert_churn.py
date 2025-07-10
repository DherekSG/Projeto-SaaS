import pandas as pd
import psycopg2
import numpy as np
from dotenv import load_dotenv
import os

# Carregar variáveis do .env
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

CSV_FILE = "inserts_churn.csv"

COLUNAS = [
    'empresa_id', 'cons_12m', 'cons_gas_12m', 'cons_last_month',
    'forecast_cons_12m', 'forecast_cons_year', 'forecast_discount_energy',
    'forecast_meter_rent_12m', 'forecast_price_energy_off_peak', 'forecast_price_energy_peak',
    'forecast_price_pow_off_peak', 'imp_cons', 'margin_gross_pow_ele', 'margin_net_pow_ele',
    'nb_prod_act', 'net_margin', 'num_years_antig', 'pow_max',
    'channel_sales_EWPAKWLLIWISIWDUIBDLFMALXOWMWPCI',
    'channel_sales_FIXDBUFSEFWOOAASFCXDXADSIEKOCEAA',
    'channel_sales_FOOSDFPFKUSACIMWKCSOSBICDXKICAUA',
    'channel_sales_LMKEBAMCAACLUBFXADLMUECCXOIMLEMA',
    'channel_sales_MISSING', 'channel_sales_SDDIEDCSLFSLKCKWLFKDPOEEAILFPEDS',
    'channel_sales_USILXUPPASEMUBLLOPKAAFESMLIBMSDF',
    'has_gas_T', 'origin_up_KAMKKXFXXUWBDSLKWIFMMCSIUSIUOSWS',
    'origin_up_LDKSSXWPMEMIDMECEBUMCIEPIFCAMKCI',
    'origin_up_LXIDPIDDSBXSBOSBOUDACOCKEIMPUEPW',
    'origin_up_MISSING', 'origin_up_USAPBEPCFOLOEKILKWSDIBOSLWAXOBDP',
    'churn_previsto', 'probabilidade_churn'
]

def inserir_churn():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()

        df = pd.read_csv(CSV_FILE).drop(columns=["Unnamed: 0"], errors="ignore")
        df = df.where(pd.notnull(df), None)

        for _, row in df[COLUNAS].iterrows():
            try:
                valores = []
                for col in COLUNAS:
                    val = row[col]
                    if pd.isna(val):
                        valores.append(None)
                    elif col == 'churn_previsto':
                        valores.append(True if int(val) == 1 else False)
                    elif isinstance(val, (np.integer, int)):
                        valores.append(int(val))
                    elif isinstance(val, (np.floating, float)):
                        valores.append(float(val))
                    elif isinstance(val, (np.bool_, bool)):
                        valores.append(bool(val))
                    else:
                        valores.append(str(val))
                valores = tuple(valores)

                cursor.execute(f"""
                    INSERT INTO predicoes_churn (
                        {', '.join(COLUNAS)}
                    ) VALUES (
                        {', '.join(['%s'] * len(COLUNAS))}
                    )
                """, valores)
            except Exception as e:
                print(f"Erro ao inserir linha: {e}")

        conn.commit()
        print("Inserção de churn concluída.")
    except Exception as e:
        print("Erro na conexão ou inserção:", e)
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

if __name__ == "__main__":
    inserir_churn()
