from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.transaction import (
    TransactionCreate,
    TransactionUpdate,
    TransactionResponse,
)
from app.services import transaction_service

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"],
)


@router.post(
    "/",
    response_model=TransactionResponse,
    status_code=201,
    summary="Create Transaction",
    description="Creates a new income or expense transaction."
)
def create_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db),
):
    return transaction_service.create_transaction(db, transaction)

@router.get(
    "/",
    response_model=list[TransactionResponse],
    summary="Get All Transactions",
    description="Returns all stored transactions."
)
def get_transactions(
    db: Session = Depends(get_db),
):
    return transaction_service.get_transactions(db)


@router.get(
    "/{transaction_id}",
    response_model=TransactionResponse,
    summary="Get Transaction",
    description="Returns a transaction using its ID."
)
def get_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
):
    transaction = transaction_service.get_transaction(db, transaction_id)

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return transaction


@router.put(
    "/{transaction_id}",
    response_model=TransactionResponse,
    summary="Update Transaction",
    description="Updates an existing transaction."
)
def update_transaction(
    transaction_id: int,
    transaction: TransactionUpdate,
    db: Session = Depends(get_db),
):
    updated_transaction = transaction_service.update_transaction(
        db,
        transaction_id,
        transaction,
    )

    if not updated_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return updated_transaction


@router.delete(
    "/{transaction_id}",
    summary="Delete Transaction",
    description="Deletes a transaction by ID."
)
def delete_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
):
    deleted_transaction = transaction_service.delete_transaction(
        db,
        transaction_id,
    )

    if not deleted_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    return {"message": "Transaction deleted successfully"}