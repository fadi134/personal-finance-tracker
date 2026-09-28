import csv
from sqlalchemy import and_


def read_csv(file):

    decoded_file = file.file.read().decode("utf-8").splitlines()

    reader = csv.DictReader(decoded_file)

    data = []

    for row in reader:
        data.append(row)

    return data


from datetime import datetime


def validate_csv(data):

    errors = []

    for index, row in enumerate(data, start=2):

        # Date
        try:
            datetime.strptime(row["date"], "%Y-%m-%d")
        except:
            errors.append(f"Row {index}: Invalid date.")

        # Description
        if not row["description"].strip():
            errors.append(f"Row {index}: Description is required.")

        # Amount
        try:
            amount = float(row["amount"])

            if amount <= 0:
                errors.append(
                    f"Row {index}: Amount must be greater than 0."
                )

        except:
            errors.append(f"Row {index}: Invalid amount.")

        # Transaction Type
        if row["transaction_type"] not in [
            "Income",
            "Expense"
        ]:
            errors.append(
                f"Row {index}: Invalid transaction type."
            )

    return errors


from app.models.transaction import Transaction


def import_transactions(db, data):

    imported = 0
    duplicates = 0

    for row in data:

        transaction_date = datetime.strptime(
            row["date"],
            "%Y-%m-%d"
        ).date()

        amount = float(row["amount"])

        existing_transaction = (
            db.query(Transaction)
            .filter(
                and_(
                    Transaction.date == transaction_date,
                    Transaction.description == row["description"],
                    Transaction.amount == amount,
                    Transaction.transaction_type == row["transaction_type"],
                )
            )
            .first()
        )

        if existing_transaction:
            duplicates += 1
            continue

        transaction = Transaction(
            date=transaction_date,
            description=row["description"],
            amount=amount,
            transaction_type=row["transaction_type"],
            category=row["category"],
            source="CSV",
        )

        db.add(transaction)

        imported += 1

    db.commit()

    return {
    "total_rows": len(data),
    "imported": imported,
    "duplicates": duplicates,
    "failed": len(data) - imported - duplicates,
    }