import os
from dataclasses import dataclass
from typing import Literal
from blacksheep import Application, FromJSON, Response, post

from services import NotFoundError, create_transaction

app = Application()

@dataclass
class TransactionRequest:
    valor: int
    descricao: str
    tipo: Literal["c", "d"]

@post("/clientes/{client_id}/transacoes")
async def index(client_id: int, input: FromJSON[TransactionRequest]):
    transaction = input.value
    try:
        await create_transaction(client_id, transaction.valor, transaction.descricao, transaction.tipo)
    except NotFoundError:
        return Response(status=404)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 3000)))
