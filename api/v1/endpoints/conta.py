from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.contas_models import contas_model
from schemas.contas_schema import contas_schema
from core.deps import get_session


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=contas_schema)
async def post_conta(conta: contas_schema, db: AsyncSession = Depends(get_session)):
    nova_conta = contas_model(descricao=contas_model.descricao,
                              valor=contas_model.valor, status=contas_model.status)

    db.add(nova_conta)
    await db.commit()

    return nova_conta


@router.get('/', response_model=List[contas_schema])
async def get_contas(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(contas_model)
        result = await session.execute(query)
        contas: List[contas_model] = result.scalars().all()

        return contas


@router.get('/{conta_id}', response_model=contas_schema, status_code=status.HTTP_200_OK)
async def get_conta(conta_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(contas_model).filter(contas_model.id == conta_id)
        result = await session.execute(query)
        conta = result.scalar_one_or_none()

        if conta:
            return conta
        else:
            raise HTTPException(detail='Conta não encontrada.', status_code=status.HTTP_404_NOT_FOUND)


@router.put('/{conta_id}', response_model=contas_schema, status_code=status.HTTP_202_ACCEPTED)
async def put_conta(conta_id: int, conta: contas_schema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(contas_model).filter(contas_model.id == conta_id)
        result = await session.execute(query)
        conta_nova = result.scalar_one_or_none()

        if conta_nova:
            conta_nova.descricao = conta.descricao
            conta_nova.valor = conta.valor
            conta_nova.status = conta.status

            await session.commit()

            return conta_nova
        else:
            raise HTTPException(detail='Conta não encontrada.', status_code=status.HTTP_404_NOT_FOUND)


@router.delete('/{conta_id}', status_code=status.HTTP_202_ACCEPTED)
async def delete_conta(conta_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(contas_model).filter(contas_model.id == conta_id)
        result = await session.execute(query)
        conta_delete = result.scalar_one_or_none()

        if conta_delete:
            await session.delete(conta_delete)
            await session.commit()

            return Response(status_code= status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Conta não encontrada.', status_code=status.HTTP_404_NOT_FOUND)
