from fastapi import APIRouter, UploadFile, File, Form
from sqlalchemy.orm import Session
from fastapi import Depends

from app.database.connection import get_db
from app.services.transaction_service import create_transaction
from app.parsers.pdf_reader import extract_text_from_pdf
from app.parsers.canara_parser import parse_canara_statement

router = APIRouter(
    prefix="/import",
    tags=["PDF Import"]
)


@router.post("/pdf")
async def import_pdf(
    bank: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    pdf_bytes = await file.read()

    text = extract_text_from_pdf(pdf_bytes)

    transactions = parse_canara_statement(text)
    saved_transactions = []

    for transaction in transactions:
        db_transaction = create_transaction(db, transaction)
        saved_transactions.append(db_transaction)
    return {
    "message": "PDF imported successfully.",
    "bank": bank,
    "filename": file.filename,
    "transactions_imported": len(saved_transactions)
}