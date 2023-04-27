from fastapi import FastAPI,HTTPException,status,Response


from models import contas_request, contas_response


# Exemplo de banco de dados
contas = {
    1: {
        'descricao': 'Conta de luz',
        'valor': 150,
        'status': 'pago'
    },
    2: {
        'descricao': 'Conta de agua',
        'valor': 100,
        'status': 'pago'
    },
    3: {
        'descricao': 'Conta de internet',
        'valor': 120,
        'status': 'pago'
    }
}

app = FastAPI()



@app.get('/contas')
async def get_contas():
    return contas


@app.get('/contas/{contas_id}')
async def get_conta(contas_id: int):
    try:
        conta = contas[contas_id]
        return conta
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada."
        )



@app.post('/contas', status_code=status.HTTP_201_CREATED)
async def post_conta(conta: contas_request):
    next_id: int = len(contas) + 1
    contas[next_id] = conta
    return conta


@app.put('/contas/{contas_id}')
async def put_contas(contas_id: int, conta: contas):
    if contas_id in contas:
        contas[contas_id] = conta
        return conta
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id da conta não existe."
        )


@app.delete('/contas/{contas_id}')
async def delete_conta(contas_id: int):
    if contas_id in contas:
        del contas[contas_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id da conta não existe."
        )





if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8001)
