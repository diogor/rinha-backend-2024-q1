import os
from datetime import datetime
from typing import Literal, Tuple
import psycopg
from psycopg_pool import ConnectionPool

conn = ConnectionPool(os.getenv("DATABASE_URL"))

class NotFoundError(Exception):
    pass

async def create_transaction(client_id: int, amount: int, descricao: str, tipo: Literal["c", "d"]) -> None:
    try:
        with conn.connection() as c:
            with c.cursor() as cur:
                cur.execute(
                    'INSERT INTO transacoes (codigo_cliente, valor, descricao, tipo, data_transacao) VALUES (%s, %s, %s, %s, %s)',
                    (client_id, amount, descricao, tipo, datetime.now())
                )
    except psycopg.errors.ForeignKeyViolation:
        raise NotFoundError("Client not found")


def get_balance(client_id: int) -> Tuple[int, int]:
    with conn.getconn() as c:
        with c.cursor() as cur:
            cur.execute(
                "SELECT saldo, limite FROM clientes WHERE id = %s",
                (client_id,)
            )
            res = cur.fetchone()

    if not res:
        raise NotFoundError("Client not found")

    return res[0], res[1]
