from fastapi import FastAPI, HTTPException, status, Response, APIRouter
from models import contas_request, contas_response


# Exemplo de banco de dados
contas = {
    1: {
        'descricao': 'conta de luz',
        'valor': 150,
        'status': 'pago'
    },
    2: {
        'descricao': 'conta de agua',
        'valor': 140,
        'status': 'pago'
    },
    3: {
        'descricao': 'conta de internet',
        'valor': 130,
        'status': 'pago'
    }

}

router = APIRouter()


@router.get('/api/v1/contas')
async def get_contas():
    return contas


@router.get('/api/v1/contas/{contas_id}')
async def get_conta(contas_id: int):
    try:
        conta = contas[contas_id]
        return conta
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada."
        )


@router.post('/api/v1/contas', status_code=status.HTTP_201_CREATED)
async def post_conta(conta: contas_request):
    next_id: int = len(contas) + 1
    contas[next_id] = conta
    return conta


@router.put(f'/api/v1/contas/contas_id')
async def put_contas(contas_id: int, conta: contas_request):
    if contas_id in contas:
        contas[contas_id] = conta
        contaresponse = contas[contas_id]
        return contaresponse
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id da conta não existe."
        )


@router.delete('/api/v1/contas/{contas_id}')
async def delete_conta(contas_id: int):
    if contas_id in contas:
        del contas[contas_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Id da conta não existe."
        )
