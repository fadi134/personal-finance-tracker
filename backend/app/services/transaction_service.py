from sqlalchemy.orm import Session
from app.utils.logger import logger

from app.models.transaction import Transaction
from app.schemas.transaction import (
    TransactionCreate,
    TransactionUpdate,
)


def create_transaction(db: Session, transaction: TransactionCreate):
    db_transaction = Transaction(
        date=transaction.date,
        description=transaction.description,
        amount=transaction.amount,
        transaction_type=transaction.transaction_type,
        category=transaction.category,
        source=transaction.source,
    )

    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    logger.info(f"Transaction created successfully. ID={db_transaction.id}")

    return db_transaction

def get_transactions(db: Session):
    return db.query(Transaction).all()


def get_transaction(db: Session, transaction_id: int):
    return (
        db.query(Transaction)
        .filter(Transaction.id == transaction_id)
        .first()
    )


def update_transaction(
    db: Session,
    transaction_id: int,
    transaction: TransactionUpdate,
):
    db_transaction = (
        db.query(Transaction)
        .filter(Transaction.id == transaction_id)
        .first()
    )

    if not db_transaction:
        return None

    update_data = transaction.model_dump(
    exclude_unset=True,
    exclude_none=True
)
    for key, value in update_data.items():
        setattr(db_transaction, key, value)

    db.commit()
    db.refresh(db_transaction)
    logger.info(f"Transaction updated successfully. ID={db_transaction.id}")

    return db_transaction


def delete_transaction(db: Session, transaction_id: int):
    db_transaction = (
        db.query(Transaction)
        .filter(Transaction.id == transaction_id)
        .first()
    )

    if not db_transaction:
        return None

    db.delete(db_transaction)
    db.commit()
    logger.info(f"Transaction deleted successfully. ID={transaction_id}")

    return db_transaction