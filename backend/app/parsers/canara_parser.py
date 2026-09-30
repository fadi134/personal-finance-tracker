import re
from datetime import datetime
from app.schemas.transaction import TransactionCreate

DATE_PATTERN = r"^\d{2}-\d{2}-\d{4}"


def parse_canara_statement(pdf_text):

    transactions = []

    lines = pdf_text.split("\n")

    description = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # Transaction line starts with date
        if re.match(DATE_PATTERN, line):

            parts = line.split()

            date = parts[0]

            amount = parts[-2].replace(",", "")

            balance = parts[-1].replace(",", "")

            description_text = " ".join(description)

            if "UPI/CR" in description_text:
                transaction_type = "Income"
            else:
                transaction_type = "Expense"

            transactions.append(
                TransactionCreate(
                    date=datetime.strptime(date, "%d-%m-%Y").date(),
                    description=description_text,
                    amount=float(amount),
                    transaction_type=transaction_type,
                    category=None,
                    source="PDF"
                    )
                )

            description = []

        else:

            # Ignore time
            if re.match(r"^\d{2}:\d{2}:\d{2}$", line):
                continue

            # Ignore cheque number
            if line.startswith("Chq:"):
                continue

            description.append(line)

    return transactions