from fastapi import APIRouter, UploadFile, File
from app.services import import_service
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db

router = APIRouter(
    prefix="/import",
    tags=["Import"],
)


@router.post("/csv")
async def upload_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    data = import_service.read_csv(file)

    errors = import_service.validate_csv(data)

    if errors:
        return {
        "status": "failed",
        "errors": errors
    }

    summary = import_service.import_transactions(
    db,
    data,
    )

    return {
    "status": "success",
    "filename": file.filename,
    "summary": summary,
    }