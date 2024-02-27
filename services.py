import os
from datetime import datetime
from typing import Literal
import psycopg2

conn = psycopg2.connect(os.getenv("DATABASE_URL"))

def create_transaction(client_id: int, amount: int, descricao: str, tipo: Literal["c", "d"]) -> None:
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO transacoes (codigo_cliente, valor, descricao, tipo, data_transacao) VALUES (%s, %s, %s, %s, %s)',
        (client_id, amount, descricao, tipo, datetime.now())
    )
    conn.commit()
